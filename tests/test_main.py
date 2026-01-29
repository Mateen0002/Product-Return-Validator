import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import io
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import validate_product_return   # type: ignore


class MockInput:
    """Mock input that prints prompts and returns values"""
    def __init__(self, values):
        self.values = iter(values)
        self.call_count = 0
    
    def __call__(self, prompt=""):
        value = next(self.values)
        print(prompt + value)
        self.call_count += 1
        return value


class TestValidateProductReturn(unittest.TestCase):

    @patch('builtins.input')
    @patch('return_validator.datetime')
    def test_valid_return_within_window(self, mock_datetime, mock_input):
        # Mock current date to be within 7 days of purchase
        mock_now = MagicMock()
        mock_now.date.return_value = datetime(2023, 8, 5).date()
        mock_datetime.now.return_value = mock_now
        mock_datetime.strptime = datetime.strptime
        mock_input.side_effect = MockInput(['Alex', 'Wireless Mouse', '08/01/23'])
        
        expected_output = (
            "Please enter the details to return the product.\n"
            "Enter your name:Alex\n"
            "Enter the product name:Wireless Mouse\n"
            "When did you purchase the product?\n"
            "Please enter the date in mm/dd/yy format:08/01/23\n"
            "Product:Wireless Mouse will be collected from the delivered address and amount:$25.99 will be returned to your account.\n"
            "Thank you.\n"
        )
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            validate_product_return()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input')
    @patch('return_validator.datetime')
    def test_return_window_exceeded(self, mock_datetime, mock_input):
        # Mock current date to be beyond 7 days
        mock_now = MagicMock()
        mock_now.date.return_value = datetime(2023, 8, 1).date()
        mock_datetime.now.return_value = mock_now
        mock_datetime.strptime = datetime.strptime
        mock_input.side_effect = MockInput(['Michael', 'USB-C Cable', '01/01/23'])
        
        expected_output = (
            "Please enter the details to return the product.\n"
            "Enter your name:Michael\n"
            "Enter the product name:USB-C Cable\n"
            "When did you purchase the product?\n"
            "Please enter the date in mm/dd/yy format:01/01/23\n"
            "Sorry! the product cannot be returned\n"
            "Thank you.\n"
        )
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            validate_product_return()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input')
    @patch('return_validator.datetime')
    def test_invalid_customer_product(self, mock_datetime, mock_input):
        mock_now = MagicMock()
        mock_now.date.return_value = datetime(2023, 8, 5).date()
        mock_datetime.now.return_value = mock_now
        mock_datetime.strptime = datetime.strptime
        mock_input.side_effect = MockInput(['John', 'Keyboard', '08/01/23'])
        
        expected_output = (
            "Please enter the details to return the product.\n"
            "Enter your name:John\n"
            "Enter the product name:Keyboard\n"
            "When did you purchase the product?\n"
            "Please enter the date in mm/dd/yy format:08/01/23\n"
            "You have not purchased that product recently with us.\n"
            "Thank you.\n"
        )
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            validate_product_return()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    @patch('builtins.input')
    @patch('return_validator.datetime')
    def test_sarah_laptop_stand_valid(self, mock_datetime, mock_input):
        # Mock current date to be within 7 days
        mock_now = MagicMock()
        mock_now.date.return_value = datetime(2023, 8, 15).date()
        mock_datetime.now.return_value = mock_now
        mock_datetime.strptime = datetime.strptime
        mock_input.side_effect = MockInput(['Sarah', 'Laptop Stand', '08/10/23'])
        
        expected_output = (
            "Please enter the details to return the product.\n"
            "Enter your name:Sarah\n"
            "Enter the product name:Laptop Stand\n"
            "When did you purchase the product?\n"
            "Please enter the date in mm/dd/yy format:08/10/23\n"
            "Product:Laptop Stand will be collected from the delivered address and amount:$45.50 will be returned to your account.\n"
            "Thank you.\n"
        )
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            validate_product_return()
            self.assertEqual(fake_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
