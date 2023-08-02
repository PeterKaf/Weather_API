import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Step 1: Read the .csv dataset
df = pd.read_csv('warsaw.csv')


# Step 2: Define routes that return data from the dataset
@app.route('/')
def home():
    return "Welcome to the Weather API!"


@app.route('/weather', methods=['GET'])
def get_weather():
    # Step 3: Convert the data to JSON
    data = df.to_dict(orient='records')

    # Step 4: Return the JSON data from the route
    return jsonify(data)


@app.route('/weather/date/<date>', methods=['GET'])
def get_weather_by_date(date):
    # Filter the dataframe based on the specified date
    filtered_df = df[df['DATE'] == date]

    # Convert the filtered data to JSON
    data = filtered_df.to_dict(orient='records')

    # Return the JSON data from the route
    return jsonify(data)


@app.route('/weather/station/<station_id>', methods=['GET'])
def get_weather_by_station(station_id):
    # Filter the dataframe based on the specified station ID
    filtered_df = df[df['STATION'] == station_id]

    # Convert the filtered data to JSON
    data = filtered_df.to_dict(orient='records')

    # Return the JSON data from the route
    return jsonify(data)


# Step 5: Run the app
if __name__ == '__main__':
    app.run(debug=True)
