# WRITE YOUR CODE HERE
import json

def compare(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    len1 = len(data1)
    len2 = len(data2)

    if len1 > len2:
        return "Dictionary 1 is longer than dictionary 2"
    elif len2 > len1:
        return "Dictionary 2 is longer than dictionary 1"
    elif len1 == len2:
      if data1 == data2:
        return "The dictionaries are equal"
      else:
        return "Dictionary 1 and dictionary 2 have the same length"


# test code below
if __name__ == "__main__":
  import sys
  
  file1 = sys.argv[1]
  file2 = sys.argv[2]

  print(compare(file1, file2))
