import time

import unittest


def retry_on_exception(func):
    def wrapper(*args, **kwargs):
        delay = 5  # Default delay
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print("Request failed:", e)
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)

    return wrapper


class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(False)
