from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll, Choice, Answer
from django.db.models import Q
from django.utils.http import urlencode


class CreateAnswer(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return render(request, 'answer/create.html', context={'poll':poll})
    def post(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice_pk = int(request.POST.get('option5'))
        choice = get_object_or_404(Choice, pk=choice_pk)
        Answer.objects.create(
                poll=poll,
                choice=choice
        )
        return redirect('view', pk=poll.pk)