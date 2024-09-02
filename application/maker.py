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

Id = st.session_state["id"]
ego = st.session_state["ego"]
li = st.session_state["list"]

st.header("파티 구성")
st.write(" \n ")

setting = st.radio("죄악 자원 설정",
                   ["기본",'단기전'],
                   index=0,
                   captions=['스토리/거울굴절철도','거울 던전'],
                   help="'단기전' 옵션은 1~3턴 이내로 전투가 끝나는 경우에 맞춰 설정되었습니다.",
                   )

Input, Output = st.columns(2)
inputSinners, inputId = Input.columns(2)

with Input:
    sinners = ["수감자 선택", "이상", "파우스트", "돈키호테", "료슈", "뫼르소", "홍루",
               "히스클리프", "이스마엘", "로쟈", "싱클레어", "오티스", "그레고르"]

    sinner1 = inputSinners.selectbox("수감자1", sinners, index=st.session_state["set_sinners1"][0], placeholder="수감자 선택", label_visibility="collapsed")
    sinner2 = inputSinners.selectbox("수감자2", sinners, index=st.session_state["set_sinners1"][1], placeholder="수감자 선택", label_visibility="collapsed")
    sinner3 = inputSinners.selectbox("수감자3", sinners, index=st.session_state["set_sinners1"][2], placeholder="수감자 선택", label_visibility="collapsed")
    sinner4 = inputSinners.selectbox("수감자4", sinners, index=st.session_state["set_sinners1"][3], placeholder="수감자 선택", label_visibility="collapsed")
    sinner5 = inputSinners.selectbox("수감자5", sinners, index=st.session_state["set_sinners1"][4], placeholder="수감자 선택", label_visibility="collapsed")
    sinner6 = inputSinners.selectbox("수감자6", sinners, index=st.session_state["set_sinners1"][5], placeholder="수감자 선택", label_visibility="collapsed")

    st.session_state["set_sinners1"] = [sinners.index(sinner1),
                                        sinners.index(sinner2),
                                        sinners.index(sinner3),
                                        sinners.index(sinner4),
                                        sinners.index(sinner5),
                                        sinners.index(sinner6)
                                        ]

    id1,id2,id3,id4,id5,id6 = "","","","","",""
    idList1,idList2,idList3,idList4,idList5,idList6 = Id.loc[(Id["sinner"] == sinner1),"identity"],\
                                                      Id.loc[(Id["sinner"] == sinner2),"identity"],\
                                                      Id.loc[(Id["sinner"] == sinner3),"identity"],\
                                                      Id.loc[(Id["sinner"] == sinner4),"identity"],\
                                                      Id.loc[(Id["sinner"] == sinner5),"identity"],\
                                                      Id.loc[(Id["sinner"] == sinner6),"identity"]

    try: id1 = Id.loc[(Id["sinner"] == sinner1) & (Id["identity"] == inputId.selectbox("인격1", idList1, index=st.session_state["set_id"][0], placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id2 = Id.loc[(Id["sinner"] == sinner2) & (Id["identity"] == inputId.selectbox("인격2", idList2, index=st.session_state["set_id"][1], placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id3 = Id.loc[(Id["sinner"] == sinner3) & (Id["identity"] == inputId.selectbox("인격3", idList3, index=st.session_state["set_id"][2], placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id4 = Id.loc[(Id["sinner"] == sinner4) & (Id["identity"] == inputId.selectbox("인격4", idList4, index=st.session_state["set_id"][3], placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id5 = Id.loc[(Id["sinner"] == sinner5) & (Id["identity"] == inputId.selectbox("인격5", idList5, index=st.session_state["set_id"][4], placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id6 = Id.loc[(Id["sinner"] == sinner6) & (Id["identity"] == inputId.selectbox("인격6", idList6, index=st.session_state["set_id"][5], placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass

    try:
        st.session_state["set_id"] = [list(idList1).index(id1),
                                      list(idList2).index(id2),
                                      list(idList3).index(id3),
                                      list(idList4).index(id4),
                                      list(idList5).index(id5),
                                      list(idList6).index(id6)
                                      ]
    except ValueError: pass

temp = [sinner1,sinner2,sinner3,sinner4,sinner5,sinner6]
try: temp.remove('수감자 선택')
except Exception: pass

if has_duplicates():
    Input.error("중복된 수감자가 있습니다.")

with Output:
    makerId = Id.loc[[i for i in [id1,id2,id3,id4,id5,id6] if i != ""]]

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
                                                                   ['color: black' if not pd.isna(i) else "" for i in x]).format(real_format)
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
    Output.markdown(f'''<table border="1">
  <thead>
    <tr>
      <th style="background-color: #ea9999; color: black;">{real_format(total[0])}</th>
      <th style="background-color: #f9cb9c; color: black;">{real_format(total[1])}</th>
      <th style="background-color: #ffe599; color: black;">{real_format(total[2])}</th>
      <th style="background-color: #b6d7a8; color: black;">{real_format(total[3])}</th>
      <th style="background-color: #a2c4c9; color: black;">{real_format(total[4])}</th>
      <th style="background-color: #a4c2f4; color: black;">{real_format(total[5])}</th>
      <th style="background-color: #b4a7d6; color: black;">{real_format(total[6])}</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background-color: #f4cccc; color: black;">(+{makerId['def_sin'].value_counts().get('분노', 0)})</td>
      <td style="background-color: #fce5cd; color: black;">(+{makerId['def_sin'].value_counts().get('색욕', 0)})</td>
      <td style="background-color: #fff2cc; color: black;">(+{makerId['def_sin'].value_counts().get('나태', 0)})</td>
      <td style="background-color: #d9ead3; color: black;">(+{makerId['def_sin'].value_counts().get('탐식', 0)})</td>
      <td style="background-color: #d0e0e3; color: black;">(+{makerId['def_sin'].value_counts().get('우울', 0)})</td>
      <td style="background-color: #c9daf8; color: black;">(+{makerId['def_sin'].value_counts().get('오만', 0)})</td>
      <td style="background-color: #d9d2e9; color: black;">(+{makerId['def_sin'].value_counts().get('질투', 0)})</td>
    </tr>
  </tbody>
</table>
''', unsafe_allow_html=True)

with st.expander("주요 E.G.O"):
    eInput, eOutput = st.columns(2)
    eInputSinners, inputEgo, inputOvclock = eInput.columns(3)

    Sinners = [i if i != None else "" for i in [sinner1,sinner2,sinner3,sinner4,sinner5,sinner6]]
    Sinners.insert(0, "수감자 선택")

    Sinner1 = eInputSinners.selectbox("e수감자1", Sinners, index=st.session_state["set_sinners2"][0], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner2 = eInputSinners.selectbox("e수감자2", Sinners, index=st.session_state["set_sinners2"][1], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner3 = eInputSinners.selectbox("e수감자3", Sinners, index=st.session_state["set_sinners2"][2], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner4 = eInputSinners.selectbox("e수감자4", Sinners, index=st.session_state["set_sinners2"][3], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner5 = eInputSinners.selectbox("e수감자5", Sinners, index=st.session_state["set_sinners2"][4], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner6 = eInputSinners.selectbox("e수감자6", Sinners, index=st.session_state["set_sinners2"][5], placeholder="수감자 선택", label_visibility="collapsed")
    Sinner7 = eInputSinners.selectbox("e수감자7", Sinners, index=st.session_state["set_sinners2"][6], placeholder="수감자 선택", label_visibility="collapsed")

    st.session_state["set_sinners2"] = [Sinners.index(Sinner1),
                                        Sinners.index(Sinner2),
                                        Sinners.index(Sinner3),
                                        Sinners.index(Sinner4),
                                        Sinners.index(Sinner5),
                                        Sinners.index(Sinner6),
                                        Sinners.index(Sinner7)]

    ego1,ego2,ego3,ego4,ego5,ego6,ego7 = "","","","","","",""
    egoList1,egoList2,egoList3,egoList4,egoList5,egoList6,egoList7 = ego.loc[(ego["sinner"] == Sinner1),"ego"],\
                                                                     ego.loc[(ego["sinner"] == Sinner2),"ego"],\
                                                                     ego.loc[(ego["sinner"] == Sinner3),"ego"],\
                                                                     ego.loc[(ego["sinner"] == Sinner4),"ego"],\
                                                                     ego.loc[(ego["sinner"] == Sinner5),"ego"],\
                                                                     ego.loc[(ego["sinner"] == Sinner6),"ego"],\
                                                                     ego.loc[(ego["sinner"] == Sinner7),"ego"]

    try: ego1 = ego.loc[(ego["sinner"] == Sinner1) & (ego["ego"] == inputEgo.selectbox("에고1", egoList1, index=st.session_state["set_ego"][0], placeholder="에고 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: ego2 = ego.loc[(ego["sinner"] == Sinner2) & (ego["ego"] == inputEgo.selectbox("에고2", egoList2, index=st.session_state["set_ego"][1], placeholder="에고 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: ego3 = ego.loc[(ego["sinner"] == Sinner3) & (ego["ego"] == inputEgo.selectbox("에고3", egoList3, index=st.session_state["set_ego"][2], placeholder="에고 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: ego4 = ego.loc[(ego["sinner"] == Sinner4) & (ego["ego"] == inputEgo.selectbox("에고4", egoList4, index=st.session_state["set_ego"][3], placeholder="에고 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: ego5 = ego.loc[(ego["sinner"] == Sinner5) & (ego["ego"] == inputEgo.selectbox("에고5", egoList5, index=st.session_state["set_ego"][4], placeholder="에고 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: ego6 = ego.loc[(ego["sinner"] == Sinner6) & (ego["ego"] == inputEgo.selectbox("에고6", egoList6, index=st.session_state["set_ego"][5], placeholder="에고 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: ego7 = ego.loc[(ego["sinner"] == Sinner7) & (ego["ego"] == inputEgo.selectbox("에고7", egoList7, index=st.session_state["set_ego"][6], placeholder="에고 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass

    try:
        st.session_state["set_ego"] = [list(egoList1).index(ego1),
                                       list(egoList2).index(ego2),
                                       list(egoList3).index(ego3),
                                       list(egoList4).index(ego4),
                                       list(egoList5).index(ego5),
                                       list(egoList6).index(ego6),
                                       list(egoList7).index(ego7)
                                       ]
    except ValueError: pass

    inputOvclock.write("")
    ovclock1 = inputOvclock.checkbox("오버클록", st.session_state["ovclock"][0], label_visibility='visible')
    ovclock2 = inputOvclock.checkbox("오버클록2", st.session_state["ovclock"][1], label_visibility='collapsed')
    inputOvclock.write("")
    inputOvclock.write("")
    ovclock3 = inputOvclock.checkbox("오버클록3", st.session_state["ovclock"][2], label_visibility='collapsed')
    ovclock4 = inputOvclock.checkbox("오버클록4", st.session_state["ovclock"][3], label_visibility='collapsed')
    inputOvclock.write("")
    inputOvclock.write("")
    ovclock5 = inputOvclock.checkbox("오버클록5", st.session_state["ovclock"][4], label_visibility='collapsed')
    ovclock6 = inputOvclock.checkbox("오버클록6", st.session_state["ovclock"][5], label_visibility='collapsed')
    inputOvclock.write("")
    ovclock7 = inputOvclock.checkbox("오버클록7", st.session_state["ovclock"][6], label_visibility='collapsed')

    st.session_state["ovclock"] = [ovclock1,ovclock2,ovclock3,ovclock4,ovclock5,ovclock6,ovclock7]
    
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
    
    makerEgo = ego.loc[[i for i in [ego1,ego2,ego3,ego4,ego5,ego6,ego7] if i != ""]]
    for i in range(makerEgo.shape[0]):
        if [ovclock1,ovclock2,ovclock3,ovclock4,
            ovclock5,ovclock6,ovclock7][i]:
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
                                                                     ['color: black' if not pd.isna(i) else "" for i in x])#.format(real_format)
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
    eOutput.markdown(f'''<table border="1">
  <thead>
    <tr>
      <th style="background-color: #ea9999; color: black;">-{Total[0]}</th>
      <th style="background-color: #f9cb9c; color: black;">-{Total[1]}</th>
      <th style="background-color: #ffe599; color: black;">-{Total[2]}</th>
      <th style="background-color: #b6d7a8; color: black;">-{Total[3]}</th>
      <th style="background-color: #a2c4c9; color: black;">-{Total[4]}</th>
      <th style="background-color: #a4c2f4; color: black;">-{Total[5]}</th>
      <th style="background-color: #b4a7d6; color: black;">-{Total[6]}</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background-color: #f4cccc; color: black;">{total[0] - int(Total[0]):.0f}</td>
      <td style="background-color: #fce5cd; color: black;">{total[1] - int(Total[1]):.0f}</td>
      <td style="background-color: #fff2cc; color: black;">{total[2] - int(Total[2]):.0f}</td>
      <td style="background-color: #d9ead3; color: black;">{total[3] - int(Total[3]):.0f}</td>
      <td style="background-color: #d0e0e3; color: black;">{total[4] - int(Total[4]):.0f}</td>
      <td style="background-color: #c9daf8; color: black;">{total[5] - int(Total[5]):.0f}</td>
      <td style="background-color: #d9d2e9; color: black;">{total[6] - int(Total[6]):.0f}</td>
    </tr>
  </tbody>
</table>
''', unsafe_allow_html=True)