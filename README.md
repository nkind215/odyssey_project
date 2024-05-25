# Odyssey Project

The Odyssey Project is a comprehensive movie recommendation system built with Python. It involves web scraping, data processing, data storage, API creation, and testing, all following clean code principles.

## Project Description

The Odyssey Project is designed to provide movie recommendations by scraping popular movie data from Google Search, processing this data for consistency, and storing it in a JSON file. An API is created to interact with this data, allowing users to retrieve, add, update, and delete movie records. The project includes comprehensive testing to ensure data integrity and code quality. All dependencies are managed in a virtual environment, and the project emphasizes clean code principles. Additionally, the scraping process is optimized with parallelization for efficiency.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/odyssey_project.git
    cd odyssey_project
    ```

2. **Create a Virtual Environment**
    ```bash
    python3.12 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. **Web Scraping**
    - Run the scraper script to collect movie data:
    ```bash
    python scraper.py
    ```

2. **Data Processing**
    - Run the data processing script to clean and standardize the movie data:
    ```bash
    python data_processing.py
    ```

3. **Start the API**
    - Run the API server:
    ```bash
    python api.py
    ```

## Testing the Project

1. **Run Tests with Tox**
    ```bash
    tox
    ```

## File Structure

```
odyssey_project/
├── README.md
├── requirements.txt
├── scraper.py
├── data_processing.py
├── api.py
├── test_data_processing.py
├── data_storage/
│   └── movies.json
└── venv/
```

## Dependencies

List all project dependencies in the `requirements.txt` file, including:
- BeautifulSoup
- Flask (or any other web framework you choose for the API)
- Tox (for testing)
- Any other libraries you use in your project

## Notes

- Follow clean code guidelines throughout the project.
- Ensure all functions and methods have appropriate docstrings.
- Handle exceptions and edge cases gracefully.

By following this structured approach, you will create a robust and maintainable movie recommendation system. Happy coding!
