import streamlit as st
import os

st.title("림버스 컴퍼니 파티메이커")
st.write(" \n ")
st.write(" \n ")

maker = st.Page(os.path.join("system","maker.py"),title="파티 구성", icon=":material/library_add:")
id = st.Page(os.path.join("system","identity.py"),title="인격 목록", icon=":material/manage_search:")
ego = st.Page(os.path.join("system","EGO.py"),title="E.G.O 목록", icon=":material/manage_search:")
keyword = st.Page(os.path.join("system","keywords.py"),title="키워드 목록", icon=":material/manage_search:")
setting = st.Page(os.path.join("system","setting.py"),title="동기화 / 레벨 설정", icon=":material/settings:")
credit = st.Page(os.path.join("system","credit.py"),title="Credit", icon=":material/person:")

st.sidebar.markdown("## Limbus Company Deck Maker")

menu = st.navigation({"":[maker], "List":[id, ego, keyword], "Settings":[setting, credit]})

menu.run()
