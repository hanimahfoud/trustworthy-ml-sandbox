FROM python:3.12-slim

WORKDIR /app

# Install Python dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project (app.py, core/, modules/, assets/, i18n*, etc.)
COPY . .

# Streamlit must serve on port 8501 (the only port HF Spaces allows for it)
EXPOSE 8501

# HF Spaces sets $PORT; default to 8501. Bind to 0.0.0.0 so it is reachable.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
