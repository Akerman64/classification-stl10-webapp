FROM python:3.11-slim


ENV PYTHONUNBUFFERED=1
ENV CUDA_VISIBLE_DEVICES=1


WORKDIR /app


# Mise à jour
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*


# Installe les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000


CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]