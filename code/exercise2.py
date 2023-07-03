# WRITE YOUR CODE HERE
def move_to_bottom(dictionary, key):
    if key in dictionary:
        value = dictionary.pop(key)
        dictionary[key] = value
        return dictionary
    else:
        return "The key is not in the dictionary"


# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 4)
  print(example_dict)