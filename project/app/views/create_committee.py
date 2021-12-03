from django.shortcuts import render,redirect
from app.models import *
from app.forms import CommitteeCreationForm
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


#Custom function to find ending date of Committee

def Committe_ending_date(committee_month_period):
    date_after_month = datetime.today()+ relativedelta(months=committee_month_period)
    ending_date = date_after_month.strftime('%Y-%m-%d')
    return ending_date



def create_committee(request):
    print('create committee running...')
    if request.method == 'POST':
        if request.user.is_authenticated: 
            committee_creation_form = CommitteeCreationForm(data=request.POST)
            print('committee_creation_form data', committee_creation_form)
            if committee_creation_form.is_valid(): 
                committee_name = committee_creation_form.cleaned_data['committee_name']
                committee_members_limit = committee_creation_form.cleaned_data['committee_members_limit'] + 1
                committee_amount_per_month = committee_creation_form.cleaned_data['committee_amount_per_month']
                committee_month_period = committee_members_limit
                committee_amount_limit = committee_members_limit * committee_amount_per_month
                committee_starting_date = committee_creation_form.cleaned_data['committee_starting_date']
                committee_ending_date = Committe_ending_date(committee_members_limit)


                Committee.objects.create(
                    committee_creator = Profile.objects.get(user=request.user),
                    committee_name = committee_name,
                    committee_members_limit = committee_members_limit,
                    committee_amount_per_month =committee_amount_per_month ,
                    committee_month_period = committee_month_period,
                    committee_amount_limit = committee_amount_limit,
                    committee_starting_date = committee_starting_date,
                    committee_ending_date = committee_ending_date

                )
                print('committee created ') 
                return redirect('committe_creator_payment')
    else:
        committee_creation_form = CommitteeCreationForm()
        committees = Committee.objects.all()
        current_date = datetime.now().strftime('%Y-%m-%d')
    return render(request,'app/create_committee.html', {'committee_creation_form':committee_creation_form})