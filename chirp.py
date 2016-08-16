import uuid
import pickle
# import time
from birdyboard import *
from convo import *

class Chirp:

  def __init__(self, current_user, message, private=False, receiver=None):
    self.message = message
    self.author = current_user.user_ID
    self.chirp_ID = uuid.uuid4()
    self.private = private
    self.receiver = receiver
    # convo = Convo(self.chirp_ID)
    # Still trying to figure out when a conversation should be created