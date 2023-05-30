from django.test import TestCase
from Main.models import Proposal, Info
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


class ProposalModelTest(TestCase):
    def test_str_representation(self):
        proposal = Proposal.objects.create(name='Test Proposal')
        self.assertEqual(str(proposal), 'Test Proposal')


class InfoModelTest(TestCase):
    def test_str_representation(self):
        proposal = Proposal.objects.create(name='Test Proposal')
        info = Info.objects.create(text='Test Info', proposal_id=proposal)
        self.assertEqual(str(info), 'Test Info')
