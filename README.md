## 설명

성능 테스트 시 실제 핑거프린트 외부 API 호출 시 호출량 제한 문제가 발생 -> 최대한 실제 환경과 비슷하게 하기 위하여 모킹 서버를 구성

## 실행 방법

### 이미지 빌드

`docker build -t finger-print-mocking-server .`

### 컨테이너 실행

`docker run -d --name finger-print-mocking-server -p 8000:8000 finger-print-mocking-server`

### 핑거프린트 API

- `[GET] /finger-print`
- 호출 시 200ms 대기
- finger print api 평균 응답 시간이 150ms, 여러 변수를 고려하여 200ms로 설정
  ![image](https://github.com/user-attachments/assets/5c597382-3cc8-421d-b3f0-66f7b322ca96)
