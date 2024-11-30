# WebSystem-HW5
---

## 프로젝트 목적 및 주요 기능 설명

### 리뷰 텍스트 마이닝을 통한 맥락 기반 POI 추천 시스템 개발

- 사용자 리뷰의 텍스트 분석을 통해 POI (Points of Interest)의 특성을 모델링
- 맥락에 따른 POI의 특성을 시각적으로 분석할 수 있는 VA 시스템 개발
- 사용자가 직접 POI 데이터를 탐색하고 인사이트를 얻을 수 있도록 지원

## 필수 의존성 패키지와 설치 방법

### 의존성
다음 패키지가 필요합니다:

- **Python 패키지**
  - Flask

- **JavaScript 라이브러리**
  - D3.js (CDN 사용)
  - Bootstrap (CDN 사용)

### 설치 방법

1. Python 환경을 설정하고 의존성을 설치합니다:

```bash
pip install flask
```

[//]: # (2. 프로젝트 디렉토리에 `DJI_data.csv`와 `edge.csv` 데이터를 `static/data` 폴더에 배치합니다.)

---

## app.py 실행 방법과 예상 출력물 설명

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
├── static/                    # 정적 파일 디렉토리
│   ├── css/                   # CSS 파일 디렉토리
│   │   └── styles.css         # 커스텀 스타일 시트
│   ├── data/                  # 데이터 파일 디렉토리
│   └── js/                    # JavaScript 파일 디렉토리
│       ├── 
│       └── 
└── templates/
    ├── index.html             # 메인 HTML 템플릿
    └── result.html            # 메인 HTML 템플릿
```

### 각 파일 설명

- **`app.py`**: Flask 서버를 실행하여 웹 애플리케이션을 호스팅합니다.
- **`templates/index.html`**: 메인 페이지의 HTML 레이아웃 파일.

---