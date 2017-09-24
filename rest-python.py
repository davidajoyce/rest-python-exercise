import sys

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

#testing the get request to make sure receiving correct information
def test_get_request(input_file_line):

	request = get_request(input_file_line)
	status_code = get_status_code(request)
	content_length = get_content_length(request)
	Date = date_of_request(request)
	
	test_status_code(status_code)
	test_content_length(content_length)
	test_date(Date)


#main function for tests
def main():
	input_file = sys.stdin.readlines()
	test_stdin_file(input_file)
	for line in input_file:
		test_get_request(line)


main()
	
