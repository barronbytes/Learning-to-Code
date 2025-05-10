# Weather Data Analysis

This mini-project allowed me to use pandas for **exploratory data analysis (EDA)** with the following scenario:

> You are a data engineer at a Brazil-based weather prediction startup called Curu-Sight. The goal of this startup is to analyze **weather trends** in Brazil and predict the **output** of non-durable consumer goods at harvest time.

> One major threat (barring tariffs) to Brazil's biggest export, coffee, is **leaf rust**. This fungus thrives in humid environments and causes plants to wither. Your company recently won a contract with the local government of Minas Gerais to analyze how humidity (and auxiliary measures) determine the yearly output of coffee.

> You will analyze a dataset that contains averages calculated based on rainfall, temperature, humidity, and wind metrics collected during the coffee growing season. You will also analyze a dataset that contains Minas Gerais' crop output. You will then combine these two datasets to explore how the weather influences coffee growth.

## Prerequisites

Before running this project locally, ensure you ahve the following installed:

* IDE (VS Code, PyCharm, etc.)
* Instally Python 3.10+ version > for type hinting compatability
* Install pandas and matplotlib: `pip install pandas matplotlib`

## Lessons Learned

I learned to do the following with CSV data:

* Concatenate datasets with identical columns > `explore_weather.ipynb` > create new CSV file > `data/weather/weather_data.csv`
* Merge datasets with different columns > `analysis.ipynb`
* Clean data > remove null value rows
* Filter data > select based upon criteria
* Use pandas for visualiztaions > line plots, histograms
* Calculate and interpret Pearson correlation coefficients

The following cutoffs were used to interpret Pearson numbers:

| Value(s) | Interpretation |
|:--------:|:--------------|
| 1 | Perfectly Positive |
| 0.7 | Strongly Positive |
| 0.4 | Moderately Positive |
| 0.1 | Weakly Positive
| 0 | None |
| -0.1 | Weakly Negative |
| -0.4 | Moderately Negative |
| -0.7 | Strongly Negative |
| -1 | Perfectly Negative | 

## Data Dictionary

Column descriptions for datasets:

**data/weather/weather_data**

This dataset describes yearly weather outcomes for the coffee-growing months of Minas Gerais. Only weather data from January through May is considered.

* year: Year on which metrics were calculated. 
* rain_max: Average maximum millimeters of rain.
* temp_avg: Average temperature in celsius.
* temp_max: Average maximum temperature in celsius.
* temp_min: Average minimum temperature in celsius.
* hum_max: Average maximum humidity in percentage.
* hum_min: Average minimum humidity in percentage.
* wind_max: Average maximum wind speed in meters per second.
* wind_avg: Average wind speed in meters per second.
* subdivision: Name of Brazilian sub-division (all should be Minais Gerais)

**data/crop/coffee_output**

This dataset describes yearly features related to the coffee harvest that begins in June and ends in September in Minas Gerais.

* country: Country where harvest occurs (all should be Brazil).
* subdivision: Name of sub-division (all should be Minais Gerais)
* type: Type of coffee bean
* 60kgs_bag: 60 kg bags of coffee beans harvested (million bags)
* year: Year of harvest
* nonbearing_trees: Amount of nonbearing coffee trees (million trees)
* bearing_trees: Amount of bearing coffee trees (million trees)
* nonbear_hectares: Hectares of nonbearing coffee trees (thousand hectares)
* bearing_hectares_per_hectare: Average number of bearing trees per hectare
* nonbearing_trees_per_hectare: Average number of non-bearing trees per hectare

## Jupyter Notebooks

There are three Jupyter notebooks with EDA findings:

* notebooks/explore_weather.ipynb
* notebooks/explore_coffee.ipynb
* notebooks/analysis.ipynb

## Credits & Additional Learning

[The Knowledge House](https://www.theknowledgehouse.org/) provided the project requirements and raw data for this project. Contributions are welcome! Feel free to submit a pull request to improve the project or opena issue to report any problems.
