
import streamlit as st
import pandas as pd

st.title("학생 정보 입력 하기")

header = ['학번', '이름', '전공']

# 세션 상태에 학생 목록 저장 (앱이 재실행되어도 데이터 유지)
if 'students' not in st.session_state:
    st.session_state.students = []

# 입력 폼
with st.form("student_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        student_id = st.text_input("학번")
    with col2:
        name = st.text_input("이름")
    with col3:
        major = st.text_input("전공")

    submitted = st.form_submit_button("추가")

    if submitted:
        if not (student_id and name and major):
            st.warning("학번, 이름, 전공을 모두 입력해주세요.")
        elif not student_id.isdigit():
            st.error("학번은 숫자만 입력할 수 있습니다.")
        else:
            st.session_state.students.append([student_id, name, major])
            st.success(f"{name} 학생 정보가 추가되었습니다.")

# 표로 출력
st.subheader("학생 목록")
df = pd.DataFrame(st.session_state.students, columns=header)
st.table(df)
