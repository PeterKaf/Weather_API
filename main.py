import pandas as pd
from flask import Flask, jsonify, render_template, request
import datetime

app = Flask(__name__)

# Read the .csv dataset
df = pd.read_csv('warsaw.csv')
df['DATE'] = pd.to_datetime(df['DATE'])


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/weather', methods=['GET'])
def get_weather_data(data=df):
    # Drop the 'TMIN' and 'TMAX' columns from the dataframe
    filtered_df = data.drop(['TMIN', 'TMAX'], axis=1)
    epsilon = 0.01  # to fix comparison of floats

    # Get the query parameters as kwargs
    kwargs = {
        'date_start': request.args.get('date_start', default=None, type=str),
        'date_end': request.args.get('date_end', default=None, type=str),
        'temp_min': request.args.get('temp_min', default=None, type=float),
        'temp_max': request.args.get('temp_max', default=None, type=float),
        'month': request.args.get('month', default=None, type=str)
    }

    # If no argument is provided, return the whole dataset
    if all(value is None for value in kwargs.values()):
        return jsonify(filtered_df.to_dict(orient='records'))

    # Filter the dataframe based on the provided arguments using kwargs
    if kwargs.get('date_start'):
        date_start = datetime.datetime.strptime(kwargs['date_start'], '%Y-%m-%d')
        filtered_df = filtered_df[filtered_df['DATE'] >= date_start]

    if kwargs.get('date_end'):
        date_end = datetime.datetime.strptime(kwargs['date_end'], '%Y-%m-%d')
        filtered_df = filtered_df[filtered_df['DATE'] <= date_end]

    if kwargs.get('temp_min') is not None:
        temp_min = kwargs['temp_min']
        filtered_df = filtered_df[(filtered_df['TAVG'] >= temp_min - epsilon)]

    if kwargs.get('temp_max') is not None:
        temp_max = kwargs['temp_max']
        filtered_df = filtered_df[(filtered_df['TAVG'] <= temp_max + epsilon)]

    if kwargs.get('month'):
        month = kwargs['month']  # Get the value of the 'month' parameter
        filtered_df = filtered_df[filtered_df['DATE'].dt.month == int(month)]

    # Convert the filtered data to JSON
    output = filtered_df.to_dict(orient='records')
    # Return the JSON data from the route
    return jsonify(output)


# Run the app
if __name__ == '__main__':
    app.run()
