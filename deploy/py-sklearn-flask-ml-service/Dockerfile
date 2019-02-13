FROM python:3.7-slim
WORKDIR /usr/src/app
COPY . .
EXPOSE 5000
RUN pip install pipenv
RUN pipenv install
ENTRYPOINT ["pipenv", "run", "python", "api.py"]