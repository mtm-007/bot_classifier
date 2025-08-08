# bot_classifier
A bot classifier end to end model with FastAPI endpoint


#### uv as python package manager
pip install uv
uv python install 3.9
uv python pin 3.9
un venv
source .venv/bin/activate
uv pip install -r requirements.txt 


### API test

#### docker run

docker run --rm -p 5432:5432 \
  -e POSTGRES_USER=$DB_USER \
  -e POSTGRES_PASSWORD=$DB_PASSWORD \
  -e POSTGRES_DB=$DB_NAME postgres:latest


then : uvicorn src.main:app --reload


curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
  "text": "How am i doing in fastai course?.",
  "dialog_id": "0f2d4682-d939-4af6-beb9-880a5da202a2",
  "id": "b47c0c01-9dcb-4413-befc-9d36014079e9",
  "participant_index": 0
}'



