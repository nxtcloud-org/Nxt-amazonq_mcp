#!/bin/bash

# Amazon Q 설치 스크립트
# 이 스크립트는 Amazon Q를 다운로드하고 설치합니다.

set -e  # 에러 발생 시 스크립트 종료

echo "🚀 Amazon Q 설치를 시작합니다..."

# 1. Amazon Q 다운로드
echo "📥 Amazon Q를 다운로드하는 중..."
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip" -o "q.zip"

if [ $? -eq 0 ]; then
    echo "✅ 다운로드가 완료되었습니다."
else
    echo "❌ 다운로드에 실패했습니다."
    exit 1
fi

# 2. 압축 해제
echo "📦 압축을 해제하는 중..."
unzip q.zip

if [ $? -eq 0 ]; then
    echo "✅ 압축 해제가 완료되었습니다."
else
    echo "❌ 압축 해제에 실패했습니다."
    exit 1
fi

# 3. 설치 스크립트 실행
echo "🔧 Amazon Q를 설치하는 중..."
./q/install.sh

if [ $? -eq 0 ]; then
    echo "✅ Amazon Q 설치가 완료되었습니다!"
    echo "🎉 설치가 성공적으로 완료되었습니다."
else
    echo "❌ 설치에 실패했습니다."
    exit 1
fi

# 임시 파일 정리
echo "🧹 임시 파일을 정리하는 중..."
rm -f q.zip
echo "✅ 정리가 완료되었습니다."
