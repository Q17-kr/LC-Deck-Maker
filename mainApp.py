import streamlit as st
import os
from application import baseDef

st.set_page_config(layout="wide")

def main():
    baseDef.start_data()

    st.title("림버스 컴퍼니 파티메이커")
    st.write(" \n ")
    st.write(" \n ")

    maker = st.Page(os.path.join("application","maker.py"),title="파티 구성", icon=":material/library_add:")
    id = st.Page(os.path.join("application","identity.py"),title="인격 목록", icon=":material/manage_search:")
    ego = st.Page(os.path.join("application","EGO.py"),title="E.G.O 목록", icon=":material/manage_search:")
    keyword = st.Page(os.path.join("application","keywords.py"),title="키워드 목록", icon=":material/manage_search:")
    setting = st.Page(os.path.join("application","setting.py"),title="동기화 / 레벨 설정", icon=":material/settings:")
    credit = st.Page(os.path.join("application","credit.py"),title="Credit", icon=":material/person:")

    st.sidebar.markdown("## Limbus Company Deck Maker")

    menu = st.navigation({"":[maker], "List":[id, ego, keyword], "Settings":[setting, credit]})

    menu.run()

if __name__ == "__main__":
    main()
