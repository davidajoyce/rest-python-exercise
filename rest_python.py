import sys
import requests
import urllib2
import json

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
	if not check_hhtp_s:
		error_message_notURL()

#testing the get request to make sure receiving correct information
def test_get_request(input_file_line):
	request = get_request(input_file_line)
	status_code = get_status_code(input_file_line)
	content_length = get_content_length(input_file_line)
	Date = date_of_response(input_file_line)

def get_request(input_file_line):
	request_get = requests.get(input_file_line)
	return request_get

def get_status_code(input_file_line):
	request = get_request(input_file_line)
	status_code = request.status_code
	return status_code

def get_content_length(input_file_line):
	request = get_request(input_file_line)
	header = request.headers
	content_length = header.get('Content-length')
	return content_length
	
def date_of_response(input_file_line):
	request = get_request(input_file_line)
	header = request.headers
	date = header.get('Date')
	return date

def is_URL_valid(URL):
	try:
		urllib2.urlopen(URL)		
		return True
	except ValueError, ex:
		sys.stderr.write("This URL is not valid")	
		return False
	except urllib2.URLError, ex:
		sys.stderr.write("This URL is not valid")
		return False

	return is_URL

def json_object_true(URL):
	status_code = get_status_code(URL)
	content_length = get_content_length(URL)
	date = date_of_response(URL)
	json_object = json.dumps({"Url": URL, "Status_code": status_code, "Content_length": content_length, "Date": date}, indent=4)

	return json_object

def json_object_false(URL):
	json_object = json.dumps({"Url": URL, "Error": "invalid url"}, indent=4)

	return json_object






	
