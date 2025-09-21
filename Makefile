.PHONY: dev seed test


dev:
uvicorn app.main:app --reload


seed:
python seed.py


test:
pytest -q