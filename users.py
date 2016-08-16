import uuid
import pickle
from chirp import *

class User:

  def __init__(self, name, handle):
    self.name = name
    self.handle = handle
    self.user_ID = uuid.uuid4()

