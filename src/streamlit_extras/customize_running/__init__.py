import time

import streamlit as st

center_css = """
<style>

div[class='css-4z1n4l ehezqtx5']{

    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50%;
}

</style>
"""


def center_running():
    st.markdown(center_css, unsafe_allow_html=True)


def example():
    click = st.button("Observe where the 🏃‍♂️ running widget is now!")
    if click:
        center_running()
        time.sleep(2)


__func__ = center_running
__title__ = "Customize running"
__desc__ = "Customize the running widget"
__icon__ = "🏃‍♂️"
__examples__ = [example]
__author__ = "koninhoo"
__forum_url__ = (
    "https://discuss.streamlit.io/t/change-the-running-widget-position/30466"
)
__experimental_playground__ = False