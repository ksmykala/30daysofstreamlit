import streamlit as st
from st_pages import first_week, hello_map, main_page

PAGES = {
    "Main": main_page,
    "Hello Map": hello_map,
    "Days 1-4": first_week,
}

selected_page = st.sidebar.selectbox(
    "Select the page", list(PAGES.keys()), index=0
)
page = PAGES[selected_page]
page.app()
