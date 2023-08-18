# Weather Data API

This script provides a Flask API to retrieve weather data from a CSV file. It allows users to query the data based 
on date range and temperature range.

## Dataset

All credit goes to the original author of the dataset.

<b>Title:</b> Warsaw Daily Weather Dataset

<b>Author:</b> [Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/)

<b>Source:</b> [https://www.kaggle.com/datasets/mateuszk013/warsaw-daily-weather](https://www.kaggle.com/datasets/mateuszk013/warsaw-daily-weather)

<b>License:</b> [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/PeterKaf/Weather_API.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:

   ```
   python main.py
   ```
2. Check if you get following message:
    ```
    Running on http://127.0.0.1:5000 (Press CTRL+C to quit)   
    ```
3. Access the API endpoints:

   - Home page: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
   - Weather data: [http://127.0.0.1:5000/weather](http://127.0.0.1:5000/weather)

4. Query the weather data:

   - To retrieve the entire dataset, simply access the weather endpoint without any query parameters.
   - To filter the data, use the following query parameters:
     - `date_start`: Start date of the date range (format: YYYY-MM-DD)(inclusive)
     - `date_end`: End date of the date range (format: YYYY-MM-DD)(inclusive)
     - `temp_min`: Minimum temperature (inclusive)
     - `temp_max`: Maximum temperature (inclusive)
     - `month`: display only data from a specific month (format: MM)

   Example query: [http://127.0.0.1:5000/weather?date_start=2022-01-01&date_end=2022-01-31&temp_min=0&temp_max=10](http://127.0.0.1:5000/weather?date_start=2022-01-01&date_end=2022-01-31&temp_min=0&temp_max=10)

5. Check [Home](http://127.0.0.1:5000/) page for more details.
