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
        "cost_envy": 'background-color: #d9d2e9',
        "ovclockcost_wrath": 'background-color: #f4cccc',
        "ovclockcost_lust": 'background-color: #fce5cd',
        "ovclockcost_sloth": 'background-color: #fff2cc',
        "ovclockcost_gluttony": 'background-color: #d9ead3',
        "ovclockcost_gloom": 'background-color: #d0e0e3',
        "ovclockcost_pride": 'background-color: #c9daf8',
        "ovclockcost_envy": 'background-color: #d9d2e9'
        }
    
    return [color.get(val.name, "background-color: white") if i != 0 else "background-color: white" for i in val]

def color_sin_char(val):
    color = {
        "취약": 'color: red',
        "내성": 'color: gray',
        "견딤": 'color: #4472c4',
        "0": 'color: white',
        0: 'color: white'
        }
    
    return color.get(val, "color: black")

def real_format(value):
    if value % 1 == 0:
        return f"{value:.0f}"
    else:
        return f"{value:.1f}"

bd.make_egoList()

ego = st.session_state["ego"].copy()

ego = ego.style.applymap(color_sin_char).apply(color_sin_bg).format({
    "cost_wrath": real_format,
    "cost_lust": real_format,
    "cost_sloth": real_format,
    "cost_gluttony": real_format,
    "cost_gloom": real_format,
    "cost_pride": real_format,
    "cost_envy": real_format,
    "ovclockcost_wrath": real_format,
    "ovclockcost_lust": real_format,
    "ovclockcost_sloth": real_format,
    "ovclockcost_gluttony": real_format,
    "ovclockcost_gloom": real_format,
    "ovclockcost_pride": real_format,
    "ovclockcost_envy": real_format,
    "atkWeight_slash": real_format,
    "atkWeight_pierce": real_format,
    "atkWeight_blunt": real_format,
    "atkWeight_slash_ovclock": real_format,
    "atkWeight_pierce_ovclock": real_format,
    "atkWeight_blunt_ovclock": real_format,
    "burn": real_format,
    "burn_cnt": real_format,
    "bleed": real_format,
    "bleed_cnt": real_format,
    "tremor": real_format,
    "tremor_cnt": real_format,
    "tremor_burst": real_format,
    "tremor_selfCnt": real_format,
    "rupture": real_format,
    "rupture_cnt": real_format,
    "sinking": real_format,
    "sinking_cnt": real_format,
    "poise_give": real_format,
    "poise_cnt_give": real_format,
    "charge_barrier": real_format,
    "atkWeight": real_format,
    "aggro": real_format,
    "aggro": real_format,
    "haste": real_format,
    "bind": real_format,
    "protect": real_format,
    "fragile": real_format,
    "paralyze": real_format,
    "power_up": real_format,
    "power_down": real_format,
    "Pcoin_drop": real_format,
    "offLv_up": real_format,
    "offLv_down": real_format,
    "defLv_up": real_format,
    'defLv_down': real_format,
    'damage_up': real_format,
    'damage_down': real_format,
    'ovclock_burn': real_format,
    'ovclock_burn_cnt': real_format,
    'ovclock_bleed': real_format,
    'ovclock_bleed_cnt': real_format,
    'ovclock_tremor': real_format,
    'ovclock_tremor_cnt': real_format,
    'ovclock_tremor_burst': real_format,
    'ovclock_tremor_selfCnt': real_format,
    'ovclock_rupture': real_format,
    'ovclock_rupture_cnt': real_format,
    'ovclock_sinking': real_format,
    'ovclock_sinking_cnt': real_format,
    'ovclock_poise_give': real_format,
    'ovclock_poise_cnt_give': real_format,
    'ovclock_charge_barrier': real_format,
    'ovclock_atkWeight': real_format,
    'ovclock_aggro': real_format,
    'ovclock_haste': real_format,
    'ovclock_bind': real_format,
    'ovclock_protect': real_format,
    'ovclock_fragile': real_format,
    'ovclock_paralyze': real_format,
    'ovclock_power_up': real_format,
    'ovclock_power_down': real_format,
    'ovclock_Pcoin_drop': real_format,
    'ovclock_offLv_up': real_format,
    'ovclock_offLv_down': real_format,
    'ovclock_defLv_up': real_format,
    'ovclock_defLv_down': real_format,
    'ovclock_damage_up': real_format,
    'ovclock_damage_down': real_format
    })

colums = ['sinner','ego',
          'grade',
          'resist_wrath','resist_lust','resist_sloth','resist_gluttony','resist_gloom','resist_pride','resist_envy',
          'cost_wrath','cost_lust','cost_sloth','cost_gluttony','cost_gloom','cost_pride','cost_envy',
          "ovclockcost_wrath","ovclockcost_lust","ovclockcost_sloth","ovclockcost_gluttony","ovclockcost_gloom","ovclockcost_pride","ovclockcost_envy",
          'atkWeight_slash','atkWeight_pierce','atkWeight_blunt',
          'atkWeight_slash_ovclock','atkWeight_pierce_ovclock','atkWeight_blunt_ovclock',
          'burn','burn_cnt','bleed','bleed_cnt','tremor','tremor_cnt','tremor_burst','amplitude_conversion','amplitude_entangle','tremor_selfCnt','rupture','rupture_cnt','sinking','sinking_cnt','poise','poise_cnt','poise_give','poise_cnt_give','charge','charge_cnt','charge_barrier','special_keyword',
          'atkWeight','aggro','haste','bind','protect','fragile','paralyze','power_up','power_down','Pcoin_drop','offLv_up','offLv_down','defLv_up','defLv_down','damage_up','damage_down','target',
          'ovclock_burn','ovclock_burn_cnt','ovclock_bleed','ovclock_bleed_cnt','ovclock_tremor','ovclock_tremor_cnt','ovclock_tremor_burst','ovclock_amplitude_conversion','ovclock_amplitude_entangle','ovclock_tremor_selfCnt','ovclock_rupture','ovclock_rupture_cnt','ovclock_sinking','ovclock_sinking_cnt','ovclock_poise','ovclock_poise_cnt','ovclock_poise_give','ovclock_poise_cnt_give','ovclock_charge','ovclock_charge_cnt','ovclock_charge_barrier','ovclock_special_keyword',
          'ovclock_atkWeight','ovclock_aggro','ovclock_haste','ovclock_bind','ovclock_protect','ovclock_fragile','ovclock_paralyze','ovclock_power_up','ovclock_power_down','ovclock_Pcoin_drop','ovclock_offLv_up','ovclock_offLv_down','ovclock_defLv_up','ovclock_defLv_down','ovclock_damage_up','ovclock_damage_down','ovclock_target',
          'passive', 'info'
          ]

ovclock = st.checkbox("오버클록", False)
if ovclock:
    colums.remove('atkWeight_slash')
    colums.remove('atkWeight_pierce')
    colums.remove('atkWeight_blunt')
    colums.remove("cost_wrath")
    colums.remove("cost_lust")
    colums.remove("cost_sloth")
    colums.remove("cost_gluttony")
    colums.remove("cost_gloom")
    colums.remove("cost_pride")
    colums.remove("cost_envy")
    colums.remove("burn")
    colums.remove('burn_cnt')
    colums.remove("bleed")
    colums.remove('bleed_cnt')
    colums.remove("tremor")
    colums.remove('tremor_cnt')
    colums.remove('tremor_burst')
    colums.remove('amplitude_conversion')
    colums.remove('amplitude_entangle')
    colums.remove('tremor_selfCnt')
    colums.remove("rupture")
    colums.remove('rupture_cnt')
    colums.remove("sinking")
    colums.remove('sinking_cnt')
    colums.remove("poise")
    colums.remove('poise_cnt')
    colums.remove("poise_give")
    colums.remove('poise_cnt_give')
    colums.remove("charge")
    colums.remove('charge_cnt')
    colums.remove('charge_barrier')
    colums.remove("special_keyword")
    colums.remove("atkWeight")
    colums.remove("aggro")
    colums.remove("haste")
    colums.remove("bind")
    colums.remove("protect")
    colums.remove("fragile")
    colums.remove("paralyze")
    colums.remove("power_up")
    colums.remove("power_down")
    colums.remove("Pcoin_drop")
    colums.remove("offLv_up")
    colums.remove("offLv_down")
    colums.remove("defLv_up")
    colums.remove("defLv_down")
    colums.remove("damage_up")
    colums.remove("damage_down")
    colums.remove("target")
else:
    colums.remove('atkWeight_slash_ovclock')
    colums.remove('atkWeight_pierce_ovclock')
    colums.remove('atkWeight_blunt_ovclock')
    colums.remove("ovclockcost_wrath")
    colums.remove("ovclockcost_lust")
    colums.remove("ovclockcost_sloth")
    colums.remove("ovclockcost_gluttony")
    colums.remove("ovclockcost_gloom")
    colums.remove("ovclockcost_pride")
    colums.remove("ovclockcost_envy")
    colums.remove("ovclock_burn")
    colums.remove('ovclock_burn_cnt')
    colums.remove("ovclock_bleed")
    colums.remove('ovclock_bleed_cnt')
    colums.remove("ovclock_tremor")
    colums.remove('ovclock_tremor_cnt')
    colums.remove('ovclock_tremor_burst')
    colums.remove('ovclock_amplitude_conversion')
    colums.remove('ovclock_amplitude_entangle')
    colums.remove('ovclock_tremor_selfCnt')
    colums.remove("ovclock_rupture")
    colums.remove('ovclock_rupture_cnt')
    colums.remove("ovclock_sinking")
    colums.remove('ovclock_sinking_cnt')
    colums.remove("ovclock_poise")
    colums.remove('ovclock_poise_cnt')
    colums.remove("ovclock_poise_give")
    colums.remove('ovclock_poise_cnt_give')
    colums.remove("ovclock_charge")
    colums.remove("ovclock_charge_cnt")
    colums.remove('ovclock_charge_barrier')
    colums.remove('ovclock_special_keyword')
    colums.remove('ovclock_atkWeight')
    colums.remove('ovclock_aggro')
    colums.remove('ovclock_haste')
    colums.remove('ovclock_bind')
    colums.remove('ovclock_protect')
    colums.remove('ovclock_fragile')
    colums.remove('ovclock_paralyze')
    colums.remove('ovclock_power_up')
    colums.remove('ovclock_power_down')
    colums.remove('ovclock_Pcoin_drop')
    colums.remove('ovclock_offLv_up')
    colums.remove('ovclock_offLv_down')
    colums.remove('ovclock_defLv_up')
    colums.remove('ovclock_defLv_down')
    colums.remove('ovclock_damage_up')
    colums.remove('ovclock_damage_down')
    colums.remove('ovclock_target')

with st.expander("열 선택"):
    info, keywords1, keywords2 = st.columns(3)

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
            if not ovclock:
                colums.remove('cost_wrath')
                colums.remove('cost_lust')
                colums.remove('cost_sloth')
                colums.remove('cost_gluttony')
                colums.remove('cost_gloom')
                colums.remove('cost_pride')
                colums.remove('cost_envy')
            else:
                colums.remove("ovclockcost_wrath")
                colums.remove("ovclockcost_lust")
                colums.remove("ovclockcost_sloth")
                colums.remove("ovclockcost_gluttony")
                colums.remove("ovclockcost_gloom")
                colums.remove("ovclockcost_pride")
                colums.remove("ovclockcost_envy")
        if not info.checkbox("공격 가중치", True):
            if not ovclock:
                colums.remove('atkWeight_slash')
                colums.remove('atkWeight_pierce')
                colums.remove('atkWeight_blunt')
            else:
                colums.remove('atkWeight_slash_ovclock')
                colums.remove('atkWeight_pierce_ovclock')
                colums.remove('atkWeight_blunt_ovclock')
        if not info.checkbox("패시브", True, key='atkWeightC'):
            colums.remove("passive")
        info.write("")

    with keywords1:
        keywords1.write("키워드")
        
        if not keywords1.checkbox("화상", False):
            if not ovclock:
                colums.remove("burn")
                colums.remove('burn_cnt')
            else:
                colums.remove("ovclock_burn")
                colums.remove('ovclock_burn_cnt')
        if not keywords1.checkbox("출혈", False):
            if not ovclock:
                colums.remove("bleed")
                colums.remove('bleed_cnt')
            else:
                colums.remove("ovclock_bleed")
                colums.remove('ovclock_bleed_cnt')
        if not keywords1.checkbox("진동", False):
            if not ovclock:
                colums.remove("tremor")
                colums.remove('tremor_cnt')
                colums.remove('tremor_burst')
                colums.remove('amplitude_conversion')
                colums.remove('amplitude_entangle')
                colums.remove('tremor_selfCnt')
            else:
                colums.remove("ovclock_tremor")
                colums.remove('ovclock_tremor_cnt')
                colums.remove('ovclock_tremor_burst')
                colums.remove('ovclock_amplitude_conversion')
                colums.remove('ovclock_amplitude_entangle')
                colums.remove('ovclock_tremor_selfCnt')
        if not keywords1.checkbox("파열", False):
            if not ovclock:
                colums.remove("rupture")
                colums.remove('rupture_cnt')
            else:
                colums.remove("ovclock_rupture")
                colums.remove('ovclock_rupture_cnt')
        if not keywords1.checkbox("침잠", False):
            if not ovclock:
                colums.remove("sinking")
                colums.remove('sinking_cnt')
            else:
                colums.remove("ovclock_sinking")
                colums.remove('ovclock_sinking_cnt')
        if not keywords1.checkbox("호흡", False):
            if not ovclock:
                colums.remove("poise")
                colums.remove('poise_cnt')
                colums.remove("poise_give")
                colums.remove('poise_cnt_give')
            else:
                colums.remove("ovclock_poise")
                colums.remove('ovclock_poise_cnt')
                colums.remove("ovclock_poise_give")
                colums.remove('ovclock_poise_cnt_give')
        if not keywords1.checkbox("충전", False):
            if not ovclock:
                colums.remove("charge")
                colums.remove('charge_cnt')
                colums.remove('charge_barrier')
            else:
                colums.remove("ovclock_charge")
                colums.remove("ovclock_charge_cnt")
                colums.remove('ovclock_charge_barrier')
        if not keywords1.checkbox("특수 키워드", True):
            if not ovclock:
                colums.remove("special_keyword")
            else:
                colums.remove('ovclock_special_keyword')
        if not keywords1.checkbox("추가 가중치", True):
            if not ovclock:
                colums.remove("atkWeight")
            else:
                colums.remove('ovclock_atkWeight')
    
    with keywords2:
        if not keywords2.checkbox("도발치", False):
            if not ovclock:
                colums.remove("aggro")
            else:
                colums.remove('ovclock_aggro')
        if not keywords2.checkbox("신속", False):
            if not ovclock:
                colums.remove("haste")
            else:
                colums.remove('ovclock_haste')
        if not keywords2.checkbox("속박", False):
            if not ovclock:
                colums.remove("bind")
            else:
                colums.remove('ovclock_bind')
        if not keywords2.checkbox("보호", False):
            if not ovclock:
                colums.remove("protect")
            else:
                colums.remove('ovclock_protect')
        if not keywords2.checkbox("취약", False):
            if not ovclock:
                colums.remove("fragile")
            else:
                colums.remove('ovclock_fragile')
        if not keywords2.checkbox("마비", False):
            if not ovclock:
                colums.remove("paralyze")
            else:
                colums.remove('ovclock_paralyze')
        if not keywords2.checkbox("위력 증가", False):
            if not ovclock:
                colums.remove("power_up")
            else:
                colums.remove('ovclock_power_up')
        if not keywords2.checkbox("위력 감소", False):
            if not ovclock:
                colums.remove("power_down")
            else:
                colums.remove('ovclock_power_down')
        if not keywords2.checkbox("더하기 코인 약화", False):
            if not ovclock:
                colums.remove("Pcoin_drop")
            else:
                colums.remove('ovclock_Pcoin_drop')
        if not keywords2.checkbox("공격 레벨 증가", False):
            if not ovclock:
                colums.remove("offLv_up")
            else:
                colums.remove('ovclock_offLv_up')
        if not keywords2.checkbox("공격 레벨 감소", False):
            if not ovclock:
                colums.remove("offLv_down")
            else:
                colums.remove('ovclock_offLv_down')
        if not keywords2.checkbox("방어 레벨 증가", False):
            if not ovclock:
                colums.remove("defLv_up")
            else:
                colums.remove('ovclock_defLv_up')
        if not keywords2.checkbox("방어 레벨 감소", False):
            if not ovclock:
                colums.remove("defLv_down")
            else:
                colums.remove('ovclock_defLv_down')
        if not keywords2.checkbox("피해량 증가", False):
            if not ovclock:
                colums.remove("damage_up")
            else:
                colums.remove('ovclock_damage_up')
        if not keywords2.checkbox("피해량 감소", False):
            if not ovclock:
                colums.remove("damage_down")
            else:
                colums.remove('ovclock_damage_down')
        if not keywords2.checkbox("타겟 우선도", False):
            if not ovclock:
                colums.remove("target")
            else:
                colums.remove('ovclock_target')

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
             height=530,
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
                            'atkWeight_slash': '참격 가중치',
                            'atkWeight_pierce': '관통 가중치',
                            'atkWeight_blunt': '타격 가중치',
                            'atkWeight_slash_ovclock': '참격 가중치',
                            'atkWeight_pierce_ovclock': '관통 가중치',
                            'atkWeight_blunt_ovclock': '타격 가중치',
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
                            'target': "타겟 우선도",
                            'ovclockcost_wrath': '분노',
                            'ovclockcost_lust': '색욕',
                            'ovclockcost_sloth': '나태',
                            'ovclockcost_gluttony': '탐식',
                            'ovclockcost_gloom': '우울',
                            'ovclockcost_pride': '오만',
                            'ovclockcost_envy': '질투',
                            'ovclock_burn': '화상 위력',
                            'ovclock_burn_cnt': '화상 횟수',
                            'ovclock_bleed': '출혈 위력',
                            'ovclock_bleed_cnt': '출혈 횟수',
                            'ovclock_tremor': '진동 위력',
                            'ovclock_tremor_cnt': '진동 횟수',
                            'ovclock_tremor_burst': '진동 폭발',
                            'ovclock_amplitude_conversion': '진폭 변환',
                            'ovclock_amplitude_entangle': '진폭 얽힘',
                            'ovclock_tremor_selfCnt': '자가 진동 수급',
                            'ovclock_rupture': '파열 위력',
                            'ovclock_rupture_cnt': '파열 횟수',
                            'ovclock_sinking': '침잠 위력',
                            'ovclock_sinking_cnt': '침잠 횟수',
                            'ovclock_poise': '호흡 위력',
                            'ovclock_poise_cnt': '호흡 횟수',
                            'ovclock_poise_give': '호흡 위력 부여',
                            'ovclock_poise_cnt_give': '호흡 횟수 부여',
                            'ovclock_charge': '충전 위력',
                            'ovclock_charge_cnt': '충전 횟수',
                            'ovclock_charge_barrier': '충전 역장',
                            'ovclock_special_keyword': st.column_config.TextColumn('특수 키워드', help='자가수급 미포함'),
                            'ovclock_atkWeight': '추가 가중치',
                            'ovclock_aggro': '도발치',
                            'ovclock_haste': st.column_config.NumberColumn('신속', help='자가수급 미포함'),
                            'ovclock_bind': '속박',
                            'ovclock_protect': st.column_config.NumberColumn('보호', help='자가수급 미포함'),
                            'ovclock_fragile': st.column_config.NumberColumn('취약', help='속성 취약 포함'),
                            'ovclock_paralyze': '마비',
                            'ovclock_power_up': st.column_config.NumberColumn('위력 증가', help='자가수급 미포함, 합/수비/속성 위력 증가 포함'),
                            'ovclock_power_down': st.column_config.NumberColumn('위력 감소', help='합/수비/속성 위력 감소 포함'),
                            'ovclock_Pcoin_drop': '더하기 코인 약화',
                            'ovclock_offLv_up': st.column_config.NumberColumn('공격 레벨 증가', help='자가수급 미포함'),
                            'ovclock_offLv_down': '공격 레벨 감소',
                            'ovclock_defLv_up': st.column_config.NumberColumn('방어 레벨 증가', help='자가수급 미포함'),
                            'ovclock_defLv_down': '방어 레벨 감소',
                            'ovclock_damage_up': st.column_config.NumberColumn('피해량 증가', help='자가수급 미포함, 속성 피해량 증가 포함'),
                            'ovclock_damage_down': st.column_config.NumberColumn('피해량 감소', help='속성 피해량 감소 포함'),
                            'ovclock_target': "타겟 우선도",
                            'passive': '패시브',
                            'info': st.column_config.LinkColumn("상세정보", display_text="링크", help="단빵숲 사이트의 각 에고 정보 페이지")
                            }
             )