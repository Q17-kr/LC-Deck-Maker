import streamlit as st
from application import baseDef as bd

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
        }
    
    return [color.get(val.name, "") if i != 0 else "" for i in val]

def real_format(value):
    if isinstance(value, int):
        return value
    else:
        return f"{value:.1f}"

bd.start_data()

st.title("림버스 컴퍼니 파티메이커")
st.write(" \n ")
st.write(" \n ")

st.sidebar.markdown("## Limbus Company Deck Maker")

bd.make_idList()

Id = st.session_state["id"].copy()
Id['speed_mean'] = (Id['min_speed'] + Id['max_speed']) / 2
Id['def_sin'] = Id['def_sin'].replace('0', "")
Id['etc'] = Id['etc'].replace('0', "")

Id = Id.style.applymap(color_sin_char)\
    .apply(color_sin_bg)\
        .format({'speed_mean':real_format,
                 'hp':'{:.0f}',
                 'atkLv_mean':real_format,
                 'simpSinCnt_wrath':real_format,
                 'simpSinCnt_lust':real_format,
                 'simpSinCnt_sloth':real_format,
                 'simpSinCnt_gluttony':real_format,
                 'simpSinCnt_gloom':real_format,
                 'simpSinCnt_pride':real_format,
                 'simpSinCnt_envy':real_format,
                 'sinCnt_wrath':real_format,
                 'sinCnt_lust':real_format,
                 'sinCnt_sloth':real_format,
                 'sinCnt_gluttony':real_format,
                 'sinCnt_gloom':real_format,
                 'sinCnt_pride':real_format,
                 'sinCnt_envy':real_format
                 })

colums = ['sinner','identity',
          'grade',
          'min_speed', 'max_speed','speed_mean',
          'hp',
          'atkLv_mean','defLv',
          'slash_coinCnt','pierce_coinCnt','blunt_coinCnt',
          'def_type','def_sin',
          'simpSinCnt_wrath','simpSinCnt_lust','simpSinCnt_sloth','simpSinCnt_gluttony','simpSinCnt_gloom','simpSinCnt_pride','simpSinCnt_envy',
          'sinCnt_wrath','sinCnt_lust','sinCnt_sloth','sinCnt_gluttony','sinCnt_gloom','sinCnt_pride','sinCnt_envy',
          'resist_slash','resist_pierce','resist_blunt',
          'battlePassive_sin','battlePassive_sinCnt','battlePassive_type','battlePassive',
          'supportPassive_sin','supportPassive_sinCnt','supportPassive_type','supportPassive',
          'etc'
          ]

with st.expander("열 선택"):
    info, keywords, etc = st.columns(3)

    with info:
        info.write("")
        if not info.checkbox("등급", True):
            colums.remove("grade")
        if not info.checkbox("체력", True):
            colums.remove("hp")
        if not info.checkbox("공격 레벨", False):
            colums.remove("atkLv_mean")
        if not info.checkbox("방어 레벨", False):
            colums.remove("defLv")
        info.markdown('''---''')
        info.write("속도")
        if not info.checkbox("최솟값", False):
            colums.remove("min_speed")
        if not info.checkbox("최댓값", False):
            colums.remove("max_speed")
        if not info.checkbox("평균값", True):
            colums.remove("speed_mean")
        info.markdown('---')
        info.write("코인 개수")
        if not info.checkbox("참격", True, key="coinS"):
            colums.remove("resist_slash")
        if not info.checkbox("관통", True, key="coinP"):
            colums.remove("resist_pierce")
        if not info.checkbox("타격", True, key="coinB"):
            colums.remove("resist_blunt")
        info.markdown('---')
        if not info.checkbox("수비스킬", True):
            colums.remove("def_type")
            colums.remove("def_sin")
        info.write("")

    with keywords:
        keywords.write("키워드")
        if not keywords.checkbox("화상", True):
            colums.remove("")
        info.write("")

    with etc:
        etc.write("죄악 자원 수집")
        if etc.radio("죄악 자원 수집",
                     ["기본",'단기전'],
                     index=0,
                     captions=['스토리/거울굴절철도','거울 던전'],
                     help="'단기전' 옵션은 1~3턴 이내로 전투가 끝나는 경우에 맞춰 설정되었습니다.",
                     label_visibility='collapsed'
                     ) == "기본":
            colums.remove("simpSinCnt_wrath")
            colums.remove("simpSinCnt_lust")
            colums.remove("simpSinCnt_sloth")
            colums.remove("simpSinCnt_gluttony")
            colums.remove("simpSinCnt_gloom")
            colums.remove("simpSinCnt_pride")
            colums.remove("simpSinCnt_envy")
        else:
            colums.remove("sinCnt_wrath")
            colums.remove("sinCnt_lust")
            colums.remove("sinCnt_sloth")
            colums.remove("sinCnt_gluttony")
            colums.remove("sinCnt_gloom")
            colums.remove("sinCnt_pride")
            colums.remove("sinCnt_envy")
        etc.markdown('''---''')
        etc.write("내성 정보")
        if not etc.checkbox("참격", True):
            colums.remove("resist_slash")
        if not etc.checkbox("관통", True):
            colums.remove("resist_pierce")
        if not etc.checkbox("타격", True):
            colums.remove("resist_blunt")
        etc.markdown('''---''')
        if not etc.checkbox("전투 패시브", True):
            colums.remove('battlePassive_sin')
            colums.remove('battlePassive_sinCnt')
            colums.remove('battlePassive_type')
            colums.remove('battlePassive')
        if not etc.checkbox("서포트 패시브", True):
            colums.remove("supportPassive_sin")
            colums.remove('supportPassive_sinCnt')
            colums.remove('supportPassive_type')
            colums.remove('supportPassive')
        if not etc.checkbox("특이사항", False):
            colums.remove("etc")
        info.write("")

with st.expander("검색"):
    searchList = {"수감자":'sinner',
                  '인격':'identity',
                  "수비 스킬 자원":'def_sin',
                  '전투 패시브 자원':'battlePassive_sin',
                  '전투 패시브':'battlePassive',
                  '서포트 패시브 자원':'supportPassive_sin',
                  '서포트 패시브':'supportPassive'
                  }
    col, txt = st.columns(2)
    search = col.radio("검색할 열 선택",
                      ["수감자",
                       '인격',
                       "수비 스킬 자원",
                       '전투 패시브',
                       '전투 패시브 자원',
                       '서포트 패시브',
                       '서포트 패시브 자원'
                       ])
    searchTxT = txt.text_input("검색어",
                               value="")
    if txt.button("초기화"):
        search = "수감자"
        searchTxT = ""
    if searchTxT != "":
        Id = Id.loc[Id[searchList[search]].str.find(searchTxT) >= 0]

st.dataframe(Id, use_container_width=True,
             hide_index=True,
             column_order=colums,
             column_config={'sinner': st.column_config.Column("수감자", width="small"),
                            'identity': st.column_config.Column("인격", width="medium"),
                            'grade': "등급",
                            'min_speed': "최소 속도",
                            'max_speed': "최대 속도",
                            'speed_mean': '평균 속도',
                            'hp': '최대 체력',
                            'atkLv_mean': st.column_config.Column('공격 레벨', help="평균값"),
                            'defLv': '방어 레벨',
                            'slash_coinCnt': st.column_config.Column('참격', help="코인 개수"),
                            'pierce_coinCnt': st.column_config.Column('관통', help="코인 개수"),
                            'blunt_coinCnt': st.column_config.Column('타격', help="코인 개수"),
                            'def_type': '수비 스킬',
                            'def_sin': "자원 - 수비",
                            'simpSinCnt_wrath': '분노',
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
                            'sinCnt_envy': '질투',
                            'resist_slash': '참격 내성',
                            'resist_pierce': '관통 내성',
                            'resist_blunt': '타격 내성',
                            'battlePassive_sin': '자원',
                            'battlePassive_sinCnt': '필요 개수',
                            'battlePassive_type': '종류',
                            'battlePassive': '전투 패시브',
                            'supportPassive_sin': '자원',
                            'supportPassive_sinCnt': '필요 개수',
                            'supportPassive_type': '종류',
                            'supportPassive': '서포트 패시브',
                            'etc': '특이사항'
                            }
             )