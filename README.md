# Walmart Interview: Movie Theater Seating Challenge
Padma Gundapaneni

This program takes an input file of movie theater reservation requests and assigns seats to satisfy customers and maximize the number of occupied seats.

## Assumptions
This program is based on the following assumptions.
1. The theater has a layout of 10 rows with 20 seats in each row.
2. The theater requires a space of 3 seats between each group reservation.
3. Row J is farthest from the screen and row A is closest from the screen.
4. Customers prefer to sit as far from the screen as possible.
5. Customers who purchase tickets together prefer to sit together. Groups will not be split across rows.
6. Customers can reserve a maximum of 20 seats (1 row in the theater).
7. Customers cannot modify or cancel their reservation after making it.

## Getting Started
### Prerequisites
Python 3.8+ access from the terminal

### Installation
Clone the git repository and open it. Navigate to the `walmart-interview` folder.

### Input/Output Examples
Sample input and output can be found in ```test_data/input.txt``` and ```test_data/output.txt``` locations of this repository.

### Executing Program
Open your terminal window. The program takes in one command line argument, the input file location. For the input file location, you can use ```input.txt```. Run the following command from the `walmart-interview` directory.

```python3 movie_theater_seating.py input.txt```

### Executing Tests
To run the tests, from the `walmart-interview` directory, execute the following command in your terminal.

```python3 movie_theater_seating_test.py  ```
