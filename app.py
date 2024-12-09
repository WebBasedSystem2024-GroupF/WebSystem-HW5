import os
import requests
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import threading
from model_utils import ModelUtils

load_dotenv()

app = Flask(
    __name__,
    static_folder='static',  # 정적 파일 저장 디렉토리
    static_url_path='/flask/static'  # 정적 파일 접근 경로
)

app.config['JSON_AS_ASCII'] = False

PLACE_API_KEY = os.getenv("PLACE_API_KEY")
GOOGLE_PLACE_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
GOOGLE_PLACE_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

model_utils = ModelUtils()

# 예제 라우트
@app.route('/flask')
def home():
    return jsonify({"message": "Flask server is running!"})


@app.route('/flask/api/place', methods=['POST'])
def get_place_details_with_name():
    # 사용자 입력 데이터
    data = request.get_json()
    place_name = data.get("place_name")
    location = data.get("location")  # {"lat": <위도>, "lng": <경도>}

    if not place_name:
        return jsonify({"error": "place_name is required"}), 400

    # Google Maps API에서 place_id 검색
    findplace_params = {
        "input": place_name,
        "inputtype": "textquery",
        "fields": "place_id",
        "key": PLACE_API_KEY,
    }
    if location:
        findplace_params["locationbias"] = f"circle:100@{location['lat']},{location['lng']}"

    findplace_response = requests.get(GOOGLE_PLACE_SEARCH_URL, params=findplace_params)

    if findplace_response.status_code == 200:
        findplace_data = findplace_response.json()
        if findplace_data.get("status") == "OK" and findplace_data.get("candidates"):
            place_id = findplace_data["candidates"][0].get("place_id")
        else:
            return jsonify({"error": "No place found", "details": findplace_data.get("status")}), 404
    else:
        return jsonify({"error": "Failed to fetch place_id", "status_code": findplace_response.status_code}), 500

    # Place ID로 상세 정보 요청
    details_params = {
        "place_id": place_id,
        "key": PLACE_API_KEY,
        "fields": "name,formatted_address,rating,user_ratings_total,price_level,opening_hours,website,formatted_phone_number,business_status,current_opening_hours,photos,reviews,url",
        "language": "ko"  # 한국어로 응답
    }
    details_response = requests.get(GOOGLE_PLACE_DETAILS_URL, params=details_params)

    if details_response.status_code == 200:
        details_data = details_response.json()
        if details_data.get("status") == "OK":
            return jsonify(details_data.get("result"))
        else:
            return jsonify({"error": details_data.get("status"),
                            "message": details_data.get("error_message", "Unknown error")}), 400
    else:
        return jsonify({"error": "Failed to fetch place details", "status_code": details_response.status_code}), 500


# Load the model in a separate thread
model_thread = threading.Thread(target=model_utils.load_model_and_data)
model_thread.start()


# 모델 가중치 계산
@app.route('/flask/api/scores', methods=['POST'])
def get_topic_weights():
    if not model_utils.model_loaded:
        return jsonify({"error": "Model is still loading, please try again later"}), 503

    user_input = request.json.get('text')
    if not user_input:
        return jsonify({"error": "No input text provided"}), 400

    topic_weights = model_utils.calculate_input_topic_weights(user_input)
    return jsonify({"topicScore": topic_weights})


if __name__ == "__main__":
    # 로컬에서 실행 시 호스트와 포트를 설정합니다.
    app.run(host='0.0.0.0', port=5000, debug=True)