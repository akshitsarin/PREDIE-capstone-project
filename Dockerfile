FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

LABEL maintainer "akshitsarin99@gmail.com"

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]