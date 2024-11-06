# --------------------------------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : app.py 
# --------------------------------------------------------------------
# 모듈 로딩
from flask import Flask, render_template, request

# 모델 로드 관련 모듈 로딩
import os
import torch


# -------------------------------------------------------------
# Application 생성 함수
#  - 함수명: create_app
# -------------------------------------------------------------


def create_app():

    # flask web server 인스턴스 생성
    APP = Flask(__name__)


    # URL 처리 모듈
    from .views import main_view
    APP.register_blueprint(main_view.mainBP)


    return APP

    

# 조건부 실행
if __name__ == '__main__':

    app = create_app()
    app.run()

