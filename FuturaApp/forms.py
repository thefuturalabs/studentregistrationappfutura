from django import forms
from django.forms import RadioSelect

from FuturaApp.models import Intern, Coding_question, Message, Result

YEAR_CHOICES = [(str(year), str(year)) for year in range(2023,1990,-1)]
class InternForm(forms.ModelForm):
    year_of_passout = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(
        attrs={'class': 'year-dropdown'}))
    technologies = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(
        attrs={'class': 'checkbox-row'}),
        choices=[
            ("React Js", "React Js"),
            ("Digital Marketing", "Digital Marketing"),
            ("Data Science", "Data Science"),
            ("Mern Stack", "Mern Stack"),
            ("Flutter", "Flutter"),
            ("Python", "Python"),
            ("UI UX Designing", "UI UX Designing"),
            ("PHP(Laravel Framework)", "PHP(Laravel)"),
            (".NET", ".NET"),
            ("Dart", "Dart"),
            ("Django", "Django"),
        ])
    interested_field = forms.ChoiceField(widget=RadioSelect,choices=[('Coding', 'Coding'), ('Non-coding', 'Non-coding')])
    class Meta:
        model = Intern
        fields = ('name','location','completed_course','year_of_passout','college','mobile_no','technologies',
                  'interested_field')

    #class Quastion_Form(forms.Form):
        #student_id = forms.IntegerField()
        #question_no=forms.IntegerField()
        #result=forms.CharField(max_length=200)



# class coding_form(forms.ModelForm):
#     class Meta:
#         model = Coding_question
#         fields = ('status',)

class messageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ('name', 'mail', 'phone', 'content')

class resultForm(forms.ModelForm):
  class Meta:
    model = Result
    fields = ('student_id', 'ques_name', 'ques_ans')