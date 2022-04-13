from django import forms
 
GEEKS_CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

CHOICES=[('select1','select 1'),
         ('select2','select 2')]
# creating a form
class InputForm(forms.Form):
 
    Usercsv = forms.FileField (label='Select a file')
    xvalue_csv = forms.CharField(max_length = 200)
    yvalue_csv = forms.CharField(max_length = 200)
    #roll_number = forms.IntegerField(
     #                help_text = "Enter 6 digit roll number"
      #               )
    #password = forms.CharField(widget = forms.PasswordInput())
    

class MyForm(forms.Form):
  
  radio = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
  #Usercsv = forms.FileField (label='Select a file')
  geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)
  days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])
  name = forms.CharField(label='Enter your name', max_length=100)
  email = forms.EmailField(label='Enter your email', max_length=100)
  #feedback = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))
  