import pandas as pd
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Read the .csv dataset
df = pd.read_csv('warsaw.csv')


# Define routes that return data from the dataset
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/weather', methods=['GET'])
def get_weather():
    # Convert the data to JSON
    data = df.to_dict(orient='records')

    # Return the JSON data from the route
    return jsonify(data)


class DateAPI:
    @staticmethod
    @app.route('/weather/date/<date>', methods=['GET'])
    def get_weather_by_date(date):
        # Filter the dataframe based on the specified date
        filtered_df = df[df['DATE'] == date]

        # Convert the filtered data to JSON
        data = filtered_df.to_dict(orient='records')

        # Return the JSON data from the route
        return jsonify(data)

    @staticmethod
    @app.route('/weather/date/before/<date_before>', methods=['GET'])
    def get_weather_by_date_before(date_before):
        # Filter the dataframe based on the specified date
        filtered_df = df[df['DATE'] <= date_before]

        # Convert the filtered data to JSON
        data = filtered_df.to_dict(orient='records')

        # Return the JSON data from the route
        return jsonify(data)

    @staticmethod
    @app.route('/weather/date/after/<date_after>', methods=['GET'])
    def get_weather_by_date_after(date_after):
        # Filter the dataframe based on the specified date
        filtered_df = df[df['DATE'] >= date_after]

        # Convert the filtered data to JSON
        data = filtered_df.to_dict(orient='records')

        # Return the JSON data from the route
        return jsonify(data)

    @staticmethod
    @app.route('/weather/date/between/<date_after>/<date_before>', methods=['GET'])
    def get_weather_by_date_range(date_after, date_before):
        # Filter the dataframe based on the specified date range
        filtered_df = df[(df['DATE'] >= date_after) & (df['DATE'] <= date_before)]

        # Convert the filtered data to JSON
        data = filtered_df.to_dict(orient='records')

        # Return the JSON data from the route
        return jsonify(data)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
