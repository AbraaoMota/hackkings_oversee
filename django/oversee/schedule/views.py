from django.shortcuts import render, redirect
from django.http import HttpResponse
from schedule.models import User, Availability, Calendar, Channel



def add_user(username):
	user, created = User.objects.get_or_create(name = username)
	#user.save()
       	
def index(request):
	#return render(request, "schedule/home.html")
	return redirect('home')
 # return HttpResponse("Hello, world. You can make a schedule here")

def home(request):
	if(request.GET.get('mybtn')):
		name = request.GET.get('username')
		print(name)
		add_user(name)
		context = {'username' : name}
		return render(request, "schedule/dashboard.html", context)
	return render(request, "schedule/home.html")

def dashboard(request):
	if(request.GET.get('new_channel')):
		return redirect('new_channel')

	return render(request, "schedule/dashboard.html")

def selectview(request):
   users  = User.objects.all() # use filter() when you have sth to filter ;)
   form = request.POST # you seem to misinterpret the use of form from django and POST data. you should take a look at [Django with forms][1]
   # you can remove the preview assignment (form =request.POST)
   if request.method == 'POST':
      selected_item = get_object_or_404(User, pk=request.POST.get('user_id'))
      # get the user you want (connect for example) in the var "user"
      #user.item = selected_item
      user = selected_item
      context = {'user' : user}
      return render(request, "schedule/new_channel.html", context)
      # Then, do a redirect for example
.t
   return render_to_response ('select/item.html', {'items':item}, context_instance =  RequestContext(request),)



def new_channel(request):
	return render(request, "schedule/new_channel.html")

def user_add_availability(request):
	return render(request, "schedule/")



# Testing:






# Create your views here.
