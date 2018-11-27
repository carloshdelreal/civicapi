from django.test import TestCase
from django.utils import timezone

from .models import Vote
form .serializers import VoteSerializer

class VoteModelTest(TestCase):""

class VoteSerializerTests(TestCase):

	"""docstring for VoteSerializerTests"""
	def test_serialization(self):
		time =timezone.now()
		vote = Vote.objects.create(
			subject = 'More Projects built in Django',
			ayes = 100,
			nays = 0,
			vote_taken = time,
		)
		serialized = VoteSerializer(vote).data
		assert vote.id == serialized['id']
		assert vote.subject == serialized['subject']
		assert vote.ayes == serialized['ayes']
		assert vote.nays == serialized['nays']


# Create your tests here.
