import argparse
import pickle
import pandas as pd


def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', type=str)
    parser.add_argument('--month', type=str)
    args = parser.parse_args()
    year = args.year
    month = args.month

    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)

    categorical = ['PULocationID', 'DOLocationID']
    print('hear')
    df = read_data(f'yellow_tripdata_{year}-{month}.parquet')
    print('hear')
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    df['ride_id'] = f'{year}/{month}' + df.index.astype('str')
    df['y'] = y_pred

    print(df['y'].mean())

    # df_result = df[['ride_id', 'y']]

    # df_result.to_parquet(
    #     'df.parquet',
    #     engine='pyarrow',
    #     compression=None,
    #     index=False
    # )