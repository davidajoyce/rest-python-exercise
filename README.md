# rest-python-exercise
This is a python script that makes http (and https) requests to specified URLs and to report certain properties and reponses it receives

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Setup Virtual machine

Using a Windows operating system, you will need to setup a virtual linux machine.

Follow these instructions:

Download a virtual machine application from https://www.virtualbox.org/

Choose a Ubuntu 64 bit machine

Start the Ubuntu 64 bit machine

### Installing

This python script was developed using python 2.7.12, make sure the correct version is installed

Install the following python module using the following command line:

```
pip install requests
```

## Running the tests

To run the unit tests:

```
python validation_test.py
```

## Running the program:

To run the program with a text file input:

Enter the url strings in a newline separated .txt file:

```
http://www.bbc.co.uk/iplayer
https://google.com
bad://address
http://www.bbc.co.uk/missing/thing
```

Use the following command line:
```
cat input.txt | python main.py
```

If you would like to output to a file, run the following command line:
```
cat input.txt | python main.py >> results.txt
```
