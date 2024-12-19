# WebSystem-HW5
---
> **채팅 기반 음식점 추천 시스템 - Chatstaurant**

## 프로젝트 목적 및 주요 기능 설명

### 리뷰 텍스트 마이닝을 통한 맥락 기반 POI 추천 시스템 개발

- 사용자 리뷰의 텍스트 분석을 통해 POI (Points of Interest)의 특성을 모델링
- 맥락에 따른 POI의 특성을 시각적으로 분석할 수 있는 VA 시스템 개발
- 사용자가 직접 POI 데이터를 탐색하고 인사이트를 얻을 수 있도록 지원

## 필수 의존성 패키지와 설치 방법

### 설치 방법

1. Python 환경을 설정하고 의존성을 설치합니다:

```bash
pip install -r requirements.txt
```

2. `gensim` 라이브러리 설치 시 오류가 발생하면, `mingw-w64`를 [Mingw-w64](https://www.mingw-w64.org/downloads/)에서 다운로드하여 설치하고, `mingw-w64` bin 디렉토리를 시스템의 PATH 환경 변수에 추가합니다.

---

### 환경 변수 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음 내용을 추가합니다:

```dotenv
GOOGLE_MAP_KEY=[YOUR_KEY]
DATABASE_URL=[YOUR_DATABASE]
```

---

### 실행 방법

1. 프로젝트 루트 디렉토리로 이동한 후, 다음 명령어를 실행합니다:

```bash
flask run
```

2. 웹 브라우저에서 [http://127.0.0.1:5000](http://127.0.0.1:5000)로 접속합니다.

---

## 파일 및 디렉토리 구조 설명

```plaintext
project/
├── app.py                     # Flask 서버 애플리케이션
├── database_utils.py          # 데이터베이스 유틸리티 함수
├── model_utils.py             # 모델 유틸리티 함수
├── .env                       # 환경 변수 파일
├── requirements.txt           # 의존성 패키지 목록
└── README.md                  # 프로젝트 문서
```

### 각 파일 설명

- **`app.py`**: Flask 서버를 실행하여 웹 애플리케이션을 호스팅합니다.
- **`database_utils.py`**: 데이터베이스 작업을 위한 함수가 포함되어 있습니다.
- **`model_utils.py`**: 모델 작업을 위한 함수가 포함되어 있습니다.
- **`.env`**: `GOOGLE_MAP_KEY`와 `DATABASE_URL`과 같은 환경 변수를 저장합니다.
- **`requirements.txt`**: 의존성 패키지 목록.
- **`README.md`**: 프로젝트 문서.

---
