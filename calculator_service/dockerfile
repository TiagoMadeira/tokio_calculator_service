FROM python:latest
WORKDIR /rest_service
COPY requirements.txt requirements.txt
RUN python3 -m venv .venv
RUN . .venv/bin/activate
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-u", "app.py" ]