from django.shortcuts import render
from .models import Solution,solutionLike,Domain




# Create your views here.
def main(request):
    if request.method == 'POST':
        pass
    else:
        solutions = Solution.objects.all()
        context = {
            'solutions':solutions,
        }
        return render(request,'archive/main.html',context)