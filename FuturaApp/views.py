from django.shortcuts import render, redirect

from FuturaApp.forms import InternForm
from FuturaApp.models import Coding_question, Noncoding_question
from FuturaApp.models import Intern, Message, Result


# Create your views here.
def Index(request):
    form = InternForm()
    if request.method == 'POST':
        form = InternForm(request.POST)
        if form.is_valid():
            cod=form.save(commit=False)
            if cod.interested_field == 'Coding':
                form.save()
                return redirect('coding',cod.id)
            else:
                form.save()


    return render(request, 'Index.html',{'form':form})

def non_coding(request):
    data = Noncoding_question.objects.all()
    return render(request,'non_coding_question.html',{'data':data})

def coding(request,id):
    data = Coding_question.objects.all()

    if request.method == 'POST':

        for i in data:
            student_id = id
            ques_name = request.POST["question_name_"+str(i.id)]
            ques_ans = request.POST["question_ans_"+str(i.id)]
            Result.objects.create(student_id = student_id, ques_name = ques_name, ques_ans = ques_ans).save()
        return redirect('diagram')

    return render(request,'coding_question.html',{'data':data})


def contact(request):

    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]

        Message.objects.create(name = name, mail = email, phone = phone, content = content).save()

        return redirect('/#contact')

    else:
        return render(request, 'contact.html')

def diagram(request):
    data = Noncoding_question.objects.all()
    return render(request,'diagram.html',{'data':data})