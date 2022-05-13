import sys
import os

class MovieTheaterSeating():
    def __init__(self):
        self.num_rows = 10
        self.seats_per_row = 20
        self.available_seats = self.num_rows * self.seats_per_row
        self.seating_map = self.generate_theater_map()
        self.reservation_details = {}
        self.reservation_ids = set()

    def generate_rows(self):
        seats = []
        for i in range(0, self.seats_per_row):
            seats.append(i + 1)
        return seats

    def generate_theater_map(self):
        theater_map = {}
        letter = chr(ord('@') + self.num_rows + 1)
        for i in range(0, self.num_rows):
            theater_map[letter] = self.generate_rows()
            letter = chr(ord(letter) - 1)
        return theater_map

    def find_closest_row(self, num_seats_reserved):
        minimum_size = float('Inf')
        row_id = 'J'
        for id, row_seats in self.seating_map.items():
            if len(row_seats) - num_seats_reserved < minimum_size and len(row_seats) - num_seats_reserved >= 0:
                minimum_size = len(row_seats) - num_seats_reserved
                row_id = id
        return row_id

    def update_available_seats(self, row_id, num_seats_reserved):
        row_seats = self.seating_map[row_id]
        reserved = False
        if len(row_seats) > 0:
            if len(row_seats) == num_seats_reserved or len(row_seats) < num_seats_reserved + 3:
                for i in range(0, num_seats_reserved):
                    del row_seats[0]
            elif len(row_seats) >= num_seats_reserved + 3:
                for i in range(0, num_seats_reserved + 3):
                    del row_seats[0]
            reserved = True
        return reserved

    def print_reservation(self, row_seats, num_seats_reserved, row_id):
        result = ""
        if num_seats_reserved > len(row_seats):
            result = "Reservation cannot be made, not enough seats available"
        elif len(row_seats) > 0:
            for i in range(0, num_seats_reserved - 1):
                result += str(row_id) + str(row_seats[i]) + ' '
            result += str(row_id) + str(row_seats[num_seats_reserved - 1])
        return result

    def find_best_seats(self, num_seats_reserved, res_id):
        if num_seats_reserved > self.available_seats or num_seats_reserved > self.seats_per_row:
            raise Exception("Reservation cannot be made, too many seats requested")
        else:
            row_id = self.find_closest_row(num_seats_reserved)
            row_seats = self.seating_map[row_id]
            self.reservation_details[res_id] = self.print_reservation(row_seats, num_seats_reserved, row_id)
            reservation_made = self.update_available_seats(row_id, num_seats_reserved)
            if reservation_made:
                self.available_seats -= num_seats_reserved
            return str(self.reservation_details[res_id])

    def parse_input(self, file_path):
        res_list = {}
        with open(file_path, 'r') as f:
            reservations = f.read().split('\n')
        f.close()
        for res in reservations:
            res_split = res.split(' ')
            if len(res_split) > 2:
                raise Exception("Too many parameters")
            if len(res_split) < 2:
                raise Exception("Too few parameters")
            if res_split[1] == "" or res_split[1] == " " or not res_split[1].isnumeric():
                raise Exception("Number of seats requested is invalid")
            if int(res_split[1]) <= 0:
                raise Exception("Number of seats requested is less than or equal to 0")
            if res_split[0] == "" or res_split[0] == " " or res_split[0].isnumeric():
                raise Exception("Reservation ID is empty or invalid")
            if len(res_split) == 2:
                res_id = res_split[0]
                if res_id in self.reservation_ids:
                    raise Exception("Reservation already made")
                self.reservation_ids.add(res_id)
                num_seats_reserved = int(res_split[1])
                res_list[res_id] = num_seats_reserved
                self.find_best_seats(num_seats_reserved, res_id)
        self.write_output()

    def write_output(self):
        output_path = os.path.join(os.path.dirname(__file__), "test_data/output.txt")
        with open(output_path, 'w') as f:
            for res_id, res_seats in self.reservation_details.items():
                f.write(res_id + " " + res_seats + "\n")
        abs_path = os.path.abspath(output_path)
        print(abs_path)
        return abs_path

    def main(self):
        file_path = sys.argv[1]
        if len(sys.argv) > 2:
            raise Exception("Too many arguments provided")
        self.parse_input(file_path)

if __name__ == "__main__":
    MovieTheaterSeating().main()
