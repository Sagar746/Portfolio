from django.shortcuts import render

from .models import Project
from .models import Contact

from .forms import ContactForm
# Create your views here.

def home(request):
	projects=Project.objects.all()
	if request.method=='POST':
		form=ContactForm(request.POST or None)
		if form.is_valid():
			form.save()
	else:
		form=ContactForm()
	context={
		'projects':projects,
		'form':form
	}
	return render(request,'home.html',context)