FROM svizor/zoomcamp-model:mlops-3.10.0-slim

# Set a working directory
WORKDIR /app

# Copy Pipfile and Pipfile.lock
COPY Pipfile* /app/

# Install dependencies
RUN pip install pipenv && pipenv install --system --deploy

# Copy your script
COPY starter.py /app/
COPY yellow_tripdata_2022-04.parquet /app/

# Set the command to run your script
CMD ["python", "starter.py", "--year", "2022", "--month", "04"]