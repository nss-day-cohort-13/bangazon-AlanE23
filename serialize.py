import pickle
from users import *
from public_chirps import *
from private_chirps import *
from convos import *


def serialize(filename, content):
  '''Serialization function that takes 2 arguements,
     the filename and the content to be serialized'''

  with open(filename, 'wb+') as file:
    pickle.dump(content, file)

def deserialize(filename, content):
  '''Serialization function that takes 2 arguements,
     the filename and the content to be serialized'''

  try:
    with open(filename, 'rb+') as file:
      content = pickle.load(file)

  except EOFError:
    content = {}