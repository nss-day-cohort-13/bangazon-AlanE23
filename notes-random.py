# # Random Notes for the Birdy Board Mastery Exercise

# # Users Storage Model, list containing randomly generated integer for UID and strings of the names
# [RandomGenUID1, 'Name', 'Handle']
# [RandomGenUID2, 'Name', 'Handle']
# [RandomGenUID3, 'Name', 'Handle']
# [RandomGenUID4, 'Name', 'Handle']
# [RandomGenUID5, 'Name', 'Handle']

# # Public Chirps Storage Model, list of strings and integers for the 2 different IDs and dict of list of comments on given message

# [ChirpID, UID, 'Public', 'Chirp Message', {Comments: ['comment 1', 'comment 2']]
# [ChirpID, UID, 'Public', 'Chirp Message', {Comments: ['comment 1', 'comment 2']]
# [ChirpID, UID, 'Public', 'Chirp Message', {Comments: ['comment 1', 'comment 2']]
# [ChirpID, UID, 'Public', 'Chirp Message', {Comments: ['comment 1', 'comment 2']]
# [ChirpID, UID, 'Public', 'Chirp Message', {Comments: ['comment 1', 'comment 2']]

# # Private Chirps Storage Model, list of strings and integers for the 2 different IDs

# [ChirpID, UID of author, 'Private', UID of receiver, 'Chirp Message']
# [ChirpID, UID of author, 'Private', UID of receiver, 'Chirp Message']
# [ChirpID, UID of author, 'Private', UID of receiver, 'Chirp Message']
# [ChirpID, UID of author, 'Private', UID of receiver, 'Chirp Message']
# [ChirpID, UID of author, 'Private', UID of receiver, 'Chirp Message']

# import csv

# ifile  = open('users.csv', "r")
# reader = csv.reader(ifile)

# rownum = 0
# for row in reader:
#     # Save header row.
#     if rownum == 0:
#         header = row
#     else:
#         colnum = 0
#         for col in row:
#             print('%-6s: %s' % (header[colnum], col))
#             colnum += 1

#     rownum += 1

# ifile.close()


##############################################

import unittest


class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_user_creation(self):
    user = User("Tractor Ryan", "tryan")
    self.assertEqual("Tractor Ryan", user.full_name)
    self.assertEqual("tryan", user.screen_name)
    self.assertIsNotNone(user.user_id)
    self.assertIsInstance(user, User)
    pass



if __name__ == '__main__':
    unittest.main()

###################################
import unittest


class TestConversation(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass




if __name__ == '__main__':
    unittest.main()

##################################
import unittest
import ConversationSingleton


class TestChirp(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_reply_public_chirp_creation(self):
    pass


  def test_new_public_chirp_creation(self):
    source = User("Arnold Swartzeneggar", "terminator")
    chirp = Chirp(
                  message="Hi everyone",
                  user=source.user_id,
                  private=False
                  )

    it_exists = ConversationSingleton.chirp_exists_in_conversation(chirp)

    self.assertTrue(it_exists)
    self.assertEqual(chirp.message, "Hi everyone")
    self.assertEqual(chirp.user_id, source.user_id)
    self.assertEqual(chirp.private, False)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)


  def test_private_chirp_creation(self):
    source = User("Arnold Swartzeneggar", "terminator")
    target = User("George Lucas", "hahajarjar")
    chirp = Chirp(
                  message="Hi everyone",
                  user=source.user_id,
                  private=True,
                  receiver=target.user_id
                  )
    self.assertIsInstance(chirp, Chirp)




if __name__ == '__main__':
    unittest.main()