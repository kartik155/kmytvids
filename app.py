import streamlit as st
from  streamlit_player import st_player

import pandas as pd

df = pd.read_excel("processed_links.xlsx")
df.drop_duplicates(inplace = True)

if __name__ == "__main__":
    import os

    # df = pd.read_excel("processed_links.xlsx")
    # df.drop_duplicates(inplace = True)
    # print(df.shape[0])
    st.set_page_config(layout="wide", page_title = "Videos worth watching!")

    top_col = st.columns(3)
    top_col[1].header(f'{df.shape[0]} Videos worth watching!')
    st.divider()

    for i in range(df.shape[0]):
        cols = st.columns(2)

        with cols[0]:
            text = df.loc[i,"Title"]
            st.subheader(f":blue[{text}]")
            sub_cols = st.columns(2)
            with sub_cols[0]:
                st.subheader("Publish Date : ")
            with sub_cols[1]:
                st.subheader(df.loc[i,"Publish time"].split("T")[0])
            st_player(df.loc[i,"Links"], key = f"player_{i}")
            
        with cols[1]:            
            # st.subheader("Description:")
            # with st.expander("Description"):
            st.text_area(":green[Description]", df.loc[i,"Description"], height = 450)
        st.divider()