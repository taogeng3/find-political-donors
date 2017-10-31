# Author
Tao Geng

# Language
Python 2.7.12

# Dependencies
from numpy import median

import datetime

import sys


# Approach summary
There is a single file called find_political_donors.py in src folder.

There are two global variables:
1. dic1: a dictionary to store information for processing medianvals_by_zip.txt file.
2. dic2: a dictionary to store information for processing medianvals_by_date.txt file.

There are totally four methods:
1. process_output1() method: to process a line of input data, and then output a line of medianvals_by_zip.txt file.
2. process2() method:  to process a line of input data for generating medianvals_by_date.txt file.
3. output2() method: to output medianvals_by_date.txt file.
4. main() method: to check the command-line arguments, open input and output files, perform process and output, and finally close input and output files.

The input file and two output files are initially opened, and the data in the input file is read line by line.

Data is extracted and processed line by line with process_output1() method (for medianvals_by_zip.txt file) and process2() method (for medianvals_by_date.txt file).

The medianvals_by_zip.txt file is outputted line by line with process_output1() method.

The medianvals_by_date.txt file is outputted line by line with output2() method.

Finally, the input file and output files are closed.


# Run instructions
Run the test with the following command from within the insight_testsuite folder:

insight_testsuite~$ ./run_tests.sh
