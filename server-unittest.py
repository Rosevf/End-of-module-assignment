import unittest
from unittest.mock import patch, MagicMock
from server import Server


class TestServer(unittest.TestCase):
    def setUp(self):
        self.server = Server()

    def test_validate_print_option_valid(self):
        self.assertTrue(self.server.validate_print_option("screen"))
        self.assertTrue(self.server.validate_print_option("file"))

    def test_validate_print_option_invalid(self):
        self.assertFalse(self.server.validate_print_option("invalid_option"))

    def test_receive_dictionary_binary(self):
        # Mock the client and pickle_file
        mock_client = MagicMock()
        mock_pickle_file = MagicMock()

        # Mock the pickle.load function to return a sample dictionary
        with patch("builtins.open", create=True), \
                patch("pickle.load", return_value={"key": "value"}) as mock_pickle_load, \
                patch("socket.socket"):
            # Make the mock_pickle_file behave like a context manager
            mock_pickle_file.__enter__.return_value = mock_pickle_file
            # Set the return value of the makefile method of mock_client
            mock_client.makefile.return_value = mock_pickle_file

            self.server.receive_dictionary_binary(mock_client, "screen")

        mock_pickle_load.assert_called_once_with(mock_pickle_file)
        mock_client.makefile.assert_called_once_with('rb')

    def test_print_dictionary_screen(self):
        dictionary = {"key": "value"}
        with patch("builtins.open", create=True) as mock_open:
            self.server.print_dictionary(dictionary, "screen")
            self.assertEqual(mock_open.call_count, 0)  # Check that the file is not opened
            self.assertEqual(mock_open.write.call_count, 0)  # Check that nothing is written to the file
            # Test that the dictionary is printed to the screen
            self.assertTrue(mock_open.write.called_with(f"Recevied dictionary is : {dictionary}"))

    @patch("cryptography.fernet.Fernet")
    @patch("builtins.open", create=True)
    def test_receive_text_file_screen_no_encrypt(self, mock_open, mock_fernet):
        mock_client = MagicMock()
        data = b"Sample data"
        mock_client.recv.return_value = data
        key = "empty key"
        self.server.receive_text_file(mock_client, "screen", "no", key)
        # Check that Fernet.decrypt is not called since encryption is set to "no"
        self.assertEqual(mock_fernet.decrypt.call_count, 0)
        # Check that the data is printed to the screen
        self.assertTrue(mock_open.write.called_with(f"Recevied text content is : {data.decode()}"))
    

   
if __name__ == "__main__":
    unittest.main()
