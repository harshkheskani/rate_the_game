from django.shortcuts import render
from rate_the_game_app.forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def register(request):
    #boolean to tell template whether the registration worked
    #set false initially, change to true when successful
    registered = False
    
    #if its a HTTP POST, we wanna process the form data
    if request.method == 'POST':
        #try grab info from form, use both UserForm AND UserProfileForm
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        #if two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            #save users form data to database
            user = user_form.save()
            
            #Now we hash the password with the set method and update user object
            user.set_password(user.password)
            user.save()
            
            #now sort out UserProfile instance
            #need to set the user attribute ourselves
            #so set commit = False to delay saving the model until ready, for integrity
            profile = profile_form.save(commit=False)
            profile.user = user
            
            #Did user give a pic? if so then need to get it from form
            #and put it in UserProfile model
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            #now save UserProfile model instance
            profile.save()
            
            #update variable to show successful registration in template
            registered = True
            
        else:
            #invalid form(s) mistakes or otherwise? print problems
            print(user_form.errors, profile_form.errors)
            
    else:
        #Not a HTTP POST, so render form using 2 ModelForm instances.
        #These forms will be blank & ready for input
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 
                  'rate_the_game_app/register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})
    
def user_login(request):
    #if HTTP POST, try pull relevant info
    if request.method == 'POST':
        #Gather username & password from login form
        #We use request.POST.get('<variable>') instead of request.POST['<variable>']
        #because the former returns None if the value doesn't exist and the latter raises an error
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #use djangos machinery to see if username/password combo is valid
        #returns a user object if it is
        user = authenticate(username=username, password=password)
        
        #if we have user object-details are correct
        #if None, no user with credentials was found
        if user:
            #is account still active?
            if user.is_active:
                #if account is valid and active, log in and send to homepage
                login(request, user)
                return redirect(reverse('rate_the_game_app:index'))
            else:
                #inactive account - no log in!
                return HttpResponse("Your Rate>The>Game account is disabled.")
        else:
            #bad login details - no log in!
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    
    #no POST request so display login form.
    #this scenario would most likely be a HTTP GET
    else:
        #no context vars to pass
        return render(request, 'rate_the_game_app/login.html')

"""@login_required    
def restricted(request):
    return render(request, 'rango/restricted.html')"""


#User login_required() to ensure only those logged in can access
@login_required
def user_logout(request):
    #since we know user is logged in, we can log them out.
    logout(request)
    return redirect(reverse('rate_the_game_app:index'))