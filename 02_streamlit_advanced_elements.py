import streamlit as st

st.set_page_config(
    page_title="영상 제작",
    layout="centered",
)

st.title("영상 제작")
st.write("영상에 넣을 내용과 기본 설정을 정해 주세요.")

topic = st.text_input(
    "영상 주제",
    placeholder="예: 우리 학교 축제 소개",
)

video_type = st.selectbox(
    "영상 형식",
    ["쇼츠", "발표 영상", "홍보 영상"],
)

duration = st.slider(
    "영상 길이(초)",
    min_value=15,
    max_value=180,
    value=60,
    step=15,
)

include_subtitles = st.checkbox("자막 넣기", value=True)

if st.button("설정 확인"):
    if topic:
        st.success("입력한 내용을 확인했습니다.")
        st.write(f"영상 주제: {topic}")
        st.write(f"영상 형식: {video_type}")
        st.write(f"영상 길이: {duration}초")
        st.write(f"자막: {'포함' if include_subtitles else '미포함'}")
    else:
        st.warning("영상 주제를 입력해 주세요.")

st.caption("제작:박준호 학번 : 20221703/ 이름 : 박준호")
