import pickle

def serialize(filename, content):
  '''Serialization function that takes 2 arguements,
     the filename and the content to be serialized'''

  with open(filename, 'wb+') as file:
    pickle.dump(content, file)

def deserialize(filename, content):
  '''Serialization function that takes 2 arguements,
     the filename and the content to be deserialized'''

  try:
    with open(filename, 'rb+') as file:
      content = pickle.load(file)

  except EOFError:
    content = {}

  return content