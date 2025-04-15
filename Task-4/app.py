import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv('financial_updates.csv')
    return data

def main():
    st.set_page_config(page_title="Financial Updates", layout="wide")
    st.title("Financial Updates for IT Companies")
    data = load_data()
    st.write("### Latest Financial Reports")
    sort_column = st.selectbox("Sort by", data.columns)
    ascending = st.radio("Sort order", ("Ascending", "Descending"))
    ascending = True if ascending == "Ascending" else False
    sorted_data = data.sort_values(by=sort_column, ascending=ascending)
    filter_column = st.selectbox("Filter by", data.columns)
    filter_value = st.text_input(f"Enter {filter_column} value to filter")
    if filter_value:
        filtered_data = sorted_data[sorted_data[filter_column].str.contains(filter_value, case=False, na=False)]
    else:
        filtered_data = sorted_data
    st.dataframe(filtered_data)
    page_size = st.slider("Select the number of rows per page", 5, 50, 10)
    page_number = st.number_input("Page number", min_value=1, value=1)
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    page_data = filtered_data.iloc[start_idx:end_idx]
    st.dataframe(page_data)
    total_pages = len(filtered_data) // page_size + 1
    if page_number > 1:
        if st.button("Previous Page"):
            st.session_state.page_number -= 1
            st.experimental_rerun()
    if page_number < total_pages:
        if st.button("Next Page"):
            st.session_state.page_number += 1
            st.experimental_rerun()

if __name__ == "__main__":
    if "page_number" not in st.session_state:
        st.session_state.page_number = 1
    main()
