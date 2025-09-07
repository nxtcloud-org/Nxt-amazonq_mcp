# AI 논문 초록 생성기 ✍️

연구자들의 캐주얼한 아이디어를 전문적인 학술 초록으로 변환해주는 AI 기반 웹 애플리케이션입니다.

## 🎯 주요 기능

- **한국어 인터페이스**: 직관적인 한국어 사용자 인터페이스
- **구조화된 입력**: 연구 주제, 배경, 방법론, 예상 결과를 체계적으로 입력
- **AI 기반 변환**: AWS Bedrock의 Amazon Nova Lite 모델을 활용한 고품질 초록 생성
- **실시간 스트리밍**: 생성 과정을 실시간으로 확인할 수 있는 스트리밍 출력
- **예시 제공**: 입력 방법을 안내하는 현실적인 한국어 예시

## 🛠️ 기술 스택

- **Frontend**: Streamlit (Python 웹 프레임워크)
- **AI Service**: AWS Bedrock (Amazon Nova Lite v1.0)
- **Cloud**: AWS (us-east-1 리전)
- **Language**: Python 3.8+

## 📋 사전 요구사항

1. **Python 3.8 이상**
2. **AWS 계정 및 자격 증명 설정**
   - AWS CLI 설정 또는 환경 변수 설정
   - Bedrock 서비스 액세스 권한 필요
3. **AWS Bedrock 모델 액세스**
   - Amazon Nova Lite 모델에 대한 액세스 권한 필요

## 🚀 설치 및 실행

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. AWS 자격 증명 설정

다음 중 하나의 방법으로 AWS 자격 증명을 설정하세요:

**방법 1: AWS CLI 사용**

```bash
aws configure
```

**방법 2: 환경 변수 설정**

```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

### 3. 애플리케이션 실행

```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501`로 접속하여 애플리케이션을 사용할 수 있습니다.

## 💡 사용 방법

### STEP 1: 연구 아이디어 입력

1. **연구 주제**: 연구하고자 하는 주제를 간단히 입력
2. **연구 배경 및 목적**: 왜 이 연구를 하는지, 무엇을 위한 연구인지 캐주얼하게 작성
3. **연구 방법**: 어떻게 연구를 진행할 것인지 대략적인 방법 입력
4. **핵심 결과**: 예상되는 결과나 발견할 것으로 기대하는 내용 작성

### STEP 2: AI 초록 생성

- "✨ 초록 생성하기" 버튼을 클릭
- AI가 실시간으로 전문적인 학술 초록을 생성
- 200-250단어 내외의 구조화된 초록 완성

## 📝 입력 예시

**연구 주제**: "대학생 과제와 생성형 AI"

**연구 배경**: "요즘 대학생들 과제할 때 챗GPT 같은 AI를 많이 씀. 이게 과연 좋은 걸까? 과제 퀄리티에 어떤 영향을 주는지 궁금함."

**연구 방법**: "두 그룹으로 나눠서 비교 실험. A그룹은 AI 사용, B그룹은 AI 미사용. 과제 결과물 점수 매기고, 설문조사도 진행."

**핵심 결과**: "AI 쓴 쪽이 과제는 빨리 끝낼 듯. 근데 내용은 다 비슷비슷하고 창의성은 떨어질 것 같음."

## 🔧 주요 구성 요소

### 핵심 함수

- `get_bedrock_client()`: AWS Bedrock 클라이언트 초기화 및 캐싱
- `generate_abstract_response()`: 스트리밍 응답 처리 제너레이터

### AI 모델 설정

- **모델**: amazon.nova-lite-v1:0
- **최대 토큰**: 1024
- **Temperature**: 0.7
- **Top P**: 0.9

## ⚠️ 주의사항

1. **AWS 비용**: Bedrock API 사용 시 비용이 발생할 수 있습니다
2. **리전 설정**: 현재 us-east-1 리전으로 고정되어 있습니다
3. **모델 액세스**: Amazon Nova Lite 모델에 대한 액세스 권한이 필요합니다
4. **네트워크**: 안정적인 인터넷 연결이 필요합니다

## 🐛 문제 해결

### 일반적인 오류

**AWS 자격 증명 오류**

```
AWS 오류가 발생했습니다: The security token included in the request is invalid
```

→ AWS 자격 증명을 다시 설정하세요

**모델 액세스 오류**

```
AWS 오류가 발생했습니다: Access denied to model
```

→ AWS 콘솔에서 Bedrock 모델 액세스 권한을 확인하세요

**네트워크 연결 오류**

```
오류가 발생했습니다: Connection timeout
```

→ 인터넷 연결을 확인하고 다시 시도하세요

## 📄 라이선스

이 프로젝트는 교육 및 연구 목적으로 제공됩니다.

## 🤝 기여

버그 리포트나 기능 제안은 이슈로 등록해 주세요.

---

💡 **Tip**: 생성된 초록을 바탕으로 동료나 지도교수님과 연구 방향에 대해 논의해보세요!
