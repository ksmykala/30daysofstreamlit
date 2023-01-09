import streamlit as st


def first_week():
    st.title('Welcome')
    st.write('[#30daysofstreamlit](https://30days.streamlit.app/)')

    st.write('Select page from the sidebar')


def app():
    first_week()


if __name__ == '__main__':
    app()