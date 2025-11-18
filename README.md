# Sentiment Analysis

## Problem Statement
Classifying text as Positive, Neutral, or Negative is essential for applications like customer reviews, feedback analysis, and social media monitoring.
This project solves the problem of deploying a real-time sentiment analysis model with:

- A simple UI where users can enter text

- A REST API for programmatic predictions

- A Dockerized & reproducible environment

- Basic MLOps practices like metrics, CI tests, and modular code

## Tech Stack

Languages & Frameworks

- Python

- Flask

- HTML / Jinja2 templates

Machine Learning

- Hugging Face Transformers (DistilBERT)

- PyTorch

MLOps & DevOps

- Docker

- uv (Python package & environment manager)

- GitHub Actions (CI)

- Prometheus (metrics endpoint)

- pytest (unit tests)
  
Other Tools

- Gunicorn (production WSGI server)

- pyproject.toml for reproducible environments

## Live Demo

A live demo of the deployed app will be available soon.

## TO run locally

1. Clone the repository:

   git clone https://github.com/Nikhil383/sentiment-analysis.git
   cd sentiment-analysis

2. Install dependencies using uv:

   uv sync

If there is no requirements.txt, install the likely packages listed above with pip.

3. Download the pre-trained Hugging Face model:

   uv run src/save_hf.py

4. Run the Flask app:
  Development mode:
    uv run app/app.py
  Production mode:
    gunicorn -w 4 -b 0.0.0.0:8000 app.app:app
5. Open your browser and go to http://localhost:5000 (or http://localhost:8000 for production mode).

6.Test the API
   curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
     -d '{"text": "I love this project!"}'

## Key Learnings & Challenges

What I Learned

- How to serve ML models using Flask and create clean REST APIs

- Dockerizing ML applications for consistent deployment

- Managing Python environments reproducibly using uv + pyproject.toml

- Integrating CI workflows to automate testing and environment checks

- Creating modular ML inference pipelines

- Adding monitoring using Prometheus metrics

Challenges Faced

- Handling Hugging Face model download time and ensuring deterministic builds

- Adjusting Flask logic for version 3.x (removal of before_first_request)

- Passing Python modules correctly for pytest (fixing import issues)  
- Creating a clean UI + API experience for non-technical users

- Ensuring model loads only once to avoid performance overhead

## Improvements & Future Work

- Add MLflow experiment tracking

- Deploy to Render / Hugging Face Spaces

- Add Kubernetes or Docker Swarm deployment

- Add logging dashboard (Grafana)

- Add fine-tuned custom sentiment model

## Contributing

Contributions are welcome. Suggested steps:

1. Fork the repository
2. Create a feature branch: git checkout -b feature-name
3. Make changes and add tests if applicable
4. Open a pull request describing your changes

## Contact

For questions or help, open an issue or contact the repository owner: @Nikhil383
