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

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_init(self):
        self.assertEqual(self.new_pitch.title, "AI")

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        pitches = Pitch.query.all()
        self.assertTrue(len(pitches) > 0)
