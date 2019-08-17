from django.shortcuts import render

# Create your views here.
from notes.models import Note
from utils.views import RegisterView


class NoteListView(RegisterView):
    model = Note
