import unittest
import birdyboard
import chirp
import uuid
import pickle
import user

class TestChirp(unittest.TestCase):

  @classmethod

  def setUpClass(self):
    current_user = user.User('Test User', 'Test Handle')


  def test_public_chirp(self):
    public_chirp = chirp.Chirp(
                              author = current_user.user_ID,
                              message = 'Test Message',
                              private = False,

                              )


  # def test_new_public_chirp(self):
  #     new_public_chirp = Chirp(
  #                   message = 'Test Chirp',
  #                   user = uuid.uuid4(),
  #                   private = False,
  #                   chirp_UID = uuid.uuid4(),
  #                   test_receiver = receiver
  #                   )
  #     new_convo = convos.Convo(convo_UID)

  #     self.assertEqual(new_public_chirp.message, 'Test Chirp')
  #     self.assertEqual(new_public_chirp.private, False)
  #     self.assertIsNotNone(new_public_chirp.chirp_UID)
  #     self.assertIsNone(new_public_chirp.test_receiver)
  #     self.assertIsNotNone(new_convo)

  #   def test_reply_to_public_chirp(self):
  #     original_user = uuid.uuid4()
  #     original_chirp = Chirp(
  #                            message = 'Test Chirp',
  #                            author = original_user,
  #                            private = False,
  #                            chirp_UID = uuid.uuid4()
  #                            )
  #     original_convoUID = uuid.uuid4()
  #     original_convo = { original_convoUID: [ original_chirp.chirp_UID ] }

  #     replying_user = users.User(name, handle)
  #     chirp_back = Chirp(
  #                        message = 'Test Reply'
  #                       )

  #   def test_new_private_chirp(self):
  #     name = 'Test Name'
  #     handle = 'Test Handle'
  #     created_user = users.User(name, handle)
  #     receiver_uid = uuid.uuid4()
  #     chirp = Chirp(
  #                   message = 'Test Chirp',
  #                   user = created_user.user_UID,
  #                   private = True,
  #                   receiver = receiver_uid
  #                   )

if __name__ == '__main__':
    unittest.main()