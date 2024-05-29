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
) -> int:
    """Extract the duration of the movie from the entry

    Args:
        entry (str): the entry from which to extract the duration

    Returns:
        int: the duration of the movie in minutes
    """
    duration_period = None
    duration_period_match = re.search(r"(\d{1})\xa0h (\d{1,2})\xa0min", entry)
    if duration_period_match:
        duration_period = (duration_period_match.group(1).strip(), duration_period_match.group(2).strip())
    else:
        duration_period_match = re.search(r"(\d{1})\xa0ore", entry)
        if duration_period_match:
            duration_period = (duration_period_match.group(1).strip(), "0")
    final_duration_period = int(duration_period[0]) * 60 + int(duration_period[1])
    return final_duration_period


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
    if "." in entry:
        return entry.split('.')[-1].strip()
    else:
        r = re.findall('([A-Z])', entry)[-1]
        for index in range(len(entry)-1, -1, -1):
            if entry[index] == r:
                return entry[index:]
