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
RUN uv sync --system --no-dev

# Copy application code
COPY . .

CMD ["python", "app.py"]
