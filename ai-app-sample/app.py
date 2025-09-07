import streamlit as st
import boto3
from botocore.exceptions import ClientError

# --- 페이지 설정 ---
st.set_page_config(layout="wide", page_title="AI 논문 초록 생성기", page_icon="✍️")

# --- 앱 제목 ---
st.title("✍️ AI 논문 초록 생성기 📄")
st.subheader(
    "머릿속 아이디어를 던져주시면, AI가 그럴듯한 논문 초록으로 다듬어 드립니다."
)
st.write("---")

# --- 입력 폼과 결과를 두 개의 컬럼으로 구성 ---
col1, col2 = st.columns(2)

with col1:
    # --- 구조화된 입력 섹션 (더 캐주얼한 예시로 변경) ---
    st.write("####  STEP 1: 연구 아이디어 입력")
    research_topic = st.text_input("**연구 주제**", "대학생 과제와 생성형 AI")

    research_background = st.text_area(
        "**연구 배경 및 목적** (이 연구를 왜, 무엇을 위해 하나요?)",
        "요즘 대학생들 과제할 때 챗GPT 같은 AI를 많이 씀. 이게 과연 좋은 걸까? 과제 퀄리티에 어떤 영향을 주는지 궁금함.",
        height=150,
    )

    methodology = st.text_area(
        "**연구 방법** (어떻게 연구를 진행할 건가요?)",
        "두 그룹으로 나눠서 비교 실험. A그룹은 AI 사용, B그룹은 AI 미사용. 과제 결과물 점수 매기고, 설문조사도 진행.",
        height=150,
    )

    key_results = st.text_area(
        "**핵심 결과 또는 예상 결과** (무엇을 발견할 것으로 기대하나요?)",
        "AI 쓴 쪽이 과제는 빨리 끝낼 듯. 근데 내용은 다 비슷비슷하고 창의성은 떨어질 것 같음. 결국 AI를 잘 쓰는 법을 가르쳐야 한다는 결론이 나올 듯.",
        height=150,
    )


# --- Bedrock 클라이언트 생성 함수 ---
@st.cache_resource
def get_bedrock_client():
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    return client


# --- 스트리밍 응답을 처리하는 생성기 함수 ---
def generate_abstract_response(prompt):
    """
    Bedrock API를 호출하고 스트리밍 응답의 텍스트 청크를 반환하는 생성기 함수.
    """
    client = get_bedrock_client()
    model_id = "amazon.nova-lite-v1:0"

    conversation = [
        {
            "role": "user",
            "content": [{"text": prompt}],
        }
    ]

    try:
        streaming_response = client.converse_stream(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 4096, "temperature": 0.7, "topP": 0.9},
        )

        for chunk in streaming_response["stream"]:
            if "contentBlockDelta" in chunk:
                yield chunk["contentBlockDelta"]["delta"]["text"]

    except ClientError as e:
        st.error(f"AWS 오류가 발생했습니다: {e.response['Error']['Message']}")
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")


with col2:
    # --- 결과 출력 섹션 ---
    st.write("#### STEP 2: AI가 생성한 논문 초록 확인")

    if st.button("✨ 초록 생성하기", type="primary"):
        if not all([research_topic, research_background, methodology, key_results]):
            st.error("❌ 모든 필드를 입력해 주세요!")
        else:
            # --- AI 프롬프트 자동 생성 (강화된 버전) ---
            prompt = f"""
            당신은 간결하고 비공식적인 아이디어를 공식적이고 구조적인 학술 초록으로 발전시키는 데 능숙한 전문 학술 작가입니다.
            사용자가 제공하는 핵심 아이디어를 바탕으로, 논리적 흐름에 맞게 살을 붙이고 전문적인 학술 용어를 사용하여 국문 논문 초록(Abstract)을 작성해 주세요.
            입력값이 매우 캐주얼하더라도, 최종 결과물은 전문적이고 학술적인 어조를 반드시 유지해야 합니다.
            초록은 표준적인 학술 구조(연구 배경 및 목적, 연구 방법, 예상 결과, 시사점)가 자연스럽게 드러나도록 논리적으로 구성해야 합니다.

            [입력 정보]
            - 연구 주제: {research_topic}
            - 연구 배경 및 목적에 대한 아이디어: {research_background}
            - 연구 방법에 대한 아이디어: {methodology}
            - 핵심 결과 또는 예상 결과에 대한 아이디어: {key_results}
            
            위 아이디어들을 종합하여 약 200-250 단어 내외의 짜임새 있는 한 편의 완결된 글로 초록을 생성해 주세요.
            결과는 제목 없이 초록 내용만 바로 보여주세요.
            """

            # --- Bedrock API 호출 및 실시간 출력 ---
            st.info("🤖 AI가 아이디어를 논문 초록으로 다듬고 있습니다...")
            st.write("##### 📄 생성된 논문 초록")

            response_placeholder = st.empty()
            full_response = response_placeholder.write_stream(
                generate_abstract_response(prompt)
            )

# --- 하단 정보 박스 ---
st.write("---")
st.info(
    """
    💡 **연구 아이디어를 빠르게 초록으로 구체화**하여 동료나 지도교수님과 논의를 시작해 보세요. 연구의 방향성을 잡고 발전시키는 데 큰 도움이 될 것입니다.
    """
)
