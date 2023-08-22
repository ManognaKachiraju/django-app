from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Identity,furniture_complain
from django.contrib import messages
def index(request):
    return render(request,'index.html')

def hospital(request):
     return render(request,'hospital.html')


def shopping(request):
     return render(request,'shopping.html')
def refinery(request):
     return render(request,'refinery.html')
def canteen(request):
     return render(request,'canteen.html')
def school(request):
     return render(request,'school.html')
def transport(request):
     return render(request,'transport.html')
def furniture(request):
     return render(request,'furniture.html')
def office(request):
     return render(request,'office.html')
def others(request):
     return render(request,'others.html')


   # return HttpResponse("this is home page")
def about(request):
     return render(request,'about.html')
    #return HttpResponse("this is about page")
def services(request):
      return render(request,'services.html')
    #return HttpResponse("this is services page")
# def Identity(request):
#       return render(request,'Identity.html')
    
def identity_view(request):
      if request.method == "POST":
         name = request.POST.get('name')
         email = request.POST.get('email')
         phone = request.POST.get('phone')
         desc = request.POST.get('desc')

         identity=Identity(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
         identity.save()
         messages.success(request, "Your feedback has been recorded")
      return render(request,'identity.html')
   # return HttpResponse("This is contact page")
def township(request): 
     return render(request,'township.html')

def furniture(request):
    if request.method == 'POST':
        # Retrieve the form data from the request
        category = request.POST.get('category')
        reason = request.POST.get('reason')
        damaged = request.POST.get('damaged')

        # Process the form data as needed
        # Here you can perform any additional operations, such as saving the data to a database, sending an email, etc.
        furniture_complain=furniture_complain(category=category,reason=reason,desc=damaged,date=datetime.today())
        furniture_complain.save()
        messages.success(request, "Your feedback has been recorded")
        # For example, you can print the form data to the console
        print("Category:", category)
        print("Reason:", reason)
        print("Can it be repaired if damaged?", damaged)

        # You can also pass the form data to a template and render it
        context = {
            'category': category,
            'reason': reason,
            'damaged': damaged
        }

    # If the request method is not POST, render the form template
    return render(request, 'furniture.html')