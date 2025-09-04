# Amazon Q MCP

Amazon Q 설치 및 MCP 설정을 위한 자동화 스크립트를 제공합니다.

## ⚡ 빠른 시작

```bash
# 1. Amazon Q 설치
./install_amazon_q.sh

# 2. MCP 설정 생성 및 편집
./setup_amazonq_mcp.sh
./setup_amazonq_mcp.sh --edit
```

## 📋 요구사항

- Linux 환경 (x86_64 아키텍처)
- `curl` 명령어
- `unzip` 명령어
- `nano` 에디터 (MCP 설정 편집용)
- 인터넷 연결

## 🚀 설치 방법

### 1단계: Amazon Q 설치

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

## 📁 파일 구조

```
Nxt-amazonq_mcp/
├── README.md                # 이 파일
├── install_amazon_q.sh      # Amazon Q 자동 설치 스크립트
└── setup_amazonq_mcp.sh     # Amazon Q MCP 설정 스크립트
```

## 🔧 스크립트 기능

### install_amazon_q.sh

Amazon Q 설치 스크립트는 다음 작업을 자동으로 수행합니다:

1. **다운로드**: Amazon Q 최신 버전 다운로드
2. **압축 해제**: 다운로드된 zip 파일 해제
3. **설치**: Amazon Q 설치 스크립트 실행
4. **에러 처리**: 각 단계별 성공/실패 확인
5. **정리**: 임시 파일 자동 삭제
6. **진행 상황 표시**: 각 단계별 상태 메시지 출력

### setup_amazonq_mcp.sh

MCP 설정 스크립트는 다음 작업을 자동으로 수행합니다:

1. **디렉토리 생성**: `~/.aws/amazonq` 디렉토리 생성
2. **설정 파일 생성**: `mcp.json` 파일 생성
3. **파일 권한 설정**: 보안을 위한 적절한 권한 설정 (600)
4. **nano 편집 기능**: `--edit` 옵션으로 nano 에디터 실행
5. **에러 처리**: 각 단계별 성공/실패 확인
6. **사용자 가이드**: 다음 단계 안내 및 사용법 제공

## 📝 MCP 설정 파일

생성되는 `~/.aws/amazonq/mcp.json` 파일의 기본 내용:

```json
{
  "mcpServers": {
    "postgresql-mcp": {
      "command": "npx",
      "args": [
        "@henkey/postgres-mcp-server",
        "--connection-string", "postgresql://{user}:{password}@{host}:5432/{database}"
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

## 🎯 전체 설치 과정

1. **Amazon Q 설치**:
   ```bash
   ./install_amazon_q.sh
   ```

2. **MCP 설정 생성**:
   ```bash
   ./setup_amazonq_mcp.sh
   ```

3. **설정 파일 편집**:
   ```bash
   ./setup_amazonq_mcp.sh --edit
   ```

4. **데이터베이스 연결 정보 입력** (nano 에디터에서)

## ⚠️ 주의사항

- 스크립트 실행 전에 실행 권한이 있는지 확인하세요
- 설치 과정에서 관리자 권한이 필요할 수 있습니다
- 네트워크 연결이 안정적인 환경에서 실행하세요
- MCP 설정 파일에는 민감한 정보가 포함되므로 적절한 권한 설정이 중요합니다

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

## 📞 지원

문제가 발생하면 GitHub Issues를 통해 문의해주세요.
