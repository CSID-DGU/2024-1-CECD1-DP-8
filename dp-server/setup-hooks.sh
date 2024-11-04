#!/bin/sh
cp hooks/pre-commit ../.git/hooks/pre-commit  # 상위 폴더의 .git/hooks로 복사
chmod +x ../.git/hooks/pre-commit  # 실행 권한 부여
