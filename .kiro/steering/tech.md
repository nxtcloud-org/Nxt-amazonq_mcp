# 기술 스택

## 핵심 기술

### AI 애플리케이션 스택

- **Python 3.8+**: 메인 프로그래밍 언어
- **Streamlit**: 웹 애플리케이션 프레임워크
- **AWS Bedrock**: AI 모델 서비스 (Amazon Nova Lite)
- **boto3/botocore**: AWS SDK for Python

### 자동화 및 설정 스택

- **Shell Scripting**: 자동화를 위한 Bash 스크립트
- **JSON**: MCP 설정을 위한 구성 파일
- **curl/unzip**: 다운로드 및 압축 해제 유틸리티

### 프론트엔드 데모 스택

- **HTML5/CSS3/JavaScript**: 간단한 웹 게임 구현

## 빌드 시스템 및 명령어

### AI 애플리케이션 실행

```bash
# AI 논문 초록 생성기 실행
cd ai-app-sample
pip install -r requirements.txt
streamlit run app.py
```

### 자동화 스크립트 실행

```bash
# 스크립트 실행 권한 부여
chmod +x install_amazon_q.sh
chmod +x setup_amazonq_mcp.sh

# Amazon Q 설치
./install_amazon_q.sh

# MCP 구성 설정
./setup_amazonq_mcp.sh

# nano로 MCP 구성 편집
./setup_amazonq_mcp.sh --edit
```

### 개발 및 테스트

```bash
# 박스 게임 데모 실행 (로컬 서버 필요)
cd box-game-sample
python -m http.server 8000
# 브라우저에서 http://localhost:8000 접속
```

## 의존성

### AI 애플리케이션 의존성

- **Python 3.8+**: 메인 런타임
- **AWS 계정**: Bedrock 서비스 액세스 필요
- **AWS 자격 증명**: CLI 설정 또는 환경 변수
- **인터넷 연결**: AWS API 호출을 위한 안정적인 연결

### 시스템 의존성

- **Linux/macOS 환경**: 스크립트 실행을 위한 Unix 계열 시스템
- **curl/unzip**: 다운로드 및 압축 해제 유틸리티
- **nano 에디터**: 구성 파일 편집용
- **Node.js/npm**: MCP PostgreSQL 서버용 (선택사항)

## 구성 파일

### AI 애플리케이션 구성

- **requirements.txt**: Python 패키지 의존성
- **AWS 자격 증명**: `~/.aws/credentials` 또는 환경 변수

### MCP 구성

- **~/.aws/amazonq/mcp.json**: MCP 서버 구성
- 보안을 위해 파일 권한을 600으로 설정

## 에러 처리

### Python 애플리케이션

- **AWS 오류**: ClientError 예외 처리 및 한국어 메시지 표시
- **입력 검증**: 사용자 입력 유효성 검사
- **스트리밍 오류**: 네트워크 중단 시 적절한 복구

### Shell 스크립트

- **빠른 실패**: `set -e`를 사용한 즉시 오류 중단
- **사용자 친화적 메시지**: 이모지와 한국어를 포함한 상태 표시
- **포괄적 검사**: 각 단계별 성공/실패 검증
