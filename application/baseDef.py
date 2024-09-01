import streamlit as st
import pandas as pd
import os

@st.cache_data
def df_to_csv(df:pd.DataFrame):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode()

@st.cache_data
def get_list():
    return pd.read_csv(os.path.join("data","list.csv")).set_index('id')


@st.cache_data
def get_id():
    id3 = pd.read_csv(os.path.join("data","id3.csv")).set_index('id')
    id4 = pd.read_csv(os.path.join("data","id4.csv")).set_index('id')
    return (id3, id4)

@st.cache_data
def get_ego():
    ego3 = pd.read_csv(os.path.join("data","ego3.csv"), dtype=str).set_index('id')
    ego4 = pd.read_csv(os.path.join("data","ego4.csv"), dtype=str).set_index('id')
    return (ego3, ego4)

def merge_id(idList:pd.DataFrame, id3:pd.DataFrame, id4:pd.DataFrame):
    idList = idList.copy()
    id3 = id3.copy()
    id4 = id4.copy()

    for i in id3.index:
        if (idList.loc[i,"uptie"] == 4).all():
            id3.loc[i] = id4.loc[i]

    id3["hp"] = round((idList['Lv'] * id3['hp_coeffic']) + id3['hp_const'])
    id3["atkLv"] = idList['Lv'] + id3['atkLv_mean']
    id3["defenceLv"] = idList['Lv'] + id3['defLv']

    return id3

def merge_ego(egoList:pd.DataFrame, ego3:pd.DataFrame, ego4:pd.DataFrame):
    egoList = egoList.copy()
    ego3 = ego3.copy()
    ego4 = ego4.copy()

    for i in ego3.index:
        if (egoList.loc[i,"uptie"] == 4).all():
            ego3.loc[i] = ego4.loc[i]

    return ego3

def make_idList():
    idList = st.session_state['list'].loc[st.session_state['list']['Lv'] > 0]
    id3, id4 = get_id()
    st.session_state['id'] = merge_id(idList, id3, id4)
    
def make_egoList():
    egoList = st.session_state['list'].loc[st.session_state['list']["Lv"].isnull()]
    ego3, ego4 = get_ego()
    st.session_state['ego'] = merge_ego(egoList, ego3, ego4)

def start_data():
    if 'list' not in st.session_state:
        st.session_state['list'] = get_list()
    
    if 'id' not in st.session_state:
        make_idList()

    if 'ego' not in st.session_state:
        make_egoList()
