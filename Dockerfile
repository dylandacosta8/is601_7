FROM python:alpine

WORKDIR /apps/qr

COPY . WORKDIR

RUN pip install --no-cache-dir -r requirements.txt

ENV QR_DATA_URL="https://github.com/dylandacosta8/is601_7"

ENTRYPOINT [ "python", "main.py" ]