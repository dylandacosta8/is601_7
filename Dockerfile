FROM python:alpine

WORKDIR /apps/qr

COPY . WORKDIR

ENV QR_DATA_URL="https://github.com/dylandacosta8/is601_7"

ENTRYPOINT [ "python", "main.py" ]