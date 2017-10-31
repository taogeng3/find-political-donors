#!/usr/bin/env python

from numpy import median
import datetime
import sys

# A dictionary to store information for processing medianvals_by_zip.txt file.
dic1 = {}

# A dictionary to store information for processing medianvals_by_date.txt file.
dic2 = {}


# Process a line of input data, and then output a line of medianvals_by_zip.txt file.
def process_output1(line, output_file):
      data = line.split('|')
      if len(data) != 21:
        return

      cmte_id = data[0]
      zip_code = data[10]
      transaction_amt_str = data[14]
      other_id = data[15]

      if other_id:
        return
      if not cmte_id:
        return
      if not transaction_amt_str:
        return
      if len(zip_code) < 5:
        return

      transaction_amt = long(transaction_amt_str)
      key = cmte_id + '|' + zip_code[:5]
      if key in dic1:
        value = dic1[key]
        value[0].append(transaction_amt)
        running_median = long(round(median(value[0])))
        value[1] += 1
        value[2] += transaction_amt
        dic1[key] = value
        output_line = '|'.join([key, str(running_median), str(value[1]), str(value[2])]) + '\n'
        output_file.write(output_line)
      else:
        dic1[key] = [[transaction_amt], 1, transaction_amt]
        output_line = '|'.join([key, str(transaction_amt), '1', str(transaction_amt)]) + '\n'
        output_file.write(output_line)


# Process a line of input data for generating medianvals_by_date.txt file.
def process2(line):
      data = line.split('|')
      if len(data) != 21:
        return

      cmte_id = data[0]
      transaction_dt = data[13]
      transaction_amt_str = data[14]
      other_id = data[15]

      if other_id:
        return
      if not cmte_id:
        return
      if not transaction_amt_str:
        return
      if len(transaction_dt) != 8:
        return
      month = int(transaction_dt[:2])
      day = int(transaction_dt[2:4])
      year = int(transaction_dt[4:])
      try:
        key_date = datetime.date(year, month, day)
      except:
        return

      transaction_amt = long(transaction_amt_str)
      key = cmte_id + key_date.strftime('%Y%m%d')
      if key in dic2:
        value = dic2[key]
        value[0].append(transaction_amt)
        value[1] += 1
        value[2] += transaction_amt
        dic2[key] = value
      else:
        dic2[key] = [[transaction_amt], 1, transaction_amt]


# Output medianvals_by_date.txt file.
def output2(output_file):
  for key in sorted(dic2.iterkeys()):
    value = dic2[key]
    final_median = long(round(median(value[0])))
    output_line = '|'.join([key[:-8], key[-4:] + key[-8:-4],
                           str(final_median), str(value[1]), str(value[2])]) + '\n'
    output_file.write(output_line)


# The main method.
def main(argv = sys.argv):
  # Check the command-line arguments.
  if len(argv) != 4:
    print 'Wrong input.'
    print ('Usage: ./src/find_political_donors.py '
           './input/itcont.txt ./output/medianvals_by_zip.txt '
           './output/medianvals_by_date.txt')
    return

  # Open input and output files.
  input_file = open(argv[1])
  output_file1 = open(argv[2], 'w')
  output_file2 = open(argv[3], 'w')

  # Process and output.
  try:
    for line in input_file:
      process_output1(line, output_file1)
      process2(line)
    output2(output_file2)
  # Close input and output files.
  finally:
    input_file.close()
    output_file1.close()
    output_file2.close()


if __name__ == "__main__":
  main()
