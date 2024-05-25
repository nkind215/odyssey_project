from fastapi import FastAPI, HTTPException
import json
from typing import List, Dict
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre
from scraper import fetch_movie_data_for_year  # Import the scraping function and Movie model

app = FastAPI()

def load_movies() -> Dict[int, List[Dict]]:
    """Load the movie data from a JSON file.

    Returns:
        Dict[int, List[Dict]]: The movie data with years as keys and lists of movies as values.
    """
    pass  # Add implementation here

def fetch_movie_data_for_year(year: int) -> List[Dict]]:
    """Fetch the most popular movies for a given year and extract detailed information.

    Args:
        year (int): The year for which to fetch the most popular movies.

    Returns:
        List[Dict]: A list of dictionaries containing detailed movie information.
    """
    pass  # Add implementation here

def save_movies(movies: Dict[int, List[Dict]]):
    """Save the movie data to a JSON file.

    Args:
        movies (Dict[int, List[Dict]]): The movie data to save.
    """
    pass  # Add implementation here

@app.get("/movies", response_model=Dict[int, List[Dict]])
def get_movies() -> Dict[int, List[Dict]]:
    """Retrieve all movies from the JSON file.

    Returns:
        Dict[int, List[Dict]]: The movie data with years as keys and lists of movies as values.
    """
    pass  # Add implementation here

@app.get("/movies/{year}", response_model=List[Dict])
def get_movies_by_year(year: int) -> List[Dict]]:
    """Retrieve movies for a specific year from the JSON file.

    Args:
        year (int): The year for which to retrieve movies.

    Returns:
        List[Dict]: A list of movies for the specified year.

    Raises:
        HTTPException: If movies for the specified year are not found.
    """
    pass  # Add implementation here

@app.post("/movies/{year}", response_model=List[Dict])
def add_movies_by_year(year: int) -> List[Dict]]:
    """Fetch and add movies for a specific year to the JSON file.

    Args:
        year (int): The year for which to fetch and add movies.

    Returns:
        List[Dict]: A list of newly added movies for the specified year.

    Raises:
        HTTPException: If movies for the specified year already exist.
    """
    pass  # Add implementation here

@app.put("/movies/{year}", response_model=List[Dict]])
def update_movie(year: int) -> List[Dict]]:
    """Update movies for a specific year in the JSON file.

    Args:
        year (int): The year for which to update movies.

    Returns:
        List[Dict]: A list of updated movies for the specified year.
    """
    pass  # Add implementation here

@app.delete("/movies/{year}/{name}", response_model=Dict)
def delete_movie(year: int, name: str) -> Dict:
    """Delete a movie for a specific year from the JSON file.

    Args:
        year (int): The year of the movie to delete.
        name (str): The name of the movie to delete.

    Returns:
        Dict: The deleted movie's details.

    Raises:
        HTTPException: If the movie for the specified year and name is not found.
    """
    pass  # Add implementation here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # You can access the API docs at http://localhost:8000/docs
