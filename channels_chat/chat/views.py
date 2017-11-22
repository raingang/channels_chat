from django.shortcuts import render
from django.views import generic
from .forms import NameForm
from django.http import HttpResponseRedirect


def index(request):
	if 'username' in request.session:
		return render(request, 'index.html', )
	else: 
		if request.method == 'POST':
			form = NameForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				request.session['username'] = username
				return HttpResponseRedirect('/')

		else:
			form = NameForm()
		return render(request, 'register.html', {'form' : form})