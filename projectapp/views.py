from django.shortcuts import render
from django.template import loader
# Create your views here.
from .corelate import get_corelation 
from django.http import HttpResponse
from .forms import InputForm , MyForm
import logging

def index(request):
  return HttpResponse("Hello Geeks")


 
# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()

   

    return render(request,"home.html", context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def responseform(request):
 #if form is submitted
     form = MyForm()
     if request.method == 'POST':
        
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            feild_val=myForm.cleaned_data['geeks_field']
            xcsv = myForm.cleaned_data['name']
            ycsv = myForm.cleaned_data['email']
            radio=myForm.cleaned_data['radio']
            #feedback = myForm.cleaned_data['feedback']
            corr=get_corelation('Total_number_of_students','Positive_cases')
            context = {
            'name': radio,
            'email': corr
            #'feedback': feedback
            }

            template = loader.get_template('thankyou.html')
            

            logging.debug("Log message goes here.")
            #returing the template
            return HttpResponse(template.render(context,request))



     else:
         form = MyForm()
     #returning form

     return render(request, 'responseform.html', {'form':form});