from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Solution,solutionLike,Domain
from .forms import SolutionModelForm,DomainModelForm
from django.db.models import Q
from users.models import Profile
from django.urls import reverse



# Create your views here.
def main_or_search(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'create_solution_form' in request.POST:
                profile = Profile.objects.get(user=request.user)
                solution_form = SolutionModelForm(request.POST or None)
                if solution_form.is_valid():
                    instance = solution_form.save(commit=False)
                    instance.author = profile
                    instance.save()
                    return redirect('archive:main_or_search')

            if 'create_domain_form' in request.POST:
                profile = Profile.objects.get(user=request.user)
                domain_form = DomainModelForm(request.POST or None)
                if domain_form.is_valid():
                    instance = domain_form.save(commit=False)
                    # instance.author = profile
                    instance.save()
                    return redirect('archive:main_or_search')
        else:
            return redirect('users:login')
    else:
        if 'domain' in request.GET and 'num' in request.GET:
            # print("//////")
            domain_query = request.GET['domain']
            number_query = request.GET['num']
            solutions = Solution.objects.filter(Q(domain=domain_query) & Q(number=number_query))
            domains = Domain.objects.all()
            # print(domains)
            solution_form = SolutionModelForm()
            domain_form = DomainModelForm()
            context = {
                'solutions':solutions,
                'domains':domains,
                'solution_form':solution_form,
                'domain_form':domain_form,
            }
            return render(request,'archive/main.html',context)
        else:
            # print("xxxxxxxxxx")
            solutions = Solution.objects.all()
            domains = Domain.objects.all()
            # print(domains)
            solution_form = SolutionModelForm()
            domain_form = DomainModelForm()
            context = {
                'solutions':solutions,
                'domains':domains,
                'solution_form':solution_form,
                'domain_form':domain_form,
            }
            return render(request,'archive/main.html',context)


def delete_solution(request,pk):
    if request.user.is_authenticated:
        try:
            obj = Solution.objects.get(pk=pk)
            if obj.author.user == request.user:
                obj.delete()
                return redirect(request.META['HTTP_REFERER'])
            else:
                return render(request,'home/error.html')
        except Solution.DoesNotExist:
            return render(request,'home/error.html')
    else:
        return redirect('users:login')


def edit_solution(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Solution.objects.get(pk=pk)
            if obj.author.user == request.user:
                if 'domain_submit_form' in request.POST:
                    domain_form = DomainModelForm(request.POST or None)
                    if domain_form.is_valid():
                        domain_form.save()
                        return redirect(request.META['HTTP_REFERER'])
                solution_form = SolutionModelForm(request.POST or None,instance=obj)
                if solution_form.is_valid():
                    solution_form.save()
                    return redirect('archive:main_or_search')
            else:
                return render(request,'home/error.html')
        else:
            try:
                obj = Solution.objects.get(pk=pk)
                if obj.author.user == request.user:
                    solution_form = SolutionModelForm(instance=obj)
                    domain_form = DomainModelForm()

                    context={
                        'solution_form':solution_form,
                        'domain_form':domain_form,
                    }
                    return render(request,'archive/edit_solution.html',context)

                else:
                    return render(request,'home/error.html')
            except Solution.DoesNotExist:
                return render(request,'home/error.html') 
    else:
        return redirect('users:login')
    # return render(request,'archive/edit_solution.html')
    