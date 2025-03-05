1 Clone Repository

    git clone https://github.com/Anushkakesharwani/historical-monuments-bot
    cd historical-monuments-bot

2 Create & Activate Virtual Environment

    python -m venv venv
    venv\Scripts\activate

3 Install Dependencies

    pip install -r requirements.txt

4 Run FastAPI Server

    uvicorn app.main:app --reload

5 Test API

    Once running, open your browser and visit:
    http://127.0.0.1:8000/docs
