import re


def extract_movie_type(
    entry: str,
) -> str:
    """Extract the type of the movie from the entry

    Args:
        entry (str): the entry from which to extract the type

    Returns:
        str: the type of the movie
    """
    movie_types = ['PG-13', 'Not Rated (USA)', 'NR', 'R', 'G']
    movie_type = "Unknown"
    
    for mt in movie_types:
        if mt in entry:
            movie_type = mt
            break
            
    return movie_type


def extract_duration_period(
    entry: str,
) -> tuple:
    """Extract the duration of the movie from the entry

    Args:
        entry (str): the entry from which to extract the duration

    Returns:
        tuple: the duration of the movie
    """
    duration_period = None
    duration_period_match = re.search(r"(\d{1})\xa0h (\d{1,2})\xa0min", entry)
    if duration_period_match:
        duration_period = (duration_period_match.group(1).strip(), duration_period_match.group(2).strip())
    else:
        duration_period_match = re.search(r"(\d{1})\xa0ore", entry)
        if duration_period_match:
            duration_period = (duration_period_match.group(1).strip(), "0")
    return duration_period


def extract_name(
    entry: str,
    movie_type="Unknown",
) -> str:
    """Extract the name of the movie from the entry
    
    Args:
        entry (str): the entry from which to extract the name
        movie_type (str): the type of the movie
        
    Returns:
        str: the name of the movie
    """
    if movie_type != "Unknown":
        name = entry.split(movie_type)[0].strip()
    else:
        name = re.search(r"^(.*?)(?=\d)", entry)
        if name:
            return name.group(0).strip()
    return name


def extract_genre(
    entry: str,
) -> str:
    """Extract the genre of the movie from the entry
    
    Args:
        entry (str): the entry from which to extract the genre
        
    Returns:
        str: the genre of the movie
    """
    # the genre is the last part of the entry
    genre = entry.split('.')[-1].strip()
    return genre
