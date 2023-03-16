from django.db import models


class Proposal(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/proposals/')


class Info(models.Model):
    text = models.TextField(max_length=2000)
    proposal_id = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name='proposals')
