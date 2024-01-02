FROM python:3.10-bullseye as builder
RUN pip install poetry
COPY . .
RUN poetry build

FROM python:3.10-slim-bullseye
WORKDIR /app
COPY --from=builder dist/*.whl /app
RUN apt update && apt install graphviz -y
RUN pip install /app/*.whl

CMD ["diagram-as-code"]
