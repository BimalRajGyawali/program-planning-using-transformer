import unittest


# Code as per student's plan which miss one edge case
# Generated by LLM, list index out of range as edge case is not handled
def reserve_seats(theater_hall, row, start_seat, num_seats):
    for i in range(len(theater_hall)):
        if num_seats == 1:
            if theater_hall[row][start_seat] == 1:
                return False
        else:
            for j in range(start_seat, start_seat + num_seats):
                if theater_hall[row][j] == 1:
                    return False

        for k in range(start_seat, start_seat + num_seats):
            theater_hall[row][k] = 0

    return True


class TestReserveSeats(unittest.TestCase):
    def test_multiple_seat_reservation_failure_not_enough_space(self):
        theater_hall = [
            [0, 0, 0, 0, 0],  # Row 0
            [0, 0, 0, 0, 0],  # Row 1
            [0, 0, 0, 0, 0],  # Row 2
            [0, 0, 0, 0, 0],  # Row 3
            [0, 0, 0, 0, 0]   # Row 4
        ]
        self.assertFalse(reserve_seats(theater_hall, 2, 2, 4))  # Not enough space at the end
        self.assertEqual(theater_hall, [
            [0, 0, 0, 0, 0],  # Row 0
            [0, 0, 0, 0, 0],  # Row 1
            [0, 0, 0, 0, 0],  # Row 2
            [0, 0, 0, 0, 0],  # Row 3
            [0, 0, 0, 0, 0]   # Row 4
        ])