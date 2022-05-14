import unittest
from app.models import Pitch,User,Comment

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_user = User(name = "kelly")
        self.new_pitch = Pitch(id = 1, title = 'AI', pitch_content = 'AI is the future. Get to learning', category = 'Inovation', upvote = 5, downvote = 0, user = self.new_user)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()

    