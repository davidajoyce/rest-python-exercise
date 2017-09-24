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


def main():
	input_file = sys.stdin.readlines()
	test_stdin_file(input_file)

main()
	
