from django.contrib import admin
from votes.models import Vote
# Register your models here.
# class VotesAdmin(admin.ModelAdmin):
#     fields = ['subject', 'vote_taken','ayes', 'nays']

admin.site.register(Vote)