FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

# Copy code and install runtime deps
COPY pyproject.toml uv.lock README.md ./ 
COPY src ./src
COPY scenarios ./scenarios

RUN pip install --no-cache-dir .

EXPOSE 9109
CMD ["python", "scenarios/invest/evaluator/src/server.py", "--host", "0.0.0.0", "--port", "9109"]
