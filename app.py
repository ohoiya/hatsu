import streamlit as st

# 리스트 선언: 범죄 종류 및 형량 구간(bad) 정의
crime_list = ["절도", "성폭행", "살인", "마약"]
bad = ["1~6년", "7~13년", "10년이상"]


# 버튼 클릭 시 실행될 함수 정의
def check_risk(choice, age):
    st.markdown("---")
    st.subheader("[결과 출력 화면]")

    # 조건 판단: 나이가 14세 미만이라면 촉법임 문구 출력 및 감경 안내
    if age < 14:
        st.write("- 촉법임 (형량 -5년 감경 대상)")
    else:
        st.write("- 촉법이 아님")

    # 반복 출력: for 구문을 이용해 범죄별 형량(bad) 배치
    for crime in crime_list:
        if crime == choice:
            if crime == "절도" or crime == "마약":
                sentence = bad[0]  # 1~6년
            elif crime == "성폭행":
                sentence = bad[1]  # 7~13년
            elif crime == "살인":
                sentence = bad[2]  # 10년이상

            if age < 14:
                st.write(f"- {crime}: {sentence} (촉법 감경 -5년 적용)")
            else:
                st.write(f"- {crime}: {sentence}")

    # 결과물 표기 방식: 두꺼운 글자로 표시
    st.markdown("**착하게 삽시다**")


# --- 앱 화면 구성 (시작: 사용자가 앱에 접속함) ---
st.title("형량 예측")
st.caption("※ 본 앱은 수업 및 조례 개정 참고용입니다.")

# 입력받기: choice로 범죄 선택, age로 나이 입력받음
choice = st.selectbox("1. 범죄 종류 선택:", crime_list)
age = st.slider("2. 나이 입력:", min_value=5, max_value=100, value=20)

# 버튼 클릭 시: check_risk 함수 실행
if st.button("분석하기"):
    check_risk(choice, age)
