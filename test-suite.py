import unittest
import birdyboard

class TestBirdy(unittest.TestCase):
  @classmethod

  def setupClass(self):
    self.birdyboard = birdyboard.BirdyBoard()

  def newUserAdded(self):
    # test on the length of the user object to ensure another one was successfully added

    pass

  def newPubMessage(self):
    # test on the length of the public message object to ensure another one was successfully added
    pass

  def newPrivMessage(self):
    # test on the length of the private message object to ensure another one was successfully added
    pass