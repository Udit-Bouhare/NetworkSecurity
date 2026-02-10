FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update -y \
    && apt-get install -y awscli \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy dependency files first (better caching)
COPY pyproject.toml uv.lock ./

# Install dependencies using uv (system-wide)
RUN uv sync --no-dev --no-install-project

# Copy application code
COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

