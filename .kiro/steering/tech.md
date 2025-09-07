# 기술 스택

## 핵심 기술

- **Shell Scripting**: 자동화를 위한 Bash 스크립트
- **HTML5/CSS3/JavaScript**: 간단한 웹 게임 구현
- **JSON**: MCP 설정을 위한 구성 파일
- **curl/unzip**: 다운로드 및 압축 해제 유틸리티

## 빌드 시스템 및 명령어

이 프로젝트는 자동화를 위해 shell 스크립트를 사용합니다. 복잡한 빌드 시스템은 필요하지 않습니다.

### 주요 명령어

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

## 의존성

- Linux 환경 (x86_64 아키텍처)
- `curl` 명령어
- `unzip` 명령어
- `nano` 에디터
- 인터넷 연결
- Node.js/npm (npx를 통한 MCP PostgreSQL 서버용)

## 구성 파일

- `~/.aws/amazonq/mcp.json`: MCP 서버 구성
- 보안을 위해 파일 권한을 600으로 설정

## 에러 처리

스크립트는 빠른 실패를 위해 `set -e`를 사용하며, 사용자 친화적인 상태 메시지와 함께 포괄적인 에러 검사를 포함합니다.
