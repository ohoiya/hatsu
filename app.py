import streamlit as st

# 리스트 선언: 범죄 종류별 기본 형량 정의 (최소 형량, 최대 형량)
crime_list = [
    {"name": "살인", "min": 10, "max": 25},
    {"name": "마약", "min": 5, "max": 15},
    {"name": "절도", "min": 1, "max": 6},
    {"name": "폭행", "min": 1, "max": 5},
]

# 버튼 클릭 시 실행될 함수 정의
def check_risk(choice, age):
    st.markdown("---")
    st.subheader("[결과 출력 화면]")

    # 조건 판단: 나이가 14세 미만이라면 촉법 판별 및 감경 설정
    if age < 14:
        status_msg = "촉법임 (형량 5년 감경 적용)"
        discount = 5
    else:
        status_msg = "촉법이 아님"
        discount = 0

    st.write(f"- {status_msg}")

    # 반복 출력: for 구문을 이용해 선택한 범죄의 형량 배치
    for crime in crime_list:
        if crime["name"] == choice:
            # 감경 적용 후 형량이 0년 미만이 되지 않도록 처리
            final_min = max(0, crime["min"] - discount)
            final_max = max(0, crime["max"] - discount)
            st.write(f"- {crime['name']}: {final_min}~{final_max}년")

    # 두꺼운 글자로 표시
    st.markdown("**착하게 삽시다**")


# --- 앱 화면 구성 (시작: 사용자가 앱에 접속함) ---
st.title("형량 예측")
st.caption("※ 본 앱은 수업 및 조례 개정 참고용 시뮬레이션입니다.")

# 1. 입력받기: choice로 범죄 선택
choice = st.selectbox(
    "1. 범죄 종류 선택:",
    ["살인", "마약", "절도", "폭행"]
)

# 2. 입력받기: age로 나이 입력받음 (슬라이더: 5~100)
age = st.slider("2. 나이 입력:", min_value=5, max_value=100, value=20)

# 3. 버튼 클릭 시: check_risk 함수 실행
if st.button("분석하기"):
    check_risk(choice, age)
