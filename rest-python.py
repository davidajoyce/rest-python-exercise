import sys
import requests

#test to make sure file contains a string to test for URL
def test_stdin_file(input_file):
	file_empty = test_file_empty(input_file)
	if file_empty:
		error_message_file_empty()

#check input file is not empty
def test_file_empty(input_file):
	if len(input_file) == 0:
		return True

# output error message to sterr
def error_message_file_empty():
	sys.stderr.write('input file has no URLs to check')

def test_URL(URL_check):
	check_http_s = check_https(URL_check)
	if not check_hhtp_s
		error_message_notURL()

#testing the get request to make sure receiving correct information
def test_get_request(input_file_line):

	request = get_request(input_file_line)
	status_code = get_status_code(request)
	content_length = get_content_length(request)
	Date = date_of_request(request)
	
	test_status_code(status_code)
	test_content_length(content_length)
	test_date(Date)

def get_request(input_file_line):
	request_get = requests.get(input_file_line)
	print request_get.content
	return request_get

def get_status_code(request):
	status_code = request.status_code
	print status_code
	return status_code


#main function for tests
def main():
	input_file = sys.stdin.readlines()
	test_stdin_file(input_file)

	for line in input_file:
		URL = line.strip()
		test_URL()		
		test_get_request(URL)




main()
	
