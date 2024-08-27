import streamlit as st
from collections import Counter

def has_duplicates(lst):
    return any(count > 1 for count in Counter(lst).values())

st.header("파티 구성")
st.write(" \n ")
st.write(" \n ")

Input, Output = st.columns(2)
inputSinners, inputEGO = Input.columns(2)

with inputSinners:
    sinners = ["이상", "파우스트", "돈키호테", "료슈", "뫼르소", "홍루",
               "히스클리프", "이스마엘", "로쟈", "싱클레어", "오티스", "그레고르"]

    sinner1 = inputSinners.selectbox("", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed", key="s1")
    sinner2 = inputSinners.selectbox("", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed", key="s2")
    sinner3 = inputSinners.selectbox("", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed", key="s3")
    sinner4 = inputSinners.selectbox("", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed", key="s4")
    sinner5 = inputSinners.selectbox("", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed", key="s5")
    sinner6 = inputSinners.selectbox("", sinners, index=None, placeholder="수감자 선택", label_visibility="collapsed", key="s6")

    if has_duplicates([sinner1,sinner2,sinner3,sinner4,sinner5,sinner6]):
        st.error("중복된 수감자가 있습니다.")

with inputEGO:
    ego1 = inputEGO.selectbox("", sinners, index=None, placeholder="주로 사용하는 E.G.O 선택", label_visibility="collapsed", key="e1")
    ego2 = inputEGO.selectbox("", sinners, index=None, placeholder="주로 사용하는 E.G.O 선택", label_visibility="collapsed", key="e2")
    ego3 = inputEGO.selectbox("", sinners, index=None, placeholder="주로 사용하는 E.G.O 선택", label_visibility="collapsed", key="e3")
    ego4 = inputEGO.selectbox("", sinners, index=None, placeholder="주로 사용하는 E.G.O 선택", label_visibility="collapsed", key="e4")
    ego5 = inputEGO.selectbox("", sinners, index=None, placeholder="주로 사용하는 E.G.O 선택", label_visibility="collapsed", key="e5")
    ego6 = inputEGO.selectbox("", sinners, index=None, placeholder="주로 사용하는 E.G.O 선택", label_visibility="collapsed", key="e6")
