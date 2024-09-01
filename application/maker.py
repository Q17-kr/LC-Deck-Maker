import streamlit as st
from collections import Counter
from application import baseDef as bd

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
        }
    
    return [color.get(val.name, "") if i != 0 else "" for i in val]

def real_format(value):
    if isinstance(value, int):
        return value
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
    sinners = ["이상", "파우스트", "돈키호테", "료슈", "뫼르소", "홍루",
               "히스클리프", "이스마엘", "로쟈", "싱클레어", "오티스", "그레고르"]

    sinner1 = inputSinners.selectbox("수감자1", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed")
    sinner2 = inputSinners.selectbox("수감자2", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed")
    sinner3 = inputSinners.selectbox("수감자3", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed")
    sinner4 = inputSinners.selectbox("수감자4", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed")
    sinner5 = inputSinners.selectbox("수감자5", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed")
    sinner6 = inputSinners.selectbox("수감자6", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed")

    id1,id2,id3,id4,id5,id6 = "","","","","",""

    try: id1 = Id.loc[(Id["sinner"] == sinner1) & (Id["identity"] == inputId.selectbox("인격1", Id.loc[(Id["sinner"] == sinner1),"identity"], index=None, placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id2 = Id.loc[(Id["sinner"] == sinner2) & (Id["identity"] == inputId.selectbox("인격2", Id.loc[(Id["sinner"] == sinner2),"identity"], index=None, placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id3 = Id.loc[(Id["sinner"] == sinner3) & (Id["identity"] == inputId.selectbox("인격3", Id.loc[(Id["sinner"] == sinner3),"identity"], index=None, placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id4 = Id.loc[(Id["sinner"] == sinner4) & (Id["identity"] == inputId.selectbox("인격4", Id.loc[(Id["sinner"] == sinner4),"identity"], index=None, placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id5 = Id.loc[(Id["sinner"] == sinner5) & (Id["identity"] == inputId.selectbox("인격5", Id.loc[(Id["sinner"] == sinner5),"identity"], index=None, placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass
    try: id6 = Id.loc[(Id["sinner"] == sinner6) & (Id["identity"] == inputId.selectbox("인격6", Id.loc[(Id["sinner"] == sinner6),"identity"], index=None, placeholder="인격 선택", label_visibility="collapsed"))].index[0]
    except IndexError:
        pass

if has_duplicates([sinner1,sinner2,sinner3,sinner4,sinner5,sinner6]):
    Input.error("중복된 수감자가 있습니다.")

with Output:
    makerId = Id.loc[[i for i in [id1,id2,id3,id4,id5,id6] if i != ""]]

    if setting == "기본":
        col = ["simpSinCnt_wrath",
               "simpSinCnt_lust",
               "simpSinCnt_sloth",
               "simpSinCnt_gluttony",
               "simpSinCnt_gloom",
               "simpSinCnt_pride",
               "simpSinCnt_envy"
               ]
    elif setting == "단기전":
        col = ["sinCnt_wrath",
               "sinCnt_lust",
               "sinCnt_sloth",
               "sinCnt_gluttony",
               "sinCnt_gloom",
               "sinCnt_pride",
               "sinCnt_envy"
               ]
    Output.dataframe(makerId[col], hide_index=True,
                     width=375,
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
      <th style="background-color: #ea9999;">{real_format(total[0])}</th>
      <th style="background-color: #f9cb9c;">{real_format(total[1])}</th>
      <th style="background-color: #ffe599;">{real_format(total[2])}</th>
      <th style="background-color: #b6d7a8;">{real_format(total[3])}</th>
      <th style="background-color: #a2c4c9;">{real_format(total[4])}</th>
      <th style="background-color: #a4c2f4;">{real_format(total[5])}</th>
      <th style="background-color: #b4a7d6;">{real_format(total[6])}</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background-color: #f4cccc;">(+{makerId['def_sin'].value_counts().get('분노', 0)})</td>
      <td style="background-color: #fce5cd;">(+{makerId['def_sin'].value_counts().get('색욕', 0)})</td>
      <td style="background-color: #fff2cc;">(+{makerId['def_sin'].value_counts().get('나태', 0)})</td>
      <td style="background-color: #d9ead3;">(+{makerId['def_sin'].value_counts().get('탐식', 0)})</td>
      <td style="background-color: #d0e0e3;">(+{makerId['def_sin'].value_counts().get('우울', 0)})</td>
      <td style="background-color: #c9daf8;">(+{makerId['def_sin'].value_counts().get('오만', 0)})</td>
      <td style="background-color: #d9d2e9;">(+{makerId['def_sin'].value_counts().get('질투', 0)})</td>
    </tr>
  </tbody>
</table>
''', unsafe_allow_html=True)
