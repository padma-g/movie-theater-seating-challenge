import unittest
from pathlib import Path
from movie_theater_seating import MovieTheaterSeating

THIS_DIR = Path(__file__)

class TestMovieTheaterSeating(unittest.TestCase):
    def setUp(self):
        self.movie_theater = MovieTheaterSeating()
        self.parse_input_data = THIS_DIR.parent / 'test_data/test_parse_input'

    def test_generate_rows(self):
        generate_rows_expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = self.movie_theater.generate_rows()
        self.assertEqual(result, generate_rows_expected)
        
    def test_generate_theater_map(self):
        generate_theater_map_expected = {
            'J': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'I': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'H': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'G': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'F': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'E': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'D': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'B': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        }
        result = self.movie_theater.generate_theater_map()
        self.assertEqual(result, generate_theater_map_expected)
    
    def test_find_closest_row(self):
        result = self.movie_theater.find_closest_row(8)
        self.assertEqual(result, "J")
    
    def test_update_available_seats(self):
        result = self.movie_theater.update_available_seats('B', 2)
        self.assertEqual(result, True)
    
    def test_print_reservation(self):
        result1 = self.movie_theater.print_reservation([16, 17, 18, 19, 20], 3, 'B')
        result2 = self.movie_theater.print_reservation([16, 17, 18, 19, 20], 7, 'A')
        self.assertEqual(result1, "B16 B17 B18")
        self.assertEqual(result2, "Reservation cannot be made, not enough seats available")
    
    def test_find_best_seats(self):
        result1 = self.movie_theater.find_best_seats(9, "R001")
        result2 = self.movie_theater.find_best_seats(8, "R002")
        result3 = self.movie_theater.find_best_seats(5, "R003")
        self.assertEqual(result1, "J1 J2 J3 J4 J5 J6 J7 J8 J9")
        self.assertEqual(result2, "J13 J14 J15 J16 J17 J18 J19 J20")
        self.assertEqual(result3, "I1 I2 I3 I4 I5")

    def test_parse_input(self):
        with self.assertRaises(Exception):
            self.movie_theater.parse_input(self.parse_input_data / 'test_parse_input_1.txt')
        with self.assertRaises(Exception):
            self.movie_theater.parse_input(self.parse_input_data / 'test_parse_input_2.txt')
        with self.assertRaises(Exception):
            self.movie_theater.parse_input(self.parse_input_data / 'test_parse_input_3.txt')
        with self.assertRaises(Exception):
            self.movie_theater.parse_input(self.parse_input_data / 'test_parse_input_4.txt')
        with self.assertRaises(Exception):
            self.movie_theater.parse_input(self.parse_input_data / 'test_parse_input_5.txt')
        result6 = self.movie_theater.parse_input(self.parse_input_data / 'test_parse_input_6.txt')
        self.assertEqual(result6, None)
        with self.assertRaises(Exception):
            self.movie_theater.parse_input(self.parse_input_data / 'test_parse_input_7.txt')

    def test_write_output(self):
        result = self.movie_theater.write_output()
        self.assertEqual(result, str(THIS_DIR.parent.resolve() / "test_data/output.txt"))

if __name__ == '__main__':
    unittest.main()