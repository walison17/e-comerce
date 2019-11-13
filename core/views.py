from django.shortcuts import render
from .forms import ContactForm

from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.decorators import login_required





class Indexview(TemplateView):
    template_name = 'index.html'

#desse modo é precisa estar logado antes de acessar a pagina index
#index = login_required(Indexview.as_view())
#desse modo não precisa estar logad
index = Indexview.as_view()







@login_required
def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request,'contact.html', context)

