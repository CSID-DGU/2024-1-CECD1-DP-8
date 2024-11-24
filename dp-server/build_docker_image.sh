#!/bin/bash

# 프로젝트 clean & build
./gradlew clean build -x test

# 현재 시간으로 태그 생성
TIMESTAMP=$(date +%Y%m%d%H%M%S)
IMAGE_NAME="limwngur/app:$TIMESTAMP"

# Docker 이미지 빌드
docker build -t $IMAGE_NAME .

# 빌드 결과 확인
if [ $? -eq 0 ]; then
  echo "Docker 이미지 '$IMAGE_NAME'가 성공적으로 빌드되었습니다."
else
  echo "Docker 이미지 빌드 중 오류가 발생했습니다."
  exit 1
fi

# Docker Hub에 이미지 push
echo "Docker Hub에 이미지 '$IMAGE_NAME'를 push 중..."
docker push $IMAGE_NAME

if [ $? -eq 0 ]; then
  echo "이미지가 Docker Hub에 성공적으로 푸시되었습니다."
else
  echo "이미지가 푸시 중 오류가 발생했습니다."
fi

#이미지 생성 확인
docker images