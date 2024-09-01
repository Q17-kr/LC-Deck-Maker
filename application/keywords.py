import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import os

@st.cache_data
def get_keyword():
    with open(os.path.join('data','keywords','keywords.html'),
              'r', encoding='utf-8') as file:
        keywords = file.read()
    
    # soup = BeautifulSoup(keywords, 'lxml')
    # table = pd.read_html(str(soup))[0].to_html(index=False)

    # keywords = str(soup).replace(str(soup.find('table')), table)
    # keywords = keywords.replace('<head>',
    #                             '<head><style>th, td { display: none; }</style>'
    #                             )
    
    return keywords

st.components.v1.html(get_keyword(),
                      height=750, width=1100,
                      scrolling=True)