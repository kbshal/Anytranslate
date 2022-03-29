FROM python:3.9 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
FROM python:3.9
WORKDIR /Anytranslate
COPY --from=requirements-stage /tmp/requirements.txt /Anytranslate/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /Anytranslate/requirements.txt
COPY . /Anytranslate
CMD ["gunicorn", "trans_api:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]
