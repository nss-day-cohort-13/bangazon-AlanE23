import csv
import uuid
import pickle
import datetime
from birdyboard import *
from users import *

class PublicChirps:

  def __init__(self, user, message):
    self.message = message
    self.author = user.user_UID
    self.chirp_UID = uuid.uuid4()
    time_stamp = datetime.datetime.utcnow()
    create_convo(self.chirp_UID)

