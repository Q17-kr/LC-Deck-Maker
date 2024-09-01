import streamlit as st
from application import baseDef as bd

def color_sin_bg(val):
    color = {
        "cost_wrath": 'background-color: #f4cccc',
        "cost_lust": 'background-color: #fce5cd',
        "cost_sloth": 'background-color: #fff2cc',
        "cost_gluttony": 'background-color: #d9ead3',
        "cost_gloom": 'background-color: #d0e0e3',
        "cost_pride": 'background-color: #c9daf8',
        "cost_envy": 'background-color: #d9d2e9'
        }
    
    return [color.get(val.name, "") if i != "0" else "" for i in val]

def color_sin_char(val):
    color = {
        "취약": 'color: red',
        "내성": 'color: gray',
        "견딤": 'color: #4472c4',
        "0": 'color: white',
        0: 'color: white'
        }
    
    return color.get(val, "")

bd.make_egoList()

ego = st.session_state["ego"].copy()

ego = ego.style.applymap(color_sin_char).apply(color_sin_bg)

colums = ['sinner','ego',
          'grade',
          'resist_wrath','resist_lust','resist_sloth','resist_gluttony','resist_gloom','resist_pride','resist_envy',
          'cost_wrath','cost_lust','cost_sloth','cost_gluttony','cost_gloom','cost_pride','cost_envy',
          'atkWeight_slash','atkWeight_pierce','atkWeight_blunt',
          'atkWeight_slash_ovclock','atkWeight_pierce_ovclock','atkWeight_blunt_ovclock',
          'passive'
          ]

with st.expander("열 선택"):
    info, keywords = st.columns(2)

    with info:
        info.write("")
        if not info.checkbox("등급", True):
            colums.remove("grade")
        if not info.checkbox("죄악 내성", False):
            colums.remove('resist_wrath')
            colums.remove('resist_lust')
            colums.remove('resist_sloth')
            colums.remove('resist_gluttony')
            colums.remove('resist_gloom')
            colums.remove('resist_pride')
            colums.remove('resist_envy')
        if not info.checkbox("소모 자원", True):
            colums.remove('cost_wrath')
            colums.remove('cost_lust')
            colums.remove('cost_sloth')
            colums.remove('cost_gluttony')
            colums.remove('cost_gloom')
            colums.remove('cost_pride')
            colums.remove('cost_envy')
        info.markdown('''---''')
        info.write("공격 가중치")
        if not info.checkbox("각성 스킬", True, key='atkWeightN'):
            colums.remove('atkWeight_slash')
            colums.remove('atkWeight_pierce')
            colums.remove('atkWeight_blunt')
        if not info.checkbox("침식 스킬", False):
            colums.remove('atkWeight_slash_ovclock')
            colums.remove('atkWeight_pierce_ovclock')
            colums.remove('atkWeight_blunt_ovclock')
        info.markdown('---')
        if not info.checkbox("패시브", True, key='atkWeightC'):
            colums.remove("passive")
        info.write("")

    with keywords:
        keywords.write("키워드")

        nomal, ovclock = keywords.columns(2)
        if nomal.checkbox("각성 스킬", True, key='keywordsN'):
            pass
        if ovclock.checkbox("침식 스킬", False, key='keywordsC'):
            pass

        if not keywords.checkbox("화상", True):
            colums.remove("passive")
        info.write("")

with st.expander("검색"):
    searchList = {"수감자":'sinner',
                  'E.G.O':'ego',
                  '패시브':'passive'
                  }
    col, txt = st.columns(2)
    search = col.radio("검색할 열 선택",
                      ["수감자", 'E.G.O', '패시브'])
    searchTxT = txt.text_input("검색어",
                               value="")
    if txt.button("초기화"):
        search = "수감자"
        searchTxT = ""
    if searchTxT != "":
        ego = ego.loc[ego[searchList[search]].str.find(searchTxT) >= 0]

st.dataframe(ego, use_container_width=True,
             height=500,
             hide_index=True,
             column_order=colums,
             column_config={'sinner': st.column_config.Column("수감자", width="small"),
                            'ego': st.column_config.Column("E.G.O", width="medium"),
                            'grade': "등급",
                            'resist_wrath': '분노 내성',
                            'resist_lust': '색욕 내성',
                            'resist_sloth': '나태 내성',
                            'resist_gluttony': '탐식 내성',
                            'resist_gloom': '우울 내성',
                            'resist_pride': '오만 내성',
                            'resist_envy': '질투 내성',
                            'cost_wrath': '분노',
                            'cost_lust': '색욕',
                            'cost_sloth': '나태',
                            'cost_gluttony': '탐식',
                            'cost_gloom': '우울',
                            'cost_pride': '오만',
                            'cost_envy': '질투',
                            'atkWeight_slash': st.column_config.Column('각성_참격', help="공격 가중치"),
                            'atkWeight_pierce': st.column_config.Column('각성_관통', help="공격 가중치"),
                            'atkWeight_blunt': st.column_config.Column('각성_타격', help="공격 가중치"),
                            'atkWeight_slash_ovclock': st.column_config.Column('침식_참격', help="공격 가중치"),
                            'atkWeight_pierce_ovclock': st.column_config.Column('침식_관통', help="공격 가중치"),
                            'atkWeight_blunt_ovclock': st.column_config.Column('침식_타격', help="공격 가중치"),
                            'passive': '패시브'
                            }
             )