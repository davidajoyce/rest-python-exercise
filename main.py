import sys
import rest_python as rp

def main():
	input_file = sys.stdin.readlines()
	rp.test_stdin_file(input_file)
	
	for line in input_file:
		URL = line.strip()
	
		if not rp.is_URL_valid(URL):
			sys.stdout.write(rp.json_object_false(URL))
			continue
	
		rp.test_get_request(URL)

		sys.stdout.write(rp.json_object_true(URL))

main()
