from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import Http404
from .forms import pasteFm      #import paste bin page's form
from .models import Pastebindb  #import database
import datetime
import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.forms import LoginForm
from users import urls

#my custom function 



# Create your views here.
def bin(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            fm = pasteFm(request.POST)
            if fm.is_valid():
                pst_nm = fm.cleaned_data['poster_name']
                pst_tp = fm.cleaned_data['poster_type']
                pst = fm.cleaned_data['poster']
                pst_url = str(uuid.uuid4())[:15]
                pst_dt = datetime.datetime.now()

                while Pastebindb.objects.filter(poster_url=pst_url):
                    pst_url = str(uuid.uuid4[:15])

                current_site = get_current_site(request)
                # print(current_site)
                user_posted_code_details = Pastebindb(
                    user=request.user.profile,
                    poster_name=pst_nm,
                    poster=pst,
                    poster_type=pst_tp,
                    poster_url = pst_url,
                    timestamp = pst_dt,
                )
                user_posted_code_details.save()
                context = {
                    'db_row':user_posted_code_details,
                    'current_site':current_site,
                    'active':'active',
                }
                return render(request,'pastebin/show.html',context)
                
        else:
            return HttpResponseRedirect('/user/login/')
            
    else :   
        fm = pasteFm()
        context = {
            'form':fm,
            'active':'active',
        }
        return render(request,'pastebin/bin.html',context)



def delete(request,id):
    if request.method == 'POST':
        fm = pasteFm(request.POST)
        if fm.is_valid():
            pst_nm = fm.cleaned_data['poster_name']
            pst_tp = fm.cleaned_data['poster_type']
            pst = fm.cleaned_data['poster']
            pst_url = str(uuid.uuid4())[:15]
            pst_dt = datetime.datetime.now()
            while Pastebindb.objects.filter(poster_url=pst_url):
                pst_url = str(uuid.uuid4[:15])


            user_posted_code_details = Pastebindb(
                user=request.user,
                poster_name=pst_nm,
                poster=pst,
                poster_type=pst_tp,
                poster_url = pst_url,
                timestamp = pst_dt,
            )
            user_posted_code_details.save()
            context = {
                'db_row':user_posted_code_details,
                'active':'active',
            }
            return render(request,'pastebin/show.html',context)
    else :
        fm = pasteFm()
        context = {
            'form':fm,
            'active':'active',
        }
        db_rw = Pastebindb.objects.get(pk=id)
        db_rw.delete()
    return render(request,'pastebin/bin.html',context)


def update_post(request,up_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_data = Pastebindb.objects.get(pk=up_id)
            if user_data.user.user == request.user:
                fm = pasteFm(request.POST,instance=user_data)
                if fm.is_valid():
                    fm.save()
                    user_data = fm.save()
                    user_data.save()
                    context={
                        'db_row':user_data,
                        'active':'active',
                    }
                    return render(request,'pastebin/show.html',context)
            else:
                return render(request,'home/error.html')
        else:
            return redirect('users:login')
    else :
        user_data = Pastebindb.objects.get(pk=up_id)
        fm = pasteFm(instance=user_data)
        context = {
            'form':fm,
            'active':'active',
        }
    return render(request,'pastebin/bin.html',context)

def show(request,rand_url):
    try:
        sharedCode = Pastebindb.objects.get(poster_url=rand_url)
        context={
            'sharedCode':sharedCode,
            'active':'active',
        }
        return render(request,'pastebin/shareCode.html',context)
    except Pastebindb.DoesNotExist:
        raise Http404("your link is Wrong or it is not available.Here")


def poster_details(request,pk):
    qs = Pastebindb.objects.get(pk=pk)
    current_site = get_current_site(request)
    context = {
        'db_row':qs,
        'current_site':current_site,
    }
    return render(request,'pastebin/poster_details.html',context)
