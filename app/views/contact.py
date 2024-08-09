from django.shortcuts import render, redirect
from django.views import View

from ..forms import ContactForm


class ContactView(View):
    def get(self,request):

        return render(request=request, template_name='contact.html')
    
    def post(self, request):

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home_page')
        return render(request=request, template_name='contact.html',context={'form':form})
      