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
                context = {'db_row':user_posted_code_details,'current_site':current_site}
                return render(request,'pastebin/show.html',context)
                
        else:
            messages.success(request,"Sign In to continue!!!")
            return HttpResponseRedirect('/user/login/')
            
    else :   
        fm = pasteFm()
        data = {'form':fm}
        return render(request,'pastebin/bin.html',data)



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


            #print('poster name ',pst_nm)
            #print('poster type ',pst_tp)
            #print('poster ',pst)
            #print('poster url :',pst_url)

            user_posted_code_details = Pastebindb(
                user=request.user,
                poster_name=pst_nm,
                poster=pst,
                poster_type=pst_tp,
                poster_url = pst_url,
                timestamp = pst_dt,
            )
            user_posted_code_details.save()
            data = {'db_row':user_posted_code_details}
            return render(request,'pastebin/show.html',data)
    else :
        fm = pasteFm()
        messages.info(request,"Code Deleted successfully!!!")
        data = {'form':fm}
        db_rw = Pastebindb.objects.get(pk=id)
        db_rw.delete()
    return render(request,'pastebin/bin.html',data)


def update_post(request,up_id):
    if request.method == 'POST':
        user_data = Pastebindb.objects.get(pk=up_id)
        fm = pasteFm(request.POST,instance=user_data)
        if fm.is_valid():
            fm.save()
            user_data = fm.save()
            user_data.save()
            messages.info(request,"Your Code is updated successfully!!")
            data={'db_row':user_data}
            return render(request,'pastebin/show.html',data)
    else :
        user_data = Pastebindb.objects.get(pk=up_id)
        fm = pasteFm(instance=user_data)
        data = {'form':fm}
    return render(request,'pastebin/bin.html',data)

def show(request,rand_url):
    try:
        sharedCode = Pastebindb.objects.get(poster_url=rand_url)
        context={'sharedCode':sharedCode}
        return render(request,'pastebin/shareCode.html',context)
    except Pastebindb.DoesNotExist:
        raise Http404("your link is Wrong or it is not available.Here")