# Odyssey Project

The Odyssey Project is a movie recommendation system built with Python Fastapi. It involves web scraping, data processing, data storage, API creation, and testing.

## Project Description

The Odyssey Project is designed to provide movie recommendations by scraping popular movie data from Google Search, processing this data for consistency, and storing it in a JSON file. An API is created to interact with this data, allowing users to retrieve, add, update, and delete movie records.

## Installation

1.	Create a new environment for your project.
2.	Install the dependencies listed inside requirements.txt:
   `pip install -r requirements.txt`

## Running the Project

In order to run the project type into your terminal: `python api.py`. You can also open api.py file and press Run in your IDE.

## File Structure
odyssey_project/
├── README.md
├── requirements.txt
├── scraper.py
├── data_processing.py
├── api.py
├── test_data_processing.py
└──data_storage/
    └── movies.json
