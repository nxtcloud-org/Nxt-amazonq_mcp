# AI 개발 학습 도구 모음 🚀

AI 기반 애플리케이션 개발과 자동화 도구를 학습하기 위한 종합 레포지토리입니다. 실제 동작하는 예제들과 자동화 스크립트를 통해 현대적인 AI 개발 워크플로우를 경험할 수 있습니다.

## 🎯 포함된 학습 도구들

### 1. 🤖 AI 논문 초록 생성기 (`ai-app-sample/`)

**학습 목표**: Streamlit + AWS Bedrock을 활용한 AI 웹 애플리케이션 개발

- **기술 스택**: Python, Streamlit, AWS Bedrock (Amazon Nova Lite)
- **주요 기능**: 캐주얼한 연구 아이디어를 전문적인 학술 초록으로 변환
- **학습 포인트**: 실시간 스트리밍, AWS AI 서비스 통합, 한국어 UI 구현

### 2. 🔧 Amazon Q MCP 자동화 도구

**학습 목표**: 개발 환경 자동화 및 MCP(Model Context Protocol) 설정

- **기술 스택**: Shell Script, JSON 설정, AWS CLI
- **주요 기능**: Amazon Q 자동 설치 및 PostgreSQL MCP 서버 설정
- **학습 포인트**: 시스템 자동화, 설정 관리, 에러 처리

### 3. 🎮 HTML5 박스 피하기 게임 (`box-game-sample/`)

**학습 목표**: 순수 웹 기술을 활용한 인터랙티브 게임 개발

- **기술 스택**: HTML5, CSS3, JavaScript
- **주요 기능**: 키보드 조작, 충돌 감지, 점수 시스템
- **학습 포인트**: 게임 루프, 이벤트 처리, 캔버스 애니메이션

## ⚡ 빠른 시작

### AI 논문 초록 생성기 실행

```bash
cd ai-app-sample
pip install -r requirements.txt
streamlit run app.py
```

### Amazon Q 및 MCP 설정

```bash
# 1. Amazon Q 설치
./install_amazon_q.sh

# 2. MCP 설정 생성 및 편집
./setup_amazonq_mcp.sh
./setup_amazonq_mcp.sh --edit
```

### 박스 피하기 게임 실행

```bash
cd box-game-sample
python -m http.server 8000
# 브라우저에서 http://localhost:8000 접속
```

## 📋 학습 환경 요구사항

### 공통 요구사항

- **운영체제**: Linux/macOS (Windows WSL 지원)
- **Python**: 3.8 이상
- **인터넷 연결**: AWS API 호출 및 패키지 설치용

### AI 애플리케이션용

- **AWS 계정**: Bedrock 서비스 액세스 필요
- **AWS CLI**: 자격 증명 설정용
- **Python 패키지**: requirements.txt 참조

### 자동화 도구용

- **Shell 환경**: Bash 지원
- **시스템 도구**: `curl`, `unzip`, `nano`
- **아키텍처**: x86_64 (Amazon Q 설치용)

## � 학습 가법이드

### 🎓 추천 학습 순서

1. **HTML5 게임 (초급)** → 웹 기술 기초 학습
2. **AI 논문 초록 생성기 (중급)** → AI 서비스 통합 학습
3. **자동화 도구 (고급)** → 시스템 자동화 학습

### 📖 각 도구별 상세 가이드

각 디렉토리의 README.md 파일에서 상세한 학습 가이드를 확인하세요:

- [`ai-app-sample/README.md`](./ai-app-sample/README.md) - AI 웹 앱 개발 가이드
- [`box-game-sample/`](./box-game-sample/) - HTML5 게임 개발 가이드

## 🚀 설치 및 실행 방법

### 1단계: AI 논문 초록 생성기 실행

```bash
cd ai-app-sample
pip install -r requirements.txt

# AWS 자격 증명 설정 (둘 중 하나 선택)
aws configure
# 또는 환경 변수 설정
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1

streamlit run app.py
```

### 2단계: Amazon Q 설치

#### 자동 설치 (권장)

제공된 설치 스크립트를 사용하여 Amazon Q를 자동으로 설치할 수 있습니다:

```bash
./install_amazon_q.sh
```

#### 수동 설치

스크립트 없이 수동으로 설치하려면 다음 명령어를 순차적으로 실행하세요:

```bash
# 1. Amazon Q 다운로드
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip" -o "q.zip"

# 2. 압축 해제
unzip q.zip

# 3. 설치 스크립트 실행
./q/install.sh
```

### 2단계: MCP 설정

#### 자동 설정 (권장)

MCP 설정을 위한 디렉토리와 설정 파일을 자동으로 생성합니다:

```bash
./setup_amazonq_mcp.sh
```

#### nano로 편집

생성된 설정 파일을 nano 에디터로 편집합니다:

```bash
./setup_amazonq_mcp.sh --edit
```

#### 수동 편집

직접 nano 에디터로 설정 파일을 편집할 수도 있습니다:

```bash
nano ~/.aws/amazonq/mcp.json
```

## 📁 레포지토리 구조

```
AI-Learning-Toolkit/
├── README.md                    # 이 파일 (전체 가이드)
├── install_amazon_q.sh          # Amazon Q 자동 설치 스크립트
├── setup_amazonq_mcp.sh         # MCP 설정 스크립트
├── ai-app-sample/               # AI 웹 애플리케이션
│   ├── app.py                   # Streamlit 메인 앱
│   ├── requirements.txt         # Python 의존성
│   └── README.md                # 앱별 상세 가이드
├── box-game-sample/             # HTML5 게임 데모
│   └── index.html               # 게임 파일
├── .kiro/                       # Kiro AI 개발 환경
│   ├── specs/                   # 기능 스펙 문서
│   │   └── ai-abstract-generator/
│   │       ├── requirements.md  # 요구사항 정의
│   │       ├── design.md        # 시스템 설계
│   │       └── tasks.md         # 구현 작업 계획
│   └── steering/                # AI 가이드 문서
│       ├── product.md           # 제품 개요
│       ├── structure.md         # 프로젝트 구조
│       └── tech.md              # 기술 스택
└── .vscode/                     # VS Code 설정
```

## 🎯 학습 목표별 가이드

### 🤖 AI 서비스 통합 학습

**AI 논문 초록 생성기를 통해 학습할 수 있는 내용:**

- AWS Bedrock API 통합 방법
- 실시간 스트리밍 구현 기법
- Streamlit을 활용한 빠른 웹 앱 개발
- 한국어 자연어 처리 애플리케이션 구축
- 오류 처리 및 사용자 경험 최적화

### 🔧 시스템 자동화 학습

**자동화 스크립트를 통해 학습할 수 있는 내용:**

- Shell 스크립트 작성 및 에러 처리
- 시스템 설치 자동화 기법
- JSON 설정 파일 관리
- 파일 권한 및 보안 설정
- 사용자 친화적 CLI 도구 개발

### 🎮 웹 기술 기초 학습

**HTML5 게임을 통해 학습할 수 있는 내용:**

- HTML5 Canvas API 활용
- JavaScript 이벤트 처리
- CSS3 애니메이션 및 스타일링
- 게임 루프 및 상태 관리
- 반응형 웹 디자인

## 🔧 도구별 주요 기능

### AI 논문 초록 생성기 특징

- **실시간 AI 응답**: AWS Bedrock을 통한 스트리밍 생성
- **구조화된 입력**: 연구 아이디어를 체계적으로 정리
- **한국어 최적화**: 한국어 학술 문서에 특화된 프롬프트
- **사용자 친화적 UI**: 직관적인 2열 레이아웃

### 자동화 스크립트 특징

- **완전 자동화**: 원클릭 설치 및 설정
- **에러 복구**: 각 단계별 실패 시 적절한 안내
- **진행 상황 표시**: 이모지와 한국어 메시지로 상태 표시
- **보안 고려**: 적절한 파일 권한 및 설정 관리

## 📝 MCP 설정 파일

생성되는 `~/.aws/amazonq/mcp.json` 파일의 기본 내용:

```json
{
  "mcpServers": {
    "postgresql-mcp": {
      "command": "npx",
      "args": [
        "@henkey/postgres-mcp-server",
        "--connection-string",
        "postgresql://{user}:{password}@{host}:5432/{database}"
      ]
    }
  }
}
```

### 설정 파일 편집

실제 데이터베이스 연결 정보를 입력하려면 다음 부분을 수정하세요:

- `{user}`: 데이터베이스 사용자명
- `{password}`: 데이터베이스 비밀번호
- `{host}`: 데이터베이스 호스트 주소
- `{database}`: 데이터베이스 이름

## 🎯 전체 학습 과정

### 1단계: 기초 웹 기술 (HTML5 게임)

```bash
cd box-game-sample
python -m http.server 8000
# 브라우저에서 http://localhost:8000 접속
```

**학습 내용**: HTML5, CSS3, JavaScript 기초

### 2단계: AI 웹 애플리케이션 (논문 초록 생성기)

```bash
cd ai-app-sample
pip install -r requirements.txt
aws configure  # AWS 자격 증명 설정
streamlit run app.py
```

**학습 내용**: Python, Streamlit, AWS Bedrock 통합

### 3단계: 시스템 자동화 (Amazon Q + MCP)

```bash
./install_amazon_q.sh
./setup_amazonq_mcp.sh
./setup_amazonq_mcp.sh --edit
```

**학습 내용**: Shell 스크립트, 시스템 자동화, 설정 관리

## 💡 학습 팁

### 효과적인 학습 방법

1. **단계별 진행**: 각 도구를 순서대로 학습하여 난이도를 점진적으로 높이세요
2. **코드 분석**: 각 예제의 소스 코드를 자세히 분석하고 주석을 읽어보세요
3. **실험과 수정**: 코드를 수정해보며 동작 원리를 이해하세요
4. **문서 활용**: 각 디렉토리의 README.md와 .kiro/specs/ 문서를 참고하세요

### 추가 학습 리소스

- **AWS Bedrock 문서**: AI 서비스 통합에 대한 상세 가이드
- **Streamlit 문서**: 웹 앱 개발 프레임워크 학습
- **HTML5 Canvas 튜토리얼**: 게임 개발 기초 학습

## ⚠️ 주의사항

### AI 애플리케이션 사용 시

- **AWS 비용**: Bedrock API 사용 시 비용이 발생할 수 있습니다
- **자격 증명 보안**: AWS 키를 안전하게 관리하세요
- **리전 설정**: 현재 us-east-1 리전으로 설정되어 있습니다

### 자동화 스크립트 사용 시

- **실행 권한**: 스크립트 실행 전 권한을 확인하세요
- **시스템 요구사항**: Linux/macOS 환경에서 테스트되었습니다
- **네트워크 연결**: 안정적인 인터넷 연결이 필요합니다

## 🆘 문제 해결

### 권한 오류

```bash
chmod +x install_amazon_q.sh
chmod +x setup_amazonq_mcp.sh
```

### 네트워크 오류

- 인터넷 연결을 확인하세요
- 방화벽 설정을 확인하세요

### 설치 실패

- 시스템 요구사항을 확인하세요
- 로그 메시지를 확인하여 구체적인 오류 원인을 파악하세요

### MCP 설정 오류

- `~/.aws/amazonq` 디렉토리 권한을 확인하세요
- `mcp.json` 파일의 JSON 형식이 올바른지 확인하세요
- 데이터베이스 연결 정보가 정확한지 확인하세요

## 🤝 기여 및 지원

### 기여 방법

- **버그 리포트**: 발견한 문제점을 Issues로 등록해주세요
- **기능 제안**: 새로운 학습 도구나 개선사항을 제안해주세요
- **코드 기여**: Pull Request를 통해 코드 개선에 참여하세요
- **문서 개선**: 학습 가이드나 설명을 더 명확하게 만들어주세요

### 지원

- **GitHub Issues**: 기술적 문제나 질문
- **학습 가이드**: 각 디렉토리의 README.md 참조
- **스펙 문서**: .kiro/specs/ 디렉토리의 상세 문서 활용

---

🎓 **Happy Learning!** 이 레포지토리를 통해 AI 개발의 다양한 측면을 경험하고 실무 역량을 키워보세요!
