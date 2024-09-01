import streamlit as st
import pandas as pd
from application import baseDef as bd

MAX_LEVEL = 45
MAX_UPTIE = 4

st.header("설정")
st.write(" \n ")
st.write(" \n ")

uploaded_data = st.file_uploader("설정 업로드", "csv", help="LCDeckMaker_settings.csv")
if uploaded_data is not None:
    uploaded_data = pd.read_csv(uploaded_data).set_index("id")
    for i in uploaded_data.index:
        st.session_state["list"].loc[i] = uploaded_data.loc[i]

idList = st.session_state["list"].copy()
idList = idList.loc[idList["Lv"] > 0]

egoList = st.session_state["list"].copy()
egoList = egoList.loc[egoList["Lv"].isnull()]

Id, Ego = st.tabs(["인격", "E.G.O"])

with Id:
    _, __, lv, t = Id.columns(4)
    if lv.button("레벨 초기화"):
        idList["Lv"] = MAX_LEVEL
    if t.button("동기화 일괄 변경", key="i"):
        if (idList["uptie"] == 3).any():
            idList["uptie"] = 4
        else:
            idList["uptie"] = 3
    
    idList = Id.data_editor(idList, hide_index=True,
                            column_order=['sinner','identity',"Lv",'uptie'],
                            column_config={
                                'sinner': '수감자',
                                'identity': '인격',
                                'Lv': st.column_config.NumberColumn(
                                    min_value=1,
                                    max_value=MAX_LEVEL,
                                    step=1
                                ),
                                'uptie': st.column_config.NumberColumn(
                                    "동기화",
                                    min_value=3,
                                    max_value=MAX_UPTIE,
                                    step=1
                                )
                            },
                            use_container_width=True,
                            num_rows="fixed",
                            disabled=('sinner','identity'))

with Ego:
    ___, ____, ts = Ego.columns(3)
    if ts.button("동기화 일괄 변경", key="e"):
        if (egoList["uptie"] == 3).any():
            egoList["uptie"] = 4
        else:
            egoList["uptie"] = 3
    
    egoList = Ego.data_editor(egoList, hide_index=True,
                              column_order=['sinner','ego','uptie'],
                              column_config={
                                'sinner': '수감자',
                                'ego': 'E.G.O',
                                'uptie': st.column_config.NumberColumn(
                                    "동기화",
                                    min_value=3,
                                    max_value=MAX_UPTIE,
                                    step=1
                                )
                              },
                              use_container_width=True,
                              num_rows="fixed",
                              disabled=('sinner','ego'))
    
st.session_state["list"] = pd.concat([idList, egoList])

st.download_button("설정 다운로드", bd.df_to_csv(st.session_state["list"]), "LCDeckMaker_settings.csv", use_container_width=True)