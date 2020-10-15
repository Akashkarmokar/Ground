from django.shortcuts import render
from .forms import pasteFm      #import paste bin page's form
from .models import Pastebindb  #import database
import datetime
import uuid


#my custom function 



# Create your views here.
def bin(request):
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
        mesg = 'Your Code/Poster is Deleted'
        data = {'form':fm,'msg':mesg,}
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
            data={'db_row':user_data,'msg':'Code Updated',}
            return render(request,'pastebin/show.html',data)
    else :
        user_data = Pastebindb.objects.get(pk=up_id)
        fm = pasteFm(instance=user_data)
        data = {'form':fm}
    return render(request,'pastebin/bin.html',data)

def show(request):
    return render(request,'pastebin/show.html')