# WRITE YOUR CODE HERE
def is_nested(dictionary):
    for value in dictionary.values():
        if type(value) in (list, tuple, dict):
            return True
    return False


# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : [4, 5]
  }

  print(is_nested(example_dict))
