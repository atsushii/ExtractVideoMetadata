FROM python


WORKDIR /api
COPY . /api/

RUN apt-get update && apt-get install -y libmagic-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD [ "flask", "run", "-h", "0.0.0.0"]

