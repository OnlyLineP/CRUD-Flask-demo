# Dockerfile

#blabla
FROM python:3.10

#blablabla
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

#blablablabla
COPY . .
#WORKDIR .

#EXPOSE 8000

#runs the production server
#ENTRYPOINT ["python", "crudapp.py"]
#CMD ["flask run", "0.0.0.0:5000"]
CMD ["gunicorn", "--bind", "0.0.0.0", "app:app"]
