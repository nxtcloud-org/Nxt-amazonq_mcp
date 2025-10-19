import streamlit as st
import boto3
from botocore.exceptions import ClientError
import json
import random
from datetime import datetime, timedelta
import time

# --- 페이지 설정 ---
st.set_page_config(layout="wide", page_title="영상의학과 스마트 도우미", page_icon="🏥")

# --- 앱 제목 ---
st.title("🏥 영상의학과 스마트 도우미")
st.subheader("검사 정보 조회, 대기 현황 확인, AI 챗봇 상담")
st.write("---")

# --- 사이드바: 메뉴 선택 ---
st.sidebar.title("📋 메뉴")
menu_option = st.sidebar.selectbox(
    "원하는 서비스를 선택하세요",
    ["🔍 검사 정보 조회", "⏰ 대기 현황", "💊 조영제 부작용 체크", "🤖 AI 챗봇 상담"],
)


# --- Bedrock 클라이언트 생성 함수 ---
@st.cache_resource
def get_bedrock_client():
    try:
        client = boto3.client("bedrock-runtime", region_name="us-east-1")
        return client
    except Exception as e:
        st.error(f"AWS 연결 오류: {e}")
        return None


# --- 검사 정보 데이터 ---
EXAM_INFO = {
    "X-ray": {
        "preparation": "특별한 준비사항 없음",
        "duration": "5-10분",
        "fasting": "금식 불필요",
        "medication": "복용 중단 약물 없음",
        "notes": "임신 가능성이 있는 경우 미리 알려주세요",
    },
    "CT": {
        "preparation": "검사 전 4시간 금식",
        "duration": "15-30분",
        "fasting": "검사 전 4시간 금식",
        "medication": "당뇨약은 검사 당일 아침 복용 중단",
        "notes": "조영제 사용 시 알레르기 반응 가능성 있음",
    },
    "MRI": {
        "preparation": "금속 물질 제거 (보석, 시계, 카드 등)",
        "duration": "30-60분",
        "fasting": "검사 종류에 따라 다름",
        "medication": "특별한 제한 없음",
        "notes": "폐쇄공포증 환자는 미리 알려주세요",
    },
    "초음파": {
        "preparation": "복부 초음파는 8시간 금식",
        "duration": "15-30분",
        "fasting": "복부 초음파만 금식",
        "medication": "특별한 제한 없음",
        "notes": "복부 초음파는 방광이 찬 상태에서 검사",
    },
}


# --- 대기 현황 시뮬레이션 데이터 ---
def get_waiting_status():
    return {
        "total_appointments": random.randint(45, 65),
        "current_waiting": random.randint(3, 12),
        "xray_status": random.choice(["가동중", "점심시간", "정비중"]),
        "ct_status": random.choice(["가동중", "점심시간", "정비중"]),
        "mri_status": random.choice(["가동중", "점심시간", "정비중"]),
        "ultrasound_status": random.choice(["가동중", "점심시간", "정비중"]),
        "avg_wait_time": random.randint(15, 45),
    }


# --- 조영제 부작용 체크 함수 ---
def check_contrast_risk(answers):
    risk_score = 0
    risk_factors = []

    if answers.get("allergy", False):
        risk_score += 3
        risk_factors.append("과거 알레르기 반응")

    if answers.get("asthma", False):
        risk_score += 2
        risk_factors.append("천식")

    if answers.get("kidney", False):
        risk_score += 3
        risk_factors.append("신장 질환")

    if answers.get("diabetes", False):
        risk_score += 1
        risk_factors.append("당뇨병")

    if answers.get("pregnancy", False):
        risk_score += 2
        risk_factors.append("임신")

    return risk_score, risk_factors


# --- AI 챗봇 응답 생성 ---
def generate_ai_response(question):
    client = get_bedrock_client()
    if not client:
        return "AI 서비스 연결에 문제가 있습니다."

    # RAG 기반 응답을 위한 프롬프트
    prompt = f"""
    당신은 영상의학과 전문 AI 어시스턴트입니다. 
    다음 질문에 대해 정확하고 도움이 되는 답변을 제공해주세요.
    
    질문: {question}
    
    답변 시 다음 사항을 고려해주세요:
    1. 일반적인 검사 정보는 제공하되, 구체적인 진단은 의료진 상담을 권합니다
    2. 응급상황이나 심각한 증상이 있다면 즉시 의료진 상담을 권합니다
    3. 답변할 수 없는 복잡한 질문은 "의료진 상담 필요"라고 안내합니다
    4. 친근하고 이해하기 쉬운 언어로 답변합니다
    """

    try:
        response = client.converse(
            modelId="amazon.nova-lite-v1:0",
            messages=[{"role": "user", "content": [{"text": prompt}]}],
            inferenceConfig={"maxTokens": 1000, "temperature": 0.7},
        )
        return response["output"]["message"]["content"][0]["text"]
    except Exception as e:
        return f"AI 응답 생성 중 오류가 발생했습니다: {e}"


# --- 메인 앱 로직 ---
if menu_option == "🔍 검사 정보 조회":
    st.header("🔍 검사 정보 조회")

    col1, col2 = st.columns([1, 2])

    with col1:
        exam_type = st.selectbox("검사 종류를 선택하세요", list(EXAM_INFO.keys()))

    with col2:
        if exam_type:
            info = EXAM_INFO[exam_type]
            st.subheader(f"{exam_type} 검사 정보")

            col_a, col_b = st.columns(2)

            with col_a:
                st.write("**📋 준비사항**")
                st.info(info["preparation"])

                st.write("**⏱️ 소요시간**")
                st.success(info["duration"])

            with col_b:
                st.write("**🍽️ 금식 여부**")
                if "금식" in info["fasting"]:
                    st.warning(info["fasting"])
                else:
                    st.success(info["fasting"])

                st.write("**💊 약물 복용**")
                st.info(info["medication"])

            st.write("**⚠️ 주의사항**")
            st.error(info["notes"])

elif menu_option == "⏰ 대기 현황":
    st.header("⏰ 실시간 대기 현황")

    # 대기 현황 데이터 가져오기
    status = get_waiting_status()

    # 메트릭 표시
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📅 오늘 예약", f"{status['total_appointments']}건")

    with col2:
        st.metric("⏳ 현재 대기", f"{status['current_waiting']}명")

    with col3:
        st.metric("⏱️ 평균 대기시간", f"{status['avg_wait_time']}분")

    with col4:
        st.metric("📊 예상 완료", f"{status['current_waiting'] * 20}분 후")

    st.write("---")

    # 검사실별 상태
    st.subheader("🏥 검사실별 현황")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**X-ray실**")
        if status["xray_status"] == "가동중":
            st.success("🟢 가동중")
        elif status["xray_status"] == "점심시간":
            st.warning("🟡 점심시간 (12:00-13:00)")
        else:
            st.error("🔴 정비중")

        st.write("**CT실**")
        if status["ct_status"] == "가동중":
            st.success("🟢 가동중")
        elif status["ct_status"] == "점심시간":
            st.warning("🟡 점심시간 (12:00-13:00)")
        else:
            st.error("🔴 정비중")

    with col2:
        st.write("**MRI실**")
        if status["mri_status"] == "가동중":
            st.success("🟢 가동중")
        elif status["mri_status"] == "점심시간":
            st.warning("🟡 점심시간 (12:00-13:00)")
        else:
            st.error("🔴 정비중")

        st.write("**초음파실**")
        if status["ultrasound_status"] == "가동중":
            st.success("🟢 가동중")
        elif status["ultrasound_status"] == "점심시간":
            st.warning("🟡 점심시간 (12:00-13:00)")
        else:
            st.error("🔴 정비중")

    # 자동 새로고침
    if st.button("🔄 상태 새로고침"):
        st.rerun()

elif menu_option == "💊 조영제 부작용 체크":
    st.header("💊 조영제 부작용 자가 체크")
    st.write("조영제 사용 전 안전성을 확인하기 위한 간단한 체크리스트입니다.")

    st.write("---")

    # 체크리스트
    st.subheader("📋 체크리스트")

    answers = {}

    col1, col2 = st.columns(2)

    with col1:
        answers["allergy"] = st.checkbox("과거 알레르기 반응 경험")
        answers["asthma"] = st.checkbox("천식 진단 이력")
        answers["kidney"] = st.checkbox("신장 질환 이력")

    with col2:
        answers["diabetes"] = st.checkbox("당뇨병 진단 이력")
        answers["pregnancy"] = st.checkbox("임신 중 (여성)")
        answers["medication"] = st.checkbox("혈압약 복용 중")

    st.write("---")

    if st.button("🔍 위험도 평가", type="primary"):
        risk_score, risk_factors = check_contrast_risk(answers)

        st.subheader("📊 평가 결과")

        if risk_score == 0:
            st.success("✅ **안전**: 조영제 사용에 특별한 제한이 없습니다.")
        elif risk_score <= 2:
            st.warning("⚠️ **주의**: 의료진과 상담 후 조영제 사용을 고려하세요.")
        elif risk_score <= 4:
            st.error("🚨 **위험**: 조영제 사용 전 반드시 의료진 상담이 필요합니다.")
        else:
            st.error(
                "🚨 **고위험**: 조영제 사용을 권하지 않습니다. 대체 검사 방법을 고려하세요."
            )

        if risk_factors:
            st.write("**발견된 위험 요인:**")
            for factor in risk_factors:
                st.write(f"• {factor}")

        st.write("---")
        st.info(
            "💡 **주의**: 이 체크리스트는 참고용입니다. 최종 판단은 의료진과 상담하세요."
        )

elif menu_option == "🤖 AI 챗봇 상담":
    st.header("🤖 AI 챗봇 상담")
    st.write("영상의학과 검사에 대한 궁금한 점을 자유롭게 질문해보세요.")

    # 채팅 히스토리 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 채팅 히스토리 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자 입력
    if prompt := st.chat_input("궁금한 점을 입력하세요..."):
        # 사용자 메시지 추가
        st.session_state.messages.append({"role": "user", "content": prompt})

        # AI 응답 생성
        with st.chat_message("assistant"):
            with st.spinner("AI가 답변을 생성하고 있습니다..."):
                response = generate_ai_response(prompt)
                st.markdown(response)

        # AI 응답을 히스토리에 추가
        st.session_state.messages.append({"role": "assistant", "content": response})

    # 예시 질문들
    st.write("---")
    st.subheader("💡 자주 묻는 질문 예시")

    example_questions = [
        "CT 찍으려면 금식해야 하나요?",
        "MRI 검사 시간 얼마나 걸리나요?",
        "조영제 부작용은 어떤 게 있나요?",
        "임신 중에 X-ray 찍어도 되나요?",
        "검사 결과 언제 나오나요?",
    ]

    for i, question in enumerate(example_questions):
        if st.button(f"Q{i+1}: {question}", key=f"example_{i}"):
            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("assistant"):
                with st.spinner("AI가 답변을 생성하고 있습니다..."):
                    response = generate_ai_response(question)
                    st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# --- 하단 정보 ---
st.write("---")
st.info(
    """
    💡 **영상의학과 스마트 도우미**는 AI 기술을 활용하여 환자들의 검사 관련 문의를 효율적으로 처리합니다. 
    복잡한 의학적 판단이 필요한 경우에는 반드시 의료진과 상담하시기 바랍니다.
    """
)
