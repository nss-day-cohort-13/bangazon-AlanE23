import unittest
import birdyboard
import uuid
import users
import pickle

class TestBirdy(unittest.TestCase):
  @classmethod

  def test_setupClass(self):
    self.birdyboard = birdyboard.Birdyboard()

  def test_user_creation(self):
    # test read/write capabilities
    name = 'Test Name'
    handle = 'Test Handle'
    created_user = users.User(name, handle)

    self.assertEqual(created_user.name, 'Test Name')
    self.assertEqual(created_user.handle, 'Test Handle')
    self.assertIsNotNone(created_user.user_UID)

  def test_new_public_message(self):
    name = 'Test Name'
    handle = 'Test Handle'
    created_user = users.User(name, handle)
    chirp = Chirp(
                  message = 'Test Chirp'
                  user = created_user.user_UID
                  private = False
                  )

    self.assertEqual(chirp.message, 'Test Chirp')
    self.assertEqual(chirp.user_UID, created_user.user_UID)
    self.assertEqual(chirp.private, False)
    self.assertIsNotNone(chirp.chirp_id)

  def test_new_private_message(self):
    name = 'Test Name'
    handle = 'Test Handle'
    created_user = users.User(name, handle)
    receiver_uid = uuid.uuid4()
    chirp = Chirp(
                  message = 'Test Chirp'
                  user = created_user.user_UID
                  private = True
                  receiver = receiver_uid
                  )


if __name__ == '__main__':
    unittest.main()