import streamlit as st
import pandas as pd
from collections import Counter

def has_duplicates(lst):
    return any(count > 1 for count in Counter(lst).values())

def color_sin_char(val):
    color = {
        "분노": 'color: #742820',
        "색욕": 'color: #a0512a',
        "나태": 'color: #cf7305',
        "탐식": 'color: #506c25',
        "우울": 'color: #28535b',
        "오만": 'color: #1e4570',
        "질투": 'color: #69407b',
        "취약": 'color: red',
        "내성": 'color: gray',
        "0": 'color: white',
        0: 'color: white'
    }
    
    return color.get(val, "")

def color_sin_char_zero(val):
    color = {
        "0": 'color: white',
        0: 'color: white'
    }
    
    return color.get(val, "")

def color_sin_bg(val):
    color = {
        "simpSinCnt_wrath": 'background-color: #f4cccc',
        "simpSinCnt_lust": 'background-color: #fce5cd',
        "simpSinCnt_sloth": 'background-color: #fff2cc',
        "simpSinCnt_gluttony": 'background-color: #d9ead3',
        "simpSinCnt_gloom": 'background-color: #d0e0e3',
        "simpSinCnt_pride": 'background-color: #c9daf8',
        "simpSinCnt_envy": 'background-color: #d9d2e9',

        "sinCnt_wrath": 'background-color: #f4cccc',
        "sinCnt_lust": 'background-color: #fce5cd',
        "sinCnt_sloth": 'background-color: #fff2cc',
        "sinCnt_gluttony": 'background-color: #d9ead3',
        "sinCnt_gloom": 'background-color: #d0e0e3',
        "sinCnt_pride": 'background-color: #c9daf8',
        "sinCnt_envy": 'background-color: #d9d2e9',

        "cost_wrath": 'background-color: #f4cccc',
        "cost_lust": 'background-color: #fce5cd',
        "cost_sloth": 'background-color: #fff2cc',
        "cost_gluttony": 'background-color: #d9ead3',
        "cost_gloom": 'background-color: #d0e0e3',
        "cost_pride": 'background-color: #c9daf8',
        "cost_envy": 'background-color: #d9d2e9',
        
        "ovclockcost_wrath": 'background-color: #f4cccc',
        "ovclockcost_lust": 'background-color: #fce5cd',
        "ovclockcost_sloth": 'background-color: #fff2cc',
        "ovclockcost_gluttony": 'background-color: #d9ead3',
        "ovclockcost_gloom": 'background-color: #d0e0e3',
        "ovclockcost_pride": 'background-color: #c9daf8',
        "ovclockcost_envy": 'background-color: #d9d2e9',
        }
    
    return [color.get(val.name, "") if i != 0 else "background-color: white" for i in val]

def real_format(value):
    if value % 1 == 0:
        return f"{value:.0f}"
    else:
        return f"{value:.1f}"

@st.cache_data
def start_maker():
    Id = st.session_state["id"]
    ego = st.session_state["ego"]
    li = st.session_state["list"]

    idList = {
        None: list(),
        '이상': li.loc[(li["sinner"] == '이상') & (li["ego"].isna()),"identity"].to_list(),
        '파우스트': li.loc[(li["sinner"] == '파우스트') & (li["ego"].isna()),"identity"].to_list(),
        '돈키호테': li.loc[(li["sinner"] == '돈키호테') & (li["ego"].isna()),"identity"].to_list(),
        '료슈': li.loc[(li["sinner"] == '료슈') & (li["ego"].isna()),"identity"].to_list(),
        '뫼르소': li.loc[(li["sinner"] == '뫼르소') & (li["ego"].isna()),"identity"].to_list(),
        '홍루': li.loc[(li["sinner"] == '홍루') & (li["ego"].isna()),"identity"].to_list(),
        '히스클리프': li.loc[(li["sinner"] == '히스클리프') & (li["ego"].isna()),"identity"].to_list(),
        '이스마엘': li.loc[(li["sinner"] == '이스마엘') & (li["ego"].isna()),"identity"].to_list(),
        '로쟈': li.loc[(li["sinner"] == '로쟈') & (li["ego"].isna()),"identity"].to_list(),
        '싱클레어': li.loc[(li["sinner"] == '싱클레어') & (li["ego"].isna()),"identity"].to_list(),
        '오티스': li.loc[(li["sinner"] == '오티스') & (li["ego"].isna()),"identity"].to_list(),
        '그레고르': li.loc[(li["sinner"] == '그레고르') & (li["ego"].isna()),"identity"].to_list()
    }

    egoList = {
        None: list(),
        '이상': li.loc[(li["sinner"] == '이상') & (li["identity"].isna()),"ego"].to_list(),
        '파우스트': li.loc[(li["sinner"] == '파우스트') & (li["identity"].isna()),"ego"].to_list(),
        '돈키호테': li.loc[(li["sinner"] == '돈키호테') & (li["identity"].isna()),"ego"].to_list(),
        '료슈': li.loc[(li["sinner"] == '료슈') & (li["identity"].isna()),"ego"].to_list(),
        '뫼르소': li.loc[(li["sinner"] == '뫼르소') & (li["identity"].isna()),"ego"].to_list(),
        '홍루': li.loc[(li["sinner"] == '홍루') & (li["identity"].isna()),"ego"].to_list(),
        '히스클리프': li.loc[(li["sinner"] == '히스클리프') & (li["identity"].isna()),"ego"].to_list(),
        '이스마엘': li.loc[(li["sinner"] == '이스마엘') & (li["identity"].isna()),"ego"].to_list(),
        '로쟈': li.loc[(li["sinner"] == '로쟈') & (li["identity"].isna()),"ego"].to_list(),
        '싱클레어': li.loc[(li["sinner"] == '싱클레어') & (li["identity"].isna()),"ego"].to_list(),
        '오티스': li.loc[(li["sinner"] == '오티스') & (li["identity"].isna()),"ego"].to_list(),
        '그레고르': li.loc[(li["sinner"] == '그레고르') & (li["identity"].isna()),"ego"].to_list()
    }

    return (Id, ego, li, idList, egoList)

st.header("파티 구성")
st.write(" \n ")

Id, ego, li, idList, egoList = start_maker()

Set, reset = st.columns(2)

setting = Set.radio("죄악 자원 설정",
                    ["기본",'단기전'],
                    index=0,
                    captions=['스토리/거울굴절철도','거울 던전'],
                    help="'단기전' 옵션은 1~3턴 이내로 전투가 끝나는 경우에 맞춰 설정되었습니다.",
                    )

if reset.button("입력 초기화"):
    st.session_state["set_sinners1"] = [None,None,None,None,None,None]
    st.session_state["set_id"] = [None,None,None,None,None,None]
    st.session_state["set_sinners2"] = [None,None,None,None,None,None,None]
    st.session_state["set_ego"] = [None,None,None,None,None,None,None]
    st.session_state["set_sup"] = [None,None,None,None,None,None,None,None,None,None,None,None]
    st.session_state["ovclock"] = [False,False,False,False,False,False,False]

Input, Output = st.columns(2)
inputSinners, inputId = Input.columns(2)

with Input:
    sinners = ["이상", "파우스트", "돈키호테", "료슈", "뫼르소", "홍루",
               "히스클리프", "이스마엘", "로쟈", "싱클레어", "오티스", "그레고르"]

    sinner1 = inputSinners.selectbox("수감자1", sinners, index=st.session_state["set_sinners1"][0], placeholder="수감자 선택", label_visibility="collapsed")
    sinner2 = inputSinners.selectbox("수감자2", sinners, index=st.session_state["set_sinners1"][1], placeholder="수감자 선택", label_visibility="collapsed")
    sinner3 = inputSinners.selectbox("수감자3", sinners, index=st.session_state["set_sinners1"][2], placeholder="수감자 선택", label_visibility="collapsed")
    sinner4 = inputSinners.selectbox("수감자4", sinners, index=st.session_state["set_sinners1"][3], placeholder="수감자 선택", label_visibility="collapsed")
    sinner5 = inputSinners.selectbox("수감자5", sinners, index=st.session_state["set_sinners1"][4], placeholder="수감자 선택", label_visibility="collapsed")
    sinner6 = inputSinners.selectbox("수감자6", sinners, index=st.session_state["set_sinners1"][5], placeholder="수감자 선택", label_visibility="collapsed")

    try:
        st.session_state["set_sinners1"][0] = sinners.index(sinner1)
    except ValueError:
        st.session_state["set_sinners1"][0] = None
    try:
        st.session_state["set_sinners1"][1] = sinners.index(sinner2)
    except ValueError:
        st.session_state["set_sinners1"][1] = None
    try:
        st.session_state["set_sinners1"][2] = sinners.index(sinner3)
    except ValueError:
        st.session_state["set_sinners1"][2] = None
    try:
        st.session_state["set_sinners1"][3] = sinners.index(sinner4)
    except ValueError:
        st.session_state["set_sinners1"][3] = None
    try:
        st.session_state["set_sinners1"][4] = sinners.index(sinner5)
    except ValueError:
        st.session_state["set_sinners1"][4] = None
    try:
        st.session_state["set_sinners1"][5] = sinners.index(sinner6)
    except ValueError:
        st.session_state["set_sinners1"][5] = None



    try:
        st.session_state["set_id"][0] = idList[sinner1].index(inputId.selectbox("인격1", idList[sinner1], index=st.session_state["set_id"][0], placeholder="인격 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_id"][0] = None
    try:
        st.session_state["set_id"][1] = idList[sinner2].index(inputId.selectbox("인격2", idList[sinner2], index=st.session_state["set_id"][1], placeholder="인격 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_id"][1] = None
    try:
        st.session_state["set_id"][2] = idList[sinner3].index(inputId.selectbox("인격3", idList[sinner3], index=st.session_state["set_id"][2], placeholder="인격 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_id"][2] = None
    try:
        st.session_state["set_id"][3] = idList[sinner4].index(inputId.selectbox("인격4", idList[sinner4], index=st.session_state["set_id"][3], placeholder="인격 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_id"][3] = None
    try:
        st.session_state["set_id"][4] = idList[sinner5].index(inputId.selectbox("인격5", idList[sinner5], index=st.session_state["set_id"][4], placeholder="인격 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_id"][4] = None
    try:
        st.session_state["set_id"][5] = idList[sinner6].index(inputId.selectbox("인격6", idList[sinner6], index=st.session_state["set_id"][5], placeholder="인격 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_id"][5] = None

temp = [sinner1,sinner2,sinner3,sinner4,sinner5,sinner6]

if has_duplicates([i for i in temp if i != None ]):
    st.error("중복된 수감자가 있습니다.")

with Output:
    idNum = [0,0,0,0,0,0]
    for i in range(6):
        try:
            idNum[i] = int(li.loc[(li["sinner"] == temp[i]) & (li["identity"] == idList[temp[i]][st.session_state["set_id"][i]]), "id"])
        except TypeError:
            continue
    
    makerId = Id.loc[[i for i in idNum if i > 0]]

    if setting == "단기전":
        col = ["simpSinCnt_wrath",
               "simpSinCnt_lust",
               "simpSinCnt_sloth",
               "simpSinCnt_gluttony",
               "simpSinCnt_gloom",
               "simpSinCnt_pride",
               "simpSinCnt_envy"
               ]
    elif setting == "기본":
        col = ["sinCnt_wrath",
               "sinCnt_lust",
               "sinCnt_sloth",
               "sinCnt_gluttony",
               "sinCnt_gloom",
               "sinCnt_pride",
               "sinCnt_envy"
               ]
    if not makerId[col].empty:
        show_sinCnt = makerId[col].style.apply(color_sin_bg).apply(lambda x:
                                                                   ['color: black' if not pd.isna(i) else "" for i in x])\
                                                                    .applymap(color_sin_char_zero).format(real_format)
    else:
        show_sinCnt = pd.DataFrame({'sinCnt_wrath': [],
                                    'sinCnt_lust': [],
                                    'sinCnt_sloth': [],
                                    'sinCnt_gluttony': [],
                                    'sinCnt_gloom': [],
                                    'sinCnt_pride': [],
                                    'sinCnt_envy': []
                                    })
    Output.dataframe(show_sinCnt,
                     hide_index=True,
                     width=380, height=248,
                     column_config={'simpSinCnt_wrath': '분노',
                                    'simpSinCnt_lust': '색욕',
                                    'simpSinCnt_sloth': '나태',
                                    'simpSinCnt_gluttony': '탐식',
                                    'simpSinCnt_gloom': '우울',
                                    'simpSinCnt_pride': '오만',
                                    'simpSinCnt_envy': '질투',
                                    'sinCnt_wrath': '분노',
                                    'sinCnt_lust': '색욕',
                                    'sinCnt_sloth': '나태',
                                    'sinCnt_gluttony': '탐식',
                                    'sinCnt_gloom': '우울',
                                    'sinCnt_pride': '오만',
                                    'sinCnt_envy': '질투'
                                    })
    total = makerId[col].sum()
    Output.markdown(f'''<table border="1" width="380">
  <thead>
    <tr>
      <th style="background-color: #ea9999; color: black; text-align: center;">{real_format(total[0])}</th>
      <th style="background-color: #f9cb9c; color: black; text-align: center;">{real_format(total[1])}</th>
      <th style="background-color: #ffe599; color: black; text-align: center;">{real_format(total[2])}</th>
      <th style="background-color: #b6d7a8; color: black; text-align: center;">{real_format(total[3])}</th>
      <th style="background-color: #a2c4c9; color: black; text-align: center;">{real_format(total[4])}</th>
      <th style="background-color: #a4c2f4; color: black; text-align: center;">{real_format(total[5])}</th>
      <th style="background-color: #b4a7d6; color: black; text-align: center;">{real_format(total[6])}</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background-color: #f4cccc; color: black; text-align: center;">(+{makerId['def_sin'].value_counts().get('분노', 0)})</td>
      <td style="background-color: #fce5cd; color: black; text-align: center;">(+{makerId['def_sin'].value_counts().get('색욕', 0)})</td>
      <td style="background-color: #fff2cc; color: black; text-align: center;">(+{makerId['def_sin'].value_counts().get('나태', 0)})</td>
      <td style="background-color: #d9ead3; color: black; text-align: center;">(+{makerId['def_sin'].value_counts().get('탐식', 0)})</td>
      <td style="background-color: #d0e0e3; color: black; text-align: center;">(+{makerId['def_sin'].value_counts().get('우울', 0)})</td>
      <td style="background-color: #c9daf8; color: black; text-align: center;">(+{makerId['def_sin'].value_counts().get('오만', 0)})</td>
      <td style="background-color: #d9d2e9; color: black; text-align: center;">(+{makerId['def_sin'].value_counts().get('질투', 0)})</td>
    </tr>
  </tbody>
</table>
''', unsafe_allow_html=True)

with st.expander("주요 E.G.O"):
    eInput, eOutput = st.columns(2)
    eInputSinners, inputEgo, inputOvclock = eInput.columns(3)

    eInputSinners.write("")
    eInputSinners.write("")
    eInputSinners.write("")
    inputEgo.write("")
    inputEgo.write("")
    inputEgo.write("")
    inputOvclock.write("오버클록")
    eOutput.write("")
    eOutput.write("")
    eOutput.write("")

    Sinners = [i for i in [sinner1,sinner2,sinner3,sinner4,sinner5,sinner6] if i != None]

    Sinner1 = eInputSinners.selectbox("e수감자1", Sinners, index=st.session_state["set_sinners2"][0], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner2 = eInputSinners.selectbox("e수감자2", Sinners, index=st.session_state["set_sinners2"][1], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner3 = eInputSinners.selectbox("e수감자3", Sinners, index=st.session_state["set_sinners2"][2], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner4 = eInputSinners.selectbox("e수감자4", Sinners, index=st.session_state["set_sinners2"][3], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner5 = eInputSinners.selectbox("e수감자5", Sinners, index=st.session_state["set_sinners2"][4], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner6 = eInputSinners.selectbox("e수감자6", Sinners, index=st.session_state["set_sinners2"][5], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner7 = eInputSinners.selectbox("e수감자7", Sinners, index=st.session_state["set_sinners2"][6], placeholder="수감자 선택", label_visibility="collapsed")

    try:
        st.session_state["set_sinners2"][0] = Sinners.index(Sinner1)
    except ValueError:
        st.session_state["set_sinners2"][0] = None
    try:
        st.session_state["set_sinners2"][1] = Sinners.index(Sinner2)
    except ValueError:
        st.session_state["set_sinners2"][1] = None
    try:
        st.session_state["set_sinners2"][2] = Sinners.index(Sinner3)
    except ValueError:
        st.session_state["set_sinners2"][2] = None
    try:
        st.session_state["set_sinners2"][3] = Sinners.index(Sinner4)
    except ValueError:
        st.session_state["set_sinners2"][3] = None
    try:
        st.session_state["set_sinners2"][4] = Sinners.index(Sinner5)
    except ValueError:
        st.session_state["set_sinners2"][4] = None
    try:
        st.session_state["set_sinners2"][5] = Sinners.index(Sinner6)
    except ValueError:
        st.session_state["set_sinners2"][5] = None
    try:
        st.session_state["set_sinners2"][6] = Sinners.index(Sinner7)
    except ValueError:
        st.session_state["set_sinners2"][6] = None
    
    tempE = [Sinner1,Sinner2,Sinner3,Sinner4,Sinner5,Sinner6,Sinner7]



    try:
        st.session_state["set_ego"][0] = egoList[Sinner1].index(inputEgo.selectbox("에고1", egoList[Sinner1], index=st.session_state["set_ego"][0], placeholder="에고 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_ego"][0] = None
    try:
        st.session_state["set_ego"][1] = egoList[Sinner2].index(inputEgo.selectbox("에고2", egoList[Sinner2], index=st.session_state["set_ego"][1], placeholder="에고 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_ego"][1] = None
    try:
        st.session_state["set_ego"][2] = egoList[Sinner3].index(inputEgo.selectbox("에고3", egoList[Sinner3], index=st.session_state["set_ego"][2], placeholder="에고 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_ego"][2] = None
    try:
        st.session_state["set_ego"][3] = egoList[Sinner4].index(inputEgo.selectbox("에고4", egoList[Sinner4], index=st.session_state["set_ego"][3], placeholder="에고 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_ego"][3] = None
    try:
        st.session_state["set_ego"][4] = egoList[Sinner5].index(inputEgo.selectbox("에고5", egoList[Sinner5], index=st.session_state["set_ego"][4], placeholder="에고 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_ego"][4] = None
    try:
        st.session_state["set_ego"][5] = egoList[Sinner6].index(inputEgo.selectbox("에고6", egoList[Sinner6], index=st.session_state["set_ego"][5], placeholder="에고 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_ego"][5] = None
    try:
        st.session_state["set_ego"][6] = egoList[Sinner7].index(inputEgo.selectbox("에고7", egoList[Sinner7], index=st.session_state["set_ego"][6], placeholder="에고 선택", label_visibility="collapsed"))
    except ValueError:
        st.session_state["set_ego"][6] = None

    st.session_state["ovclock"][0] = inputOvclock.container(height=40,border=False).toggle("오버클록1", st.session_state["ovclock"][0], label_visibility='collapsed')
    st.session_state["ovclock"][1] = inputOvclock.container(height=40,border=False).toggle("오버클록2", st.session_state["ovclock"][1], label_visibility='collapsed')
    st.session_state["ovclock"][2] = inputOvclock.container(height=40,border=False).toggle("오버클록3", st.session_state["ovclock"][2], label_visibility='collapsed')
    st.session_state["ovclock"][3] = inputOvclock.container(height=40,border=False).toggle("오버클록4", st.session_state["ovclock"][3], label_visibility='collapsed')
    st.session_state["ovclock"][4] = inputOvclock.container(height=40,border=False).toggle("오버클록5", st.session_state["ovclock"][4], label_visibility='collapsed')
    st.session_state["ovclock"][5] = inputOvclock.container(height=40,border=False).toggle("오버클록6", st.session_state["ovclock"][5], label_visibility='collapsed')
    st.session_state["ovclock"][6] = inputOvclock.container(height=40,border=False).toggle("오버클록7", st.session_state["ovclock"][6], label_visibility='collapsed')
    
    Col = ["cost_wrath",
           'cost_lust',
           'cost_sloth',
           'cost_gluttony',
           'cost_gloom',
           'cost_pride',
           "cost_envy",

           "ovclockcost_wrath",
           "ovclockcost_lust",
           "ovclockcost_sloth",
           "ovclockcost_gluttony",
           "ovclockcost_gloom",
           "ovclockcost_pride",
           "ovclockcost_envy"
           ]
    
    sinCost = pd.DataFrame({"cost_wrath":[],
                                 'cost_lust':[],
                                 'cost_sloth':[],
                                 'cost_gluttony':[],
                                 'cost_gloom':[],
                                 'cost_pride':[],
                                 "cost_envy":[]
                                 })
    
    egoNum = [0,0,0,0,0,0]
    for i in range(7):
        try:
            egoNum[i] = int(li.loc[(li["sinner"] == tempE[i]) & (li["ego"] == egoList[tempE[i]][st.session_state["set_ego"][i]]), "id"])
        except TypeError:
            continue
    
    makerEgo = ego.loc[[i for i in egoNum if i > 0]]

    for i in range(makerEgo.shape[0]):
        if st.session_state["ovclock"][i]:
            sinCost.loc[i] = list((makerEgo.iloc[i])[["ovclockcost_wrath",
                                                           "ovclockcost_lust",
                                                           "ovclockcost_sloth",
                                                           "ovclockcost_gluttony",
                                                           "ovclockcost_gloom",
                                                           "ovclockcost_pride",
                                                           "ovclockcost_envy"
                                                           ]])
        else:
            sinCost.loc[i] = list((makerEgo.iloc[i])[["cost_wrath",
                                                           'cost_lust',
                                                           'cost_sloth',
                                                           'cost_gluttony',
                                                           'cost_gloom',
                                                           'cost_pride',
                                                           "cost_envy"
                                                           ]])
    
    if not makerEgo[Col].empty:
        show_sinCost = sinCost.style.apply(color_sin_bg).apply(lambda x:
                                                                     ['color: black' if not pd.isna(i) else "" for i in x])\
                                                                        .applymap(color_sin_char_zero).format(real_format)
    else:
        show_sinCost = sinCost

    eOutput.dataframe(show_sinCost,
                      hide_index=True,
                      width=380, height=283,
                      column_config={"cost_wrath":"분노",
                                     'cost_lust':"색욕",
                                     'cost_sloth':"나태",
                                     'cost_gluttony':"탐식",
                                     'cost_gloom':"우울",
                                     'cost_pride':"오만",
                                     "cost_envy":"질투",
                                     })
    Total = sinCost.sum()
    eOutput.markdown(f'''<table border="1" width="380">
  <thead>
    <tr>
      <th style="background-color: #ea9999; color: black; text-align: center;">-{real_format(Total[0])}</th>
      <th style="background-color: #f9cb9c; color: black; text-align: center;">-{real_format(Total[1])}</th>
      <th style="background-color: #ffe599; color: black; text-align: center;">-{real_format(Total[2])}</th>
      <th style="background-color: #b6d7a8; color: black; text-align: center;">-{real_format(Total[3])}</th>
      <th style="background-color: #a2c4c9; color: black; text-align: center;">-{real_format(Total[4])}</th>
      <th style="background-color: #a4c2f4; color: black; text-align: center;">-{real_format(Total[5])}</th>
      <th style="background-color: #b4a7d6; color: black; text-align: center;">-{real_format(Total[6])}</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background-color: #f4cccc; color: black; text-align: center;">{real_format(total[0] - int(Total[0]))}</td>
      <td style="background-color: #fce5cd; color: black; text-align: center;">{real_format(total[1] - int(Total[1]))}</td>
      <td style="background-color: #fff2cc; color: black; text-align: center;">{real_format(total[2] - int(Total[2]))}</td>
      <td style="background-color: #d9ead3; color: black; text-align: center;">{real_format(total[3] - int(Total[3]))}</td>
      <td style="background-color: #d0e0e3; color: black; text-align: center;">{real_format(total[4] - int(Total[4]))}</td>
      <td style="background-color: #c9daf8; color: black; text-align: center;">{real_format(total[5] - int(Total[5]))}</td>
      <td style="background-color: #d9d2e9; color: black; text-align: center;">{real_format(total[6] - int(Total[6]))}</td>
    </tr>
  </tbody>
</table>
''', unsafe_allow_html=True)

with st.expander("스탯 / 전투 패시브"):
    stat, battlepassive = st.columns(2)
    stat.dataframe(makerId.style.applymap(color_sin_char).format({'hp':real_format,'atkLv_mean':real_format}),
                   use_container_width=True,
                   hide_index=True,
                   column_order=['identity','min_speed','max_speed','hp','atkLv_mean','defLv','battlePassive_sin','battlePassive_sinCnt','battlePassive_type'],
                   column_config={
                       'sinner': st.column_config.Column("수감자", width="small"),
                       'identity': st.column_config.Column("인격", width="medium"),
                       'min_speed': "최소 속도",
                       'max_speed': "최대 속도",
                       'speed_mean': '평균 속도',
                       'hp': '최대 체력',
                       'atkLv_mean': st.column_config.Column('공격 레벨', help="평균값"),
                       'defLv': '방어 레벨',
                       'battlePassive_sin': st.column_config.TextColumn('자원'),
                       'battlePassive_sinCnt': st.column_config.TextColumn('필요량'),
                       'battlePassive_type': st.column_config.TextColumn('종류')
                   }
                   )
    battlepassive.dataframe(makerId['battlePassive'],
                            use_container_width=True,
                            hide_index=True,
                            column_config={
                                'battlePassive': '전투 패시브'
                            })



with st.expander("서포트 패시브"):
    # Ssinners = [i in Sinners for i in ["이상","파우스트","돈키호테","료슈","뫼르소","홍루","히스클리프","이스마엘","로쟈","싱클레어","오티스","그레고르"]]
    supporter, supportpassive = st.columns(2)
    supSinner, supId = supporter.columns(2)

    Ssinners = []

    if '이상' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자1", ['이상'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][0] = idList['이상'].index(supId.selectbox("서포트1", idList['이상'], index=st.session_state["set_sup"][0], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][0] = None
    if '파우스트' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자2", ['파우스트'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][1] = idList['파우스트'].index(supId.selectbox("서포트2", idList['파우스트'], index=st.session_state["set_sup"][1], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][1] = None
    if '돈키호테' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자3", ['돈키호테'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][2] = idList['돈키호테'].index(supId.selectbox("서포트3", idList['돈키호테'], index=st.session_state["set_sup"][2], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][2] = None
    if '료슈' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자4", ['료슈'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][3] = idList['료슈'].index(supId.selectbox("서포트4", idList['료슈'], index=st.session_state["set_sup"][3], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][3] = None
    if '뫼르소' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자5", ['뫼르소'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][4] = idList['뫼르소'].index(supId.selectbox("서포트5", idList['뫼르소'], index=st.session_state["set_sup"][4], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][4] = None
    if '홍루' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자6", ['홍루'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][5] = idList['홍루'].index(supId.selectbox("서포트6", idList['홍루'], index=st.session_state["set_sup"][5], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][5] = None
    if '히스클리프' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자7", ['히스클리프'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][6] = idList['히스클리프'].index(supId.selectbox("서포트7", idList['히스클리프'], index=st.session_state["set_sup"][6], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][6] = None
    if '이스마엘' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자8", ['이스마엘'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][7] = idList['이스마엘'].index(supId.selectbox("서포트8", idList['이스마엘'], index=st.session_state["set_sup"][7], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][7] = None
    if '로쟈' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자9", ['로쟈'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][8] = idList['로쟈'].index(supId.selectbox("서포트9", idList['로쟈'], index=st.session_state["set_sup"][8], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][8] = None
    if '싱클레어' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자10", ['싱클레어'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][9] = idList['싱클레어'].index(supId.selectbox("서포트10", idList['싱클레어'], index=st.session_state["set_sup"][9], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][9] = None
    if '오티스' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자11", ['오티스'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][10] = idList['오티스'].index(supId.selectbox("서포트11", idList['오티스'], index=st.session_state["set_sup"][10], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][10] = None
    if '그레고르' not in Sinners:
        Ssinners.append(supSinner.selectbox("s수감자12", ['그레고르'], index=0, label_visibility="collapsed"))
        try:
            st.session_state["set_sup"][11] = idList['그레고르'].index(supId.selectbox("서포트12", idList['그레고르'], index=st.session_state["set_sup"][11], placeholder="인격 선택", label_visibility="collapsed"))
        except ValueError:
            st.session_state["set_sup"][11] = None
    
    supNum = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(12):
        try:
            supNum[i] = int(li.loc[(li["sinner"] == sinners[i]) & (li["identity"] == idList[sinners[i]][st.session_state["set_sup"][i]]), "id"])
        except TypeError:
            continue
    
    makerSup = Id.loc[[i for i in supNum if i > 0]]
    supportpassive.dataframe(makerSup.style.applymap(color_sin_char),
                             use_container_width=True, height=457,
                             hide_index=True,
                             column_order=['supportPassive_sin','supportPassive_sinCnt','supportPassive_type','supportPassive'],
                             column_config={
                                 'supportPassive_sin': '자원',
                                 'supportPassive_sinCnt': '필요량',
                                 'supportPassive_type': '종류',
                                 'supportPassive': '서포트 패시브'
                             })