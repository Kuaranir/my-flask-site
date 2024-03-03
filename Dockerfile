FROM python:3.10
COPY . .
EXPOSE 443
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
