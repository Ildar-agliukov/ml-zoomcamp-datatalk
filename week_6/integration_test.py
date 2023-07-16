import os
from datetime import datetime

import pandas as pd
from batch import get_input_path, get_output_path


def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)

def save_data(year = 2022, month= 1):
    S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL', 'http://localhost:4566')

    options = {
        'client_kwargs': {
            'endpoint_url': S3_ENDPOINT_URL
        }
    }

    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2), dt(1, 10)),
        (1, 2, dt(2, 2), dt(2, 3)),
        (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),     
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df_input = pd.DataFrame(data, columns=columns)

    input_file = get_input_path(year, month)

    df_input.to_parquet(
        input_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )


if __name__ == "__main__":
    year = 2022
    month = 1
    save_data(year, month)