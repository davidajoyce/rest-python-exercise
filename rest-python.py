import sys

#test to make sure file contains a string to test for URL
def test_stdin_file(input_file):
	file_empty = test_file_not_empty()
	if file_empty:
		error_message()


def main():
	input_file = sys.stdin.readlines()
	test_stdin_file(input_file)

main()
	
