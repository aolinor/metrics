FROM python:3

RUN pip3 install psutil

RUN mkdir -p app
WORKDIR /app
COPY . .

# RUN ls

ENTRYPOINT [ "python3", "./metrics.py"]
CMD []
