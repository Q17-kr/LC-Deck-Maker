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
    
    return color.get(val, "color: black")

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
    
    return [color.get(val.name, "background-color: white") if i != 0 else "background-color: white" for i in val]

def real_format(value):
    if value % 1 == 0:
        return f"{value:.0f}"
    else:
        return f"{value:.1f}"

bd.make_idList()

Id = st.session_state["id"].copy()
Id['speed_mean'] = (Id['min_speed'] + Id['max_speed']) / 2
Id['def_sin'] = Id['def_sin'].replace('0', "")
Id['etc'] = Id['etc'].replace('0', "")
Id['tremor_selfCnt'] = Id['tremor_selfCnt'].replace(1, "O")
Id['poise'] = Id['poise'].replace(1, "O")
Id['poise_cnt'] = Id['poise_cnt'].replace(1, "O")
Id['charge'] = Id['charge'].replace(1, "O")
Id['charge_cnt'] = Id['charge_cnt'].replace(1, "O")

Id = Id.style.applymap(color_sin_char)\
    .apply(color_sin_bg)\
        .format({'min_speed':real_format,
                 'max_speed':real_format,
                 'speed_mean':real_format,
                 'hp':'{:.0f}',
                 'atkLv_mean':real_format,
                 'defLv':real_format,
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
                 'sinCnt_envy':real_format,
                 'burn':real_format,
                 'burn_cnt':real_format,
                 'bleed':real_format,
                 'bleed_cnt':real_format,
                 'tremor':real_format,
                 'tremor_cnt':real_format,
                 'tremor_burst':real_format,
                 'rupture':real_format,
                 'rupture_cnt':real_format,
                 'sinking':real_format,
                 'sinking_cnt':real_format,
                 'poise_give':real_format,
                 'poise_cnt_give':real_format,
                 'charge_barrier':real_format,
                 'atkWeight':real_format,
                 'aggro':real_format,
                 'haste':real_format,
                 'bind':real_format,
                 'protect':real_format,
                 'fragile':real_format,
                 'paralyze':real_format,
                 'power_up':real_format,
                 'power_down':real_format,
                 'Pcoin_drop':real_format,
                 'offLv_up':real_format,
                 'offLv_down':real_format,
                 'defLv_up':real_format,
                 'defLv_down':real_format,
                 'damage_up':real_format,
                 'damage_down':real_format,
                 'battlePassive_sinCnt':'{:.0f}',
                 'supportPassive_sinCnt':'{:.0f}'
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
          'burn','burn_cnt','bleed','bleed_cnt','tremor','tremor_cnt','tremor_burst','amplitude_conversion','amplitude_entangle','tremor_selfCnt','rupture','rupture_cnt','sinking','sinking_cnt','poise','poise_cnt','poise_give','poise_cnt_give','charge','charge_cnt','charge_barrier',
          'special_keyword','atkWeight',
          'aggro','haste','bind','protect','fragile','paralyze','power_up','power_down','Pcoin_drop','offLv_up','offLv_down','defLv_up','defLv_down','damage_up','damage_down',
          'battlePassive_sin','battlePassive_sinCnt','battlePassive_type','battlePassive',
          'supportPassive_sin','supportPassive_sinCnt','supportPassive_type','supportPassive',
          'etc','info'
          ]

with st.expander("열 선택"):
    info, keywords, etc = st.columns(3)

    with info:
        info.write("")
        if not info.checkbox("등급", False):
            colums.remove("grade")
        if not info.checkbox("체력", True):
            colums.remove("hp")
        if not info.checkbox("공격 레벨", False, help="평균값"):
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
        if not info.checkbox("수비 스킬", True):
            colums.remove("def_type")
            colums.remove("def_sin")
        info.write("")

    with keywords:
        keywords.write("키워드")
        if not keywords.checkbox("화상", False):
            colums.remove("burn")
            colums.remove("burn_cnt")
        if not keywords.checkbox("출혈", False):
            colums.remove("bleed")
            colums.remove("bleed_cnt")
        if not keywords.checkbox("진동", False):
            colums.remove("tremor")
            colums.remove("tremor_cnt")
            colums.remove("tremor_burst")
            colums.remove("amplitude_conversion")
            colums.remove("amplitude_entangle")
            colums.remove("tremor_selfCnt")
        if not keywords.checkbox("파열", False):
            colums.remove("rupture")
            colums.remove("rupture_cnt")
        if not keywords.checkbox("침잠", False):
            colums.remove("sinking")
            colums.remove("sinking_cnt")
        if not keywords.checkbox("호흡", False):
            colums.remove("poise")
            colums.remove("poise_cnt")
            colums.remove("poise_give")
            colums.remove("poise_cnt_give")
        if not keywords.checkbox("충전", False):
            colums.remove("charge")
            colums.remove("charge_cnt")
            colums.remove("charge_barrier")
        if not keywords.checkbox("특수 키워드", True, help='자가수급 미포함'):
            colums.remove("special_keyword")
        keywords.markdown('---')
        if not keywords.checkbox("추가 가중치", False):
            colums.remove("atkWeight")
        if not keywords.checkbox("도발치", False):
            colums.remove("aggro")
        if not keywords.checkbox("신속", False, help='자가수급 미포함'):
            colums.remove("haste")
        if not keywords.checkbox("속박", False):
            colums.remove("bind")
        if not keywords.checkbox("보호", False, help='자가수급 미포함'):
            colums.remove("protect")
        if not keywords.checkbox("취약", False, help='속성 취약 포함'):
            colums.remove("fragile")
        if not keywords.checkbox("마비", False):
            colums.remove("paralyze")
        if not keywords.checkbox("위력 증가", False, help='자가수급 미포함, 합/수비/속성 위력 증가 포함'):
            colums.remove("power_up")
        if not keywords.checkbox("위력 감소", False):
            colums.remove("power_down")
        if not keywords.checkbox("더하기 코인 약화", False):
            colums.remove("Pcoin_drop")
        if not keywords.checkbox("공격 레벨 증가", False, help='자가수급 미포함'):
            colums.remove("offLv_up")
        if not keywords.checkbox("공격 레벨 감소", False):
            colums.remove("offLv_down")
        if not keywords.checkbox("방어 레벨 증가", False, help='자가수급 미포함'):
            colums.remove("defLv_up")
        if not keywords.checkbox("방어 레벨 감소", False):
            colums.remove("defLv_down")
        if not keywords.checkbox("피해량 증가", False, help='자가수급 미포함, 속성 피해량 증가 포함'):
            colums.remove("damage_up")
        if not keywords.checkbox("피해량 감소", False, help='속성 피해량 감소 포함'):
            colums.remove("damage_down")
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
                  '특수 키워드':'special_keyword',
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
                       '특수 키워드',
                       '전투 패시브 자원',
                       '전투 패시브',
                       '서포트 패시브 자원',
                       '서포트 패시브'
                       ], index=3)
    searchTxT = txt.text_input("검색어",
                               value="")
    if txt.button("초기화"):
        search = "수감자"
        searchTxT = ""
    if searchTxT != "":
        Id = Id.loc[Id[searchList[search]].str.find(searchTxT) >= 0]

st.dataframe(Id, use_container_width=True, height=380,
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
                            'def_sin': "수비 스킬 자원",
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
                            'burn': '화상 위력',
                            'burn_cnt': '화상 횟수',
                            'bleed': '출혈 위력',
                            'bleed_cnt': '출혈 횟수',
                            'tremor': '진동 위력',
                            'tremor_cnt': '진동 횟수',
                            'tremor_burst': '진동 폭발',
                            'amplitude_conversion': '진폭 변환',
                            'amplitude_entangle': '진폭 얽힘',
                            'tremor_selfCnt': '자가 진동 수급',
                            'rupture': '파열 위력',
                            'rupture_cnt': '파열 횟수',
                            'sinking': '침잠 위력',
                            'sinking_cnt': '침잠 횟수',
                            'poise': '호흡 위력',
                            'poise_cnt': '호흡 횟수',
                            'poise_give': '호흡 위력 부여',
                            'poise_cnt_give': '호흡 횟수 부여',
                            'charge': '충전 위력',
                            'charge_cnt': '충전 횟수',
                            'charge_barrier': '충전 역장',
                            'special_keyword': st.column_config.TextColumn('특수 키워드', help='자가수급 미포함'),
                            'atkWeight': '추가 가중치',
                            'aggro': '도발치',
                            'haste': st.column_config.NumberColumn('신속', help='자가수급 미포함'),
                            'bind': '속박',
                            'protect': st.column_config.NumberColumn('보호', help='자가수급 미포함'),
                            'fragile': st.column_config.NumberColumn('취약', help='속성 취약 포함'),
                            'paralyze': '마비',
                            'power_up': st.column_config.NumberColumn('위력 증가', help='자가수급 미포함, 합/수비/속성 위력 증가 포함'),
                            'power_down': st.column_config.NumberColumn('위력 감소', help='합/수비/속성 위력 감소 포함'),
                            'Pcoin_drop': '더하기 코인 약화',
                            'offLv_up': st.column_config.NumberColumn('공격 레벨 증가', help='자가수급 미포함'),
                            'offLv_down': '공격 레벨 감소',
                            'defLv_up': st.column_config.NumberColumn('방어 레벨 증가', help='자가수급 미포함'),
                            'defLv_down': '방어 레벨 감소',
                            'damage_up': st.column_config.NumberColumn('피해량 증가', help='자가수급 미포함, 속성 피해량 증가 포함'),
                            'damage_down': st.column_config.NumberColumn('피해량 감소', help='속성 피해량 감소 포함'),
                            'battlePassive_sin': st.column_config.TextColumn('자원', help="전투 패시브"),
                            'battlePassive_sinCnt': st.column_config.TextColumn('필요 개수', help="전투 패시브"),
                            'battlePassive_type': st.column_config.TextColumn('종류', help="전투 패시브"),
                            'battlePassive': '전투 패시브',
                            'supportPassive_sin': st.column_config.TextColumn('자원', help="서포트 패시브"),
                            'supportPassive_sinCnt': st.column_config.TextColumn('필요 개수', help="서포트 패시브"),
                            'supportPassive_type': st.column_config.TextColumn('종류', help="서포트 패시브"),
                            'supportPassive': '서포트 패시브',
                            'etc': '특이사항',
                            'info': st.column_config.LinkColumn("상세정보", display_text="링크", help="단빵숲 사이트의 각 인격 정보 페이지")
                            }
             )