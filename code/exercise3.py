# WRITE YOUR CODE HERE
def swap(dictionary):
    if any(isinstance(value, (list, dict, set)) for value in dictionary.values()):
        return "Cannot swap the keys and values for this dictionary"

    return {value: key for key, value in dictionary.items()}


# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : (4, 5)
  }

  swapped = swap(example_dict)
  print(swapped)