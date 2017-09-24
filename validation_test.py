import rest_python
import unittest

class test_url_validation(unittest.TestCase):
	
	def test_check_valid_http(self):
		self.assertTrue(rest_python.is_URL_valid('https://google.com'))

	def test_check_invalid_http(self):
		self.assertFalse(rest_python.is_URL_valid('invalidURL'))

if __name__ == '__main__':
	unittest.main()
