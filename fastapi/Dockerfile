FROM python:3.12-alpine

ENV PLATFORM cloud

RUN pip install pipenv
RUN pip install python-jose[cryptography]

WORKDIR /app

ADD ./ /app

RUN pipenv install --system

EXPOSE 3000
# CMD ["fastapi", "run", "app.py", "--port", "3000"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]