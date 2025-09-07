# 프로젝트 구조

## 루트 디렉토리 레이아웃

```
├── README.md                 # 한국어 문서 (주요)
├── index.html               # HTML5 박스 피하기 게임 데모
├── install_amazon_q.sh      # Amazon Q 설치 스크립트
├── setup_amazonq_mcp.sh     # MCP 구성 설정 스크립트
├── .gitignore              # 포괄적인 무시 규칙
├── .kiro/                  # Kiro AI 어시스턴트 구성
│   └── steering/           # AI 가이드 문서
└── .vscode/                # VS Code 설정
```

## 파일 구성 원칙

### 스크립트 (`*.sh`)

- 한국어 주석이 포함된 실행 가능한 shell 스크립트
- 에러 처리를 위해 `set -e` 사용
- 이모지를 포함한 진행 상황 표시기
- 일관된 명명 규칙 준수: `동작_대상.sh`

### 문서

- 한국어로 작성된 주요 문서 (`README.md`)
- 포괄적인 설정 지침
- 문제 해결 섹션 포함
- 단계별 설치 가이드

### 구성

- `~/.aws/amazonq/mcp.json`에 저장된 MCP 구성
- `.gitignore`를 통해 민감한 파일 제외
- 보안을 위해 파일 권한을 600으로 설정

### 데모 콘텐츠

- `index.html`: 독립형 게임 데모
- 인라인 CSS/JS로 자체 포함
- 한국어 언어 인터페이스

## 명명 규칙

- 스크립트: 소문자와 언더스코어 사용
- 문서: 한국어 선호
- 변수: JavaScript에서는 camelCase, shell에서는 snake_case
- 파일 권한: 스크립트는 755, 구성 파일은 600
