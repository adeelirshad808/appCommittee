from django.shortcuts import render,redirect
from app.models import *
from app.forms import CommitteeJoinForm
from datetime import datetime, timedelta

def committe_creator_payment(request):
    creator_payment_status = False
    print('committe_creator_paymen_running', )
    if request.method == 'POST':
        committeeJoinForm = CommitteeJoinForm(request.POST,request.FILES)
        if committeeJoinForm.is_valid(): 
            print('sliiiip',  committeeJoinForm.cleaned_data['participants_payment_slip'])
            committe_per_month = ([str(i.committee_amount_per_month) for i in Committee.objects.all()])
            committe_per_month = ('.'.join(str(x) for x in committe_per_month))
            participants_name = Profile.objects.get(user=request.user)
            participants_committee_name = Committee.objects.get()
            participants_paid_status = False
            participants_amount_paid = committe_per_month
            print('runnnnn')
            participants_payment_slip = committeeJoinForm.cleaned_data['participants_payment_slip']

            Participants.objects.create(
            participants_name=participants_name,
            participants_committee_name=participants_committee_name,
            participants_paid_status=participants_paid_status,
            participants_amount_paid=participants_amount_paid,
            participants_payment_slip =participants_payment_slip

            ) 
            print(('amount paid'))
            return redirect('index')

    else:
        committeeJoinForm = CommitteeJoinForm()
        if Participants.objects.filter(participants_name=Profile.objects.get(user=request.user)).exists():
            print('exist')
            payment_status = True
        else:
            print('not exsistsss')

            payment_status = False
    return render(request,'app/committe_creator_payment.html',{'committeeJoinForm':committeeJoinForm,'payment_status':payment_status} )