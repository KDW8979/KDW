# --------------------------------------------------------------------
# Flask Framework에서 모듈 단위 URL 처리 파일
# - 파일명 : main_view.py
# --------------------------------------------------------------------
# 모듈 로딩 -----------------------------------------------------------
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

import torch
# from flask_utils import *


# Blueprint 인스턴스 생성
mainBP = Blueprint('MAIN',
                   import_name=__name__,
                   url_prefix='/',
                   template_folder='templates')



# 예측을 위한 모델 함수 (구현해야 함)
def predict(conversation):
    # 여기에 모델 예측 로직을 추가
    return "예측 결과"  # 예시로 반환

@mainBP.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)  # 요청 데이터 확인
        conversation = request.form.get('conversation')  # 안전하게 키를 가져오기
        if not conversation:
            print("conversation 키가 없습니다.")
            return render_template('index.html', error="대화를 입력해 주세요.")
        
        # 예측 수행
        prediction = predict(conversation)
        print("사용자가 입력한 대화:", conversation)
        
        # 예측 결과 페이지로 리다이렉트
        return redirect(url_for('MAIN.result', conversation=conversation, prediction=prediction))
    
    return render_template('index.html')

@mainBP.route("/result")
def result():
    conversation = request.args.get('conversation')
    prediction = request.args.get('prediction')
    return render_template('result.html', conversation_text=conversation, prediction_result=prediction)
