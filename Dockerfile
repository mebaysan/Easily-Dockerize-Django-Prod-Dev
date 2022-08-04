FROM python:3.9
# enviroment

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip  

RUN make install

EXPOSE 8000  