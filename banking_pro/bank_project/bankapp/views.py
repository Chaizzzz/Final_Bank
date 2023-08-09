from django.shortcuts import render, redirect


# Create your views here.
def home_view(request):
    # if request.user.is_authenticated:
    #     return redirect('/bankingapp/final_page')
    return render(request,"index.html")


