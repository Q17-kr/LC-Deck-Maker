import streamlit as st
import pandas as pd
from application import baseDef as bd

bd.make_idList()

Id = st.session_state["id"].copy()
Id['speed_mean'] = (Id['min_speed'] + Id['max_speed']) / 2

colums = ['grade',
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

    with keywords:
        keywords.write("키워드")
        if not keywords.checkbox("화상", True):
            colums.remove("")

    with etc:
        if etc.radio("죄악 자원 수집",
                     ["기본",'단기전'],
                     index=0,
                     captions=['스토리/거울굴절철도','거울 던전'],
                     help="'단기전' 옵션은 1~3턴 이내로 전투가 끝나는 경우에 맞춰 설정되었습니다."
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

st.dataframe(st.session_state["id"],
             use_container_width=True,
             height=770,
             hide_index=True,
             column_order=['sinner','identity'] + colums
             )