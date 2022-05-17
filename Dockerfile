FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /myPro

COPY . /myPro/

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /myPro

CMD [ "python", "/myPro/src/models/train_model.py" ]