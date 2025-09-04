#!/bin/bash

# Amazon Q MCP 설정 스크립트
# 이 스크립트는 Amazon Q MCP 설정을 위한 디렉토리와 설정 파일을 생성합니다.

set -e  # 에러 발생 시 스크립트 종료

# 함수: nano 편집 모드
edit_with_nano() {
    echo "📝 nano 에디터로 설정 파일을 편집합니다..."
    echo "💡 편집 후 Ctrl+X, Y, Enter를 눌러 저장하고 종료하세요."
    echo ""
    read -p "계속하시겠습니까? (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        nano ~/.aws/amazonq/mcp.json
        echo "✅ 편집이 완료되었습니다."
    else
        echo "❌ 편집이 취소되었습니다."
    fi
}

# --edit 옵션 처리
if [ "$1" = "--edit" ]; then
    if [ -f ~/.aws/amazonq/mcp.json ]; then
        edit_with_nano
        exit 0
    else
        echo "❌ 설정 파일이 존재하지 않습니다. 먼저 기본 설정을 생성하세요."
        exit 1
    fi
fi

echo "🚀 Amazon Q MCP 설정을 시작합니다..."

# 1. 디렉토리 생성
echo "📁 Amazon Q MCP 디렉토리를 생성하는 중..."
mkdir -p ~/.aws/amazonq

if [ $? -eq 0 ]; then
    echo "✅ 디렉토리가 성공적으로 생성되었습니다: ~/.aws/amazonq"
else
    echo "❌ 디렉토리 생성에 실패했습니다."
    exit 1
fi

# 2. 설정 파일 생성
echo "📝 MCP 설정 파일을 생성하는 중..."

# mcp.json 파일 내용
cat > ~/.aws/amazonq/mcp.json << 'JSON_EOF'
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
JSON_EOF

if [ $? -eq 0 ]; then
    echo "✅ MCP 설정 파일이 성공적으로 생성되었습니다: ~/.aws/amazonq/mcp.json"
else
    echo "❌ 설정 파일 생성에 실패했습니다."
    exit 1
fi

# 3. 파일 권한 설정
echo "🔐 파일 권한을 설정하는 중..."
chmod 600 ~/.aws/amazonq/mcp.json

if [ $? -eq 0 ]; then
    echo "✅ 파일 권한이 설정되었습니다."
else
    echo "⚠️  파일 권한 설정에 실패했습니다. (계속 진행)"
fi

# 4. 설정 파일 내용 확인
echo "📋 생성된 설정 파일 내용:"
echo "----------------------------------------"
cat ~/.aws/amazonq/mcp.json
echo "----------------------------------------"

echo ""
echo "🎉 Amazon Q MCP 설정이 완료되었습니다!"
echo ""
echo "📝 다음 단계:"
echo "1. ~/.aws/amazonq/mcp.json 파일을 편집하여 실제 데이터베이스 연결 정보를 입력하세요"
echo "2. {user}, {password}, {host}, {database} 부분을 실제 값으로 교체하세요"
echo ""
echo "💡 편집 방법:"
echo "   방법 1: nano ~/.aws/amazonq/mcp.json"
echo "   방법 2: ./setup_amazonq_mcp.sh --edit"
echo ""
echo "�� 사용법:"
echo "   ./setup_amazonq_mcp.sh        # 기본 설정 생성"
echo "   ./setup_amazonq_mcp.sh --edit # nano로 편집"
