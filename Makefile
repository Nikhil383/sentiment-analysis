install:
	uv sync

cache:
	uv run src/save_hf.py

run:
	uv run gunicorn -w 4 -b 0.0.0.0:5000 app:app

test:
	uv run pytest -q
