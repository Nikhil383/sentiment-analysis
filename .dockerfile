FROM python:3.11-slim
WORKDIR /app

RUN pip install uv

COPY pyproject.toml ./pyproject.toml
COPY app ./app
COPY src ./src
COPY models ./models

RUN uv sync --no-cache

ENV MODEL_PATH=/app/models/hf_model
ENV HF_MODEL_NAME=distilbert-base-uncased-finetuned-sst-2-english
ENV TORCH_DEVICE=-1

CMD ["uv", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
