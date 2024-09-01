import streamlit as st

st.set_page_config(layout="wide")

import os
from application import baseDef as bd

def main():

    menu = st.navigation({"":[st.Page(os.path.join("application","maker.py"),title="파티 구성", icon=":material/library_add:")
                              ],
                          "List":[st.Page(os.path.join("application","identity.py"),title="인격 목록", icon=":material/manage_search:"),
                                  st.Page(os.path.join("application","EGO.py"),title="E.G.O 목록", icon=":material/manage_search:"),
                                  st.Page(os.path.join("application","keywords.py"),title="키워드 목록", icon=":material/manage_search:")
                                  ],
                          "Settings":[st.Page(os.path.join("application","setting.py"),title="동기화 / 레벨 설정", icon=":material/settings:"),
                                      st.Page(os.path.join("application","credit.py"),title="Credit", icon=":material/person:")
                                      ]
                          })
    
    bd.start_data()

    st.title("림버스 컴퍼니 파티메이커")
    st.write(" \n ")
    st.write(" \n ")

    st.sidebar.markdown("## Limbus Company Deck Maker")

    menu.run()

if __name__ == "__main__":
    main()
