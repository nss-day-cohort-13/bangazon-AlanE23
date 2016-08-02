import csv
import random
import math
from birdyboard import *

class User:

  def __init__(self, name, handle):
    self.name = name
    self.handle = handle

    self.UID = math.floor(random.random()*100000)