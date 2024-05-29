import unittest
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre


class TestMovieDataExtraction(unittest.TestCase):

    def test_extract_movie_type(self):
        """Function for testing the extract_movie_type function"""
        self.assertEqual(extract_movie_type('Top Gun 2PG-132\xa0h 10\xa0min.Acțiune'), 'PG-13')
        self.assertEqual(extract_movie_type('Decizia de a plecaNot Rated (USA)2\xa0h 18\xa0min.De comedie'), 'Not Rated (USA)')
        self.assertEqual(extract_movie_type('The Banshees of InisherinR1\xa0h 49\xa0min.De groază'), 'R')
        self.assertEqual(extract_movie_type('Unknown MovieG1\xa0h 30\xa0min.Dramă'), 'G')
        self.assertEqual(extract_movie_type('Another Movie2\xa0h 18\xa0min.De comedie'), 'Unknown')

    def test_extract_duration_period(self):
        """Function for testing the extract_duration_period function"""
        self.assertEqual(extract_duration_period('Top Gun 2PG-132\xa0h 10\xa0min.Acțiune'), 130)
        self.assertEqual(extract_duration_period('Decizia de a plecaNot Rated (USA)2\xa0h 18\xa0min.De comedie'), 138)
        self.assertEqual(extract_duration_period('Unknown MovieG1\xa0h 30\xa0min.Dramă'), 90)
        self.assertEqual(extract_duration_period('Short MovieR1\xa0oreAcțiune'), 60)

    def test_extract_name(self):
        """Function for testing the extract_name function"""
        self.assertEqual(extract_name('Top Gun 2PG-132\xa0h 10\xa0min.Acțiune', 'PG-13'), 'Top Gun 2')
        self.assertEqual(extract_name('Decizia de a plecaNot Rated (USA)2\xa0h 18\xa0min.De comedie', 'Not Rated (USA)'), 'Decizia de a pleca')
        self.assertEqual(extract_name('The Banshees of InisherinR1\xa0h 49\xa0min.De groază', 'R'), 'The Banshees of Inisherin')
        self.assertEqual(extract_name('Unknown MovieG1\xa0h 30\xa0min.Dramă', 'G'), 'Unknown Movie')
        self.assertEqual(extract_name('Another Movie2\xa0h 18\xa0min.De comedie'), 'Another Movie')

    def test_extract_genre(self):
        """Function for testing the extract_genre function"""
        self.assertEqual(extract_genre('Top Gun 2PG-132\xa0h 10\xa0min.Acțiune'), 'Acțiune')
        self.assertEqual(extract_genre('Decizia de a plecaNot Rated (USA)2\xa0h 18\xa0min.De comedie'), 'De comedie')
        self.assertEqual(extract_genre('The Banshees of InisherinR1\xa0h 49\xa0min.De groază'), 'De groază')
        self.assertEqual(extract_genre('Unknown MovieG1\xa0h 30\xa0min.Dramă'), 'Dramă')
        self.assertEqual(extract_genre('Another Movie2\xa0h 18\xa0min.Narațiune'), 'Narațiune')


if __name__ == '__main__':
    unittest.main()