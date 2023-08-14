import math

import pandas as pd
from flask import Flask, jsonify, render_template, request
import numpy as np

app = Flask(__name__)

# Read the .csv dataset
df = pd.read_csv('warsaw.csv')
df.info()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/weather', methods=['GET'])
def get_weather(data=df):
    # Drop the 'TMIN' and 'TMAX' columns from the dataframe
    filtered_df = data.drop(['TMIN', 'TMAX'], axis=1)
    epsilon = 0.01  # to fix comparison of floats

    # Get the query parameters as kwargs
    kwargs = {
        'date': request.args.get('date', default=None, type=str),
        'temp_min': request.args.get('temp_min', default=None, type=float),
        'temp_max': request.args.get('temp_max', default=None, type=float),
        'due_to': request.args.get('due_to', default=None, type=str)
    }

    # If no argument is provided, return the whole dataset
    if all(value is None for value in kwargs.values()):
        return jsonify(filtered_df.to_dict(orient='records'))

    # Filter the dataframe based on the provided arguments using kwargs
    if kwargs.get('date'):
        filtered_df = filtered_df[filtered_df['DATE'] == kwargs['date']]

    if kwargs.get('temp_min') is not None:
        temp_min = kwargs['temp_min']
        filtered_df = filtered_df[(filtered_df['TAVG'] >= temp_min - epsilon) | (filtered_df['TAVG'].isnull())]

    if kwargs.get('temp_max') is not None:
        temp_max = kwargs['temp_max']
        filtered_df = filtered_df[(filtered_df['TAVG'] <= temp_max + epsilon) | (filtered_df['TAVG'].isnull())]

    if kwargs.get('due_to'):
        due_to = kwargs['due_to']
        filtered_df = filtered_df[filtered_df['DATE'] <= due_to]

    # Convert the filtered data to JSON
    output = filtered_df.to_dict(orient='records')

    # Return the JSON data from the route
    return jsonify(output)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
