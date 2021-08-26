from django.shortcuts import render
from . import forms

# Create your views here.
def feedback_view(request):
    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printing feedback info')
            print('Student Name:',form.cleaned_data['name'])
            print('Student Mail Id:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
                
                
         



    return render(request,'testapp/feedback.html',{'form':form})
