'''
Author: Padma Gundapaneni
Date: 5/13/2022
Description: This script generates movie theater seat assignments given
an input file with movie theater reservation requests.
@input_file     filepath to the txt file with the reservation requests
python3 movie_theater_seating.py input_file
'''

import sys
import os

class MovieTheaterSeating():
    """
    A class used to represent a movie theater.
    
    Attributes
    ----------
    num_rows : int
        The number of rows in the theater
    seats_per_row : int
        The number of seats per row in the theater
    space_between_res : int
        The amount of space (seats) needed between
        2 reservations
    available_seats : int
        The number of available seats in the theater
    seating_map : dict
        The layout of the theater
    reservation_details : dict
        The assigned seats for each reservation
    reservation_ids : set
        The unique ids of the reservations received

    Methods
    -------
    generate_rows()
        Generates a blank seating chart for each row in the theater
    generate_theater_map()
        Generates a blank theater seating chart with the names of the rows and
        the seat numbers
    find_closest_row(num_seats_reserved)
        Finds the closest row to the back of the theater where a reservation
        can be seated
    update_available_seats(row_id, num_seats_reserved)
        Makes a reservation for a group and removes those and neighboring seats
        (if applicable) from the available seats
    print_reservation(row_seats, num_seats_reserved, row_id)
        Generates the reservation details for a reservation request
    find_best_seats(num_seats_reserved, row_id)
        Finds the optimal seats for a reservation
    parse_input(file_path)
        Parses the input file with reservation requests
    write_output()
        Prints the filepath to an output file with all the reservation details
    main()
        Main function to generate the reservations
    """
    
    def __init__(self):
        """
        Parameters
        ----------
        num_rows : int
            The number of rows in the theater
        seats_per_row : int
            The number of seats per row in the theater
        space_between_res : int
            The amount of space (seats) needed between
            2 reservations
        available_seats : int
            The number of available seats in the theater
        seating_map : dict
            The layout of the theater
        reservation_details : dict
            The assigned seats for each reservation
        reservation_ids : set
            The unique ids of the reservations received
        """
        self.num_rows = 10
        self.seats_per_row = 20
        self.space_between_res = 3
        self.available_seats = self.num_rows * self.seats_per_row
        self.seating_map = self.generate_theater_map()
        self.reservation_details = {}
        self.reservation_ids = set()

    def generate_rows(self):
        """ Generates a blank seating chart for each row in the theater

        Parameters
        ----------
        None

        Returns
        -------
        seats : list
            A list of seat numbers for a row
        """
        seats = []
        for i in range(0, self.seats_per_row):
            seats.append(i + 1)
        return seats

    def generate_theater_map(self):
        """ Generates a blank theater seating chart with the names of the rows
        and the seat numbers

        Parameters
        ----------
        None

        Returns
        -------
        theater_map : dict
            A map of seat numbers by row ID
        """
        theater_map = {}
        # Get the capital letter ASCII character for the farthest row from the
        # screen
        letter = chr(ord('@') + self.num_rows)
        for i in range(0, self.num_rows):
            theater_map[letter] = self.generate_rows()
            letter = chr(ord(letter) - 1)
        return theater_map

    def find_closest_row(self, num_seats_reserved):
        """ Finds the closest row to the back of the theater where a
        reservation can be seated

        Parameters
        ----------
        num_seats_reserved : int
            The number of seats in the reservation request
        
        Returns
        -------
        row_id : int
            The ID of the row where the reservation can be seated
        """
        # Initialize the minimum space needed to seat the reservation to the
        # max possible value
        minimum_space = float('Inf')
        # Initialize the row to be seated in to the capital letter ASCII
        # character for the farthest row from the screen
        row_id = chr(ord('@') + self.num_rows)
        # For each set of row ID and seat numbers in the theater seating map
        for id, row_seats in self.seating_map.items():
            # If the number of available seats in the row minus the number
            # of seats requested is less than the minimum space needed to
            # seat the reservation
            # OR
            # If the number of available seats in the minus the number of seats
            # requested is equal to 0
            if (len(row_seats) - num_seats_reserved < minimum_space) and \
                (len(row_seats) - num_seats_reserved >= 0):
                # Set the minimum space needed to seat the reservation to the
                # difference between the number of available seats in the row
                # minus the number of seats requested
                minimum_space = len(row_seats) - num_seats_reserved
                # Set the row ID equal to the this row's ID
                row_id = id
        # Return the row ID
        return row_id

    def update_available_seats(self, row_id, num_seats_reserved):
        """ Makes a reservation for a group and removes those and neighboring
        seats (if applicable) from the available seats
        
        Parameters
        ----------
        row_id : int
            The ID of the ideal row to seat the reservation
        num_seats_reserved : int
            The number of rows in the reservation request
        
        Returns
        -------
        reserved : bool
            True if there is enough space for the reservation and the request
            is fulfilled
            False if there is not enough space for the reservation to be
            fulfilled
        """
        # Get the available seats in this row
        row_seats = self.seating_map[row_id]
        # Mark the request as not yet fulfilled
        reserved = False
        # If there is at least one available seat in the row
        if len(row_seats) > 0:
            # If the number of available seats in the row equals the number of
            # seats requested is less than the number of seats requested plus
            # the required seats between reservations
            if len(row_seats) == num_seats_reserved or len(row_seats) < \
                num_seats_reserved + self.space_between_res:
                # Mark the seats as occupied
                for i in range(0, num_seats_reserved):
                    del row_seats[0]
            # If the number of available seats in the row is greater than or
            # equal to the number of seats requested plus the required seats
            # between reservations
            elif len(row_seats) >= num_seats_reserved + self.space_between_res:
                # Mark the seats as occupied
                for i in range(0, num_seats_reserved + self.space_between_res):
                    del row_seats[0]
            # Mark the request as fulfilled
            reserved = True
        # Return the status of the request
        return reserved

    def print_reservation(self, row_seats, num_seats_reserved, row_id):
        """ Generates the reservation details for a reservation request

        Parameters
        ----------
        row_seats : list
            A list of the seat numbers reserved
        num_seats : int
            The number of seats requested
        row_id : str
            The row ID in which the reservation was made
        
        Returns
        -------
        result : str
            A string representing the reservation that was made
        """
        result = ""
        if num_seats_reserved > len(row_seats):
            result = "Reservation cannot be made, not enough seats available"
        elif len(row_seats) > 0:
            for i in range(0, num_seats_reserved - 1):
                # Concatenate the row ID and the seat number
                result += str(row_id) + str(row_seats[i]) + ' '
            result += str(row_id) + str(row_seats[num_seats_reserved - 1])
        return result

    def find_best_seats(self, num_seats_reserved, res_id):
        """ Finds the optimal seats for a reservation

        Parameters
        ----------
        num_seats_reserved : int
            The number of seats requested
        res_id : str
            The reservation ID associated with this reservation
        
        Raises
        ------
        Exception
            If the number of seats requested is more than the number of
            available seats in the theater or the number of seats requested is
            more than the number of seats in a row of the theater
        
        Returns
        -------
            res_details : str
            A string with the reservation details for this reservation ID
        """
        if num_seats_reserved > self.available_seats or num_seats_reserved > \
            self.seats_per_row:
            raise Exception("Reservation cannot be made, too many seats " + \
            "requested")
        else:
            # Find the optimal row to seat this request
            row_id = self.find_closest_row(num_seats_reserved)
            # Get the available seats in this row
            row_seats = self.seating_map[row_id]
            # Make the reservation for this request
            self.reservation_details[res_id] = \
                self.print_reservation(row_seats, num_seats_reserved, row_id)
            # Check whether or not the reservation was successful
            reservation_made = \
                self.update_available_seats(row_id, num_seats_reserved)
            # If the reservation is successful, subtract the seats requested
            # from the total number of available seats
            if reservation_made:
                self.available_seats -= num_seats_reserved
            # Get the reservation details for this reservation ID
            res_details = str(self.reservation_details[res_id])
            # Return the reservation details for this reservation ID
            return res_details

    def parse_input(self, file_path):
        """ Parses the input file with reservation requests

        Parameters
        ----------
        file_path : str
            The path to the txt file with the reservation requests
        
        Raises
        ------
        Exception
            If too many parameters are passed in for a reservation
            If too few parameters are passed in for a reservation
            If the number of seats requested in a reservation is invalid
            If the number of seats requested in a reservation is negative or 0
            If the reservation ID for a reservation is empty or invalid
            If there is a duplicate reservation ID
        
        Returns
        -------
        None
        """
        # Map of reservation ID to number of seats requested
        res_list = {}
        with open(file_path, 'r') as f:
            # Split the file on newlines
            reservations = f.read().split('\n')
        f.close()
        # For each reservation (line) in the file
        for res in reservations:
            # Split the reservation on the space (separating the reservation ID
            # from the requested number of seats)
            res_split = res.split(' ')
            if len(res_split) > 2:
                raise Exception("Too many parameters")
            if len(res_split) < 2:
                raise Exception("Too few parameters")
            if res_split[1] == "" or res_split[1] == " " or not \
                res_split[1].isnumeric():
                raise Exception("Number of seats requested is invalid")
            if int(res_split[1]) <= 0:
                raise Exception("Number of seats requested is " + \
                "less than or equal to 0")
            if res_split[0] == "" or res_split[0] == " " or \
                res_split[0].isnumeric():
                raise Exception("Reservation ID is empty or invalid")
            if len(res_split) == 2:
                res_id = res_split[0]
                if res_id in self.reservation_ids:
                    raise Exception("Reservation already made")
                self.reservation_ids.add(res_id)
                # Get the number of seats in the request
                num_seats_reserved = int(res_split[1])
                # Add the ID and number of seats requested to a map
                res_list[res_id] = num_seats_reserved
                # Find the best seats for this request
                self.find_best_seats(num_seats_reserved, res_id)
        # Generate the output file for this input file
        self.write_output()

    def write_output(self):
        """ Prints the filepath to an output file with all the reservation
        details

        Parameters
        ----------
        None

        Returns:
        abs_path : str
            The absolute path to the filepath of the output file with
            reservations
        """
        # Initialize the path to output the reservation details to
        output_path = os.path.join(os.path.dirname(__file__), 
        "test_data/output.txt")
        # Write to the file at this path
        with open(output_path, 'w') as f:
            # For each reservation ID and seats reserved
            for res_id, res_seats in self.reservation_details.items():
                # Add a new line with the reservation ID followed by their
                # seat information
                f.write(res_id + " " + res_seats + "\n")
        # Close the file when done writing
        f.close()
        # Get the absolute path for the output filepath
        abs_path = os.path.abspath(output_path)
        # Print the absolute path to the terminal
        print(abs_path)
        # Return the absolute path
        return abs_path

    def main(self):
        """ Main function to generate the reservations
        Parameters
        ----------
        None

        Raises
        ------
        Exception
            If more than 2 arguments are provided in the terminal
        
        Returns
        -------
        None
        """
        # The input file path is the second argument provided in the terminal
        file_path = sys.argv[1]
        # If there are more than 2 arguments provided
        if len(sys.argv) > 2:
            raise Exception("Too many arguments provided")
        # Parse the input for the input file
        self.parse_input(file_path)

if __name__ == "__main__":
    MovieTheaterSeating().main()
