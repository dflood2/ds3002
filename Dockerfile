FROM python:3.8.0-buster

# Make directory for pipeline
WORKDIR /usr/local/ds_project1
COPY ds_project1 ./

#Install dependencies
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

# Run the application
CMD ["python3", "housing_ETL.py"]