FROM python:3.10-alpine

RUN apk add git && git clone https://github.com/VIadIen/Statistic.git Statisticsa
WORKDIR Statisticsa
RUN pip install -r requirements.txt


CMD ["uvicorn", "Statistic.main:app", "--host", "0.0.0.0", "--port", "80"]