import pandas as pd
import os

folder_path = '/Users/judith.rethmann/Downloads/FlightsData'

dataframes = []

for filename in os.listdir(folder_path):
    if filename.startswith('T_ONTIME_REPORTING') and filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        dataframes.append(df)

common_columns = set(dataframes[0].columns)
for df in dataframes[1:]:
    common_columns.intersection_update(df.columns)

common_columns = list(common_columns)
df_flight_data = pd.concat([df[common_columns] for df in dataframes], ignore_index=True)

df_flights_SFO_UA = df_flight_data[(df_flight_data['ORIGIN_CITY_NAME'] == 'San Francisco, CA') & (df_flight_data['OP_UNIQUE_CARRIER'] == 'UA') & (df_flight_data['CANCELLED'] == 0) & (df_flight_data['DIVERTED'] == 0)]

'''columns_to_keep = [
    'ORIGIN_CITY_NAME', 'ORIGIN_AIRPORT_ID', 'OP_UNIQUE_CARRIER', 'OP_CARRIER_FL_NUM',
    'FL_DATE', 'YEAR', 'MONTH', 'DAY_OF_MONTH', 'DAY_OF_WEEK', 'DEST_CITY_NAME',
    'DEST_AIRPORT_ID', 'AIR_TIME', 'DEP_TIME', 'DIVERTED', 'CANCELLED', 'DEP_DELAY',
    'DEP_DEL15', 'NAS_DELAY', 'CARRIER_DELAY', 'SECURITY_DELAY', 'WEATHER_DELAY'
]'''

columns_to_keep = [
    'ORIGIN_CITY_NAME', 'ORIGIN_AIRPORT_ID', 'OP_UNIQUE_CARRIER', 'OP_CARRIER_FL_NUM',
    'FL_DATE', 'YEAR', 'MONTH', 'DAY_OF_MONTH', 'DAY_OF_WEEK', 'DEST_CITY_NAME',
    'DEST_AIRPORT_ID', 'AIR_TIME', 'DEP_TIME', 'DEP_DELAY', 'DEP_DEL15'
]

df_flights_SFO_UA = df_flights_SFO_UA[columns_to_keep]

df_flights_SFO_UA.to_csv('/Users/judith.rethmann/Documents/MBS/PredictiveAnalytics/FlightData/flights_SFO_UA.csv', index=False)