import unittest
import birdyboard
import uuid
import users
import pickle

class TestBirdy(unittest.TestCase):

  @classmethod

  def setUpClass(self):
    name = 'Test Name'
    handle = 'Test Handle'

  def test_user_creation(self):
    created_user = users.User(name, handle)

    self.assertEqual(created_user.name, 'Test Name')
    self.assertEqual(created_user.handle, 'Test Handle')
    self.assertIsNotNone(created_user.user_ID)

if __name__ == '__main__':
    unittest.main()