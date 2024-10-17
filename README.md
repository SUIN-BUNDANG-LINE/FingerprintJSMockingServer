## 실행 방법

### 이미지 빌드

docker build -t finger-print-mocking-server .

### 컨테이너 실행

docker run -d --name finger-print-mocking-server -p 8000:8000 finger-print-mocking-server

### 핑거프린트 API

- `[GET] /finger-print`
- 호출 시 150ms 대기
