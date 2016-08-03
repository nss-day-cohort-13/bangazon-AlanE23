import csv
import uuid
import pickle
from birdyboard import *

class User:

  def __init__(self, name, handle):
    self.name = name
    self.handle = handle
    self.user_UID = uuid.uuid4()



