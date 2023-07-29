import unittest
from client import Client  

class TestValidationFunctions(unittest.TestCase):

    def test_validate_pickling_format_valid(self):
        client = Client()  # instance of the Client class
        valid_formats = ["binary", "json", "xml"]
        for format in valid_formats:
            result = client.validate_pickling_format(format)
            self.assertTrue(result, f"Expected '{format}' to be valid, but it is not.")

    def test_validate_pickling_format_invalid(self):
        client = Client()  # instance of the Client class
        invalid_formats = ["text", "yaml", "csv"]
        for format in invalid_formats:
            result = client.validate_pickling_format(format)
            self.assertFalse(result, f"Expected '{format}' to be invalid, but it is not.")

    def test_validate_encrypt_option_valid(self):
        client = Client()  # instance of the Client class
        valid_options = ["yes", "no"]
        for option in valid_options:
            result = client.validate_encrypt_option(option)
            self.assertTrue(result, f"Expected '{option}' to be valid, but it is not.")

    def test_validate_encrypt_option_invalid(self):
        client = Client()  # instance of the Client class
        invalid_options = ["true", "false", "encrypt", "decrypt"]
        for option in invalid_options:
            result = client.validate_encrypt_option(option)
            self.assertFalse(result, f"Expected '{option}' to be invalid, but it is not.")

if __name__ == '__main__':
    unittest.main()
