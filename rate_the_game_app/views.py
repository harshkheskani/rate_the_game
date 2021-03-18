from django.shortcuts import render
from rate_the_game_app.forms import UserForm, UserProfileForm

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