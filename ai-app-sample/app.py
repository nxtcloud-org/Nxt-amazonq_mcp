import streamlit as st
import boto3
from botocore.exceptions import ClientError

# --- 페이지 설정 ---
st.set_page_config(layout="wide", page_title="AI 이메일 작성기", page_icon="📧")

# --- 앱 제목 ---
st.title("📧 AI 정중한 이메일 초안 작성기 ✍️")
st.subheader("몇 가지 정보만 입력하면 AI가 격식에 맞는 이메일을 완성해 드려요.")
st.write("---")

# --- 입력 폼과 결과를 두 개의 컬럼으로 구성 ---
col1, col2 = st.columns(2)

with col1:
    # --- 구조화된 입력 섹션 ---
    st.write("####  STEP 1: 이메일 정보 입력")
    recipient = st.text_input(
        "**받는 사람** (예: 김민준 교수님, 인사팀장님)", "김민준 교수님"
    )

    purpose_options = {
        "과제 기한 연장 요청": "assignment_extension",
        "강의 내용 질문": "lecture_question",
        "면담 요청": "meeting_request",
        "감사 인사": "thank_you",
        "가벼운 안부 인사": "casual_greeting",
    }
    purpose_label = st.selectbox(
        "**이메일 목적**", options=list(purpose_options.keys())
    )

    tone_options = {
        "매우 정중하게 (격식체)": "very_formal",
        "친절하고 부드럽게": "friendly_formal",
        "간결하고 핵심만": "concise",
    }
    tone_label = st.radio(
        "**원하는 어조**", options=list(tone_options.keys()), horizontal=True
    )

    core_message = st.text_area(
        "**핵심 내용** (AI가 이 내용을 바탕으로 문장을 다듬습니다)",
        "안녕하세요, 교수님. 다름이 아니라 이번 주 과제 제출 기한을 하루만 연장해주실 수 있는지 정중히 여쭙고 싶습니다. 개인적인 사정으로 인해 부득이하게 요청드립니다.",
        height=150,
    )


# --- Bedrock 클라이언트 생성 함수 ---
# 캐싱을 사용하여 클라이언트 객체를 재사용함으로써 성능을 향상시킵니다.
@st.cache_resource
def get_bedrock_client():
    # Bedrock 클라이언트를 us-east-1 리전으로 생성합니다.
    # Nova 모델은 현재 해당 리전에서 사용 가능합니다.
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    return client


# --- 스트리밍 응답을 처리하는 생성기 함수 ---
def generate_email_response(prompt):
    """
    Bedrock API를 호출하고 스트리밍 응답의 텍스트 청크를 반환하는 생성기 함수.
    """
    client = get_bedrock_client()
    model_id = "amazon.nova-lite-v1:0"

    # Bedrock Converse API가 요구하는 대화 형식으로 메시지를 구성합니다.
    conversation = [
        {
            "role": "user",
            "content": [{"text": prompt}],
        }
    ]

    try:
        # 스트리밍 방식으로 Bedrock API를 호출합니다.
        streaming_response = client.converse_stream(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 1024, "temperature": 0.7, "topP": 0.9},
        )

        # 스트림에서 텍스트 청크를 추출하여 반환(yield)합니다.
        for chunk in streaming_response["stream"]:
            if "contentBlockDelta" in chunk:
                yield chunk["contentBlockDelta"]["delta"]["text"]

    except ClientError as e:
        # AWS 클라이언트 오류 처리
        st.error(f"AWS 오류가 발생했습니다: {e.response['Error']['Message']}")
    except Exception as e:
        # 기타 예외 처리
        st.error(f"오류가 발생했습니다: {e}")


with col2:
    # --- 결과 출력 섹션 ---
    st.write("#### STEP 2: AI가 생성한 이메일 확인")

    if st.button("✨ 이메일 생성하기", type="primary"):
        if not all([recipient, purpose_label, tone_label, core_message]):
            st.error("❌ 모든 필드를 입력해 주세요!")
        else:
            # --- AI 프롬프트 자동 생성 ---
            prompt = f"""
            '{recipient}'에게 보내는 이메일 초안을 작성해 줘.
            이메일의 목적은 '{purpose_label}'이야.
            전체적인 톤은 '{tone_label}' 스타일로 맞춰 줘.
            아래 핵심 내용을 바탕으로 자연스럽고 격식 있는 문장으로 완성해 줘.
            
            [핵심 내용]
            {core_message}
            
            결과는 '제목:'과 '본문:'으로 명확히 구분해서 보여줘.
            """

            # --- Bedrock API 호출 및 실시간 출력 ---
            st.info("🤖 AI가 이메일을 실시간으로 생성하고 있습니다...")
            st.write("##### 📧 생성된 이메일 초안")

            # st.write_stream을 사용하여 스트리밍 응답을 화면에 실시간으로 표시
            response_placeholder = st.empty()
            full_response = response_placeholder.write_stream(
                generate_email_response(prompt)
            )

# --- 하단 정보 박스 ---
st.write("---")
st.info(
    """
    💡 **AI 모델을 활용한 서비스**는 사용자가 복잡한 프롬프트를 고민할 필요 없이, **정해진 절차에 따라 최고의 결과물을 얻도록 돕는 것**이 핵심입니다.
    """
)
