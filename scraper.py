import requests
from bs4 import BeautifulSoup


def extract_movie_data_for_year(
        year: int,
) -> list:
    """Fetch the most popular movies in a given year

    Args:
        year (int): the year for which to fetch the most popular movies

    Returns:
        list: the most popular movies in the given year
    """
    url = f'https://www.google.com/search?q=popular+movies+in+{year}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    movies = []

    movie_elements = soup.find_all('div', class_='UnFsfe cyKJce ZvGeOb')

    for element in movie_elements:
        name = element.text.strip()

        movies.append(name)

    return movies



