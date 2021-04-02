from django.shortcuts import render
from rate_the_game_app.forms import UserForm, UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rate_the_game_app.models import Category, Game, Review
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

def index(request):
    return render(request, 'rate_the_game_app/index.html')

# def contact(request):
#     if request.method == "POST":
#         form = contactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#             body = {
#                 'first_name': form.cleaned_data['first_name'],
#                 'last_name': form.cleaned_data['last_name'],
#                 'email': form.cleaned_data['email_address'],
#                 'message': form.cleaned_data['message'],
#             }
#             message = "\n".join(body.values())
            
#             try:
#                 send_mail(subject,message,'admin@example,com',['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.') 
#             return redirect ("rate_the_game_app:index") 

#     form = contactForm()
#     return render(request, "rate_the_game_app/contact.html", {'form:':form})   
def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['hkheskani01@gmail.com']
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'rate_the_game_app/contact.html', {'form': form})


@login_required
def my_account(request):
    return render(request, 'rate_the_game_app/my_account.html')

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
                return redirect(reverse('rate_the_game_app:my_account'))
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


#User login_required() to ensure only those logged in can access
@login_required
def user_logout(request):
    #since we know user is logged in, we can log them out.
    logout(request)
    return redirect(reverse('rate_the_game_app:index'))
    
#list of categories page
def show_list(request):
    #refrence sent to html file to produce page with relevant information
    context_dict = {}
    category_list = Category.objects.all()
    context_dict['categories'] = category_list    
    return render(request, 'rate_the_game_app/list.html', context=context_dict)
    
def show_category(request, category_name_slug):
    #refrence sent to html file to produce page with relevant information
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        
        games = Game.objects.filter(category=category)
        
        context_dict['games'] = games
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['games'] = None
        
    return render(request, 'rate_the_game_app/category.html', context=context_dict)

def show_game(request, game_name_slug):
    #refrence sent to html file to produce page with relevant information
    context_dict = {}
    try:
        game = Game.objects.get(slug=game_name_slug)
        
        reviews = Review.objects.filter(game=game)
        
        context_dict['game'] = games
        context_dict['reviews'] = reviews
    except Game.DoesNotExist:
        context_dict['game'] = None
        context_dict['reviews'] = None
        
    return render(request, 'rate_the_game_app/game.html', context=context_dict)

@login_required   
def add_game(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None
    
    if category is None:
        return redirect('/rate_the_game_app/')
        
    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            if category:
                game = form.save(commit=False)
                game.category = category
                game.save()
                #redirect back to the category page were this game has been created
                return redirect(reverse('rate_the_game_app:show_category', kwargs={'category_name_slug': category_name_slug}))
            else:
                print(form.errors)
    context_dict = {'form':form, 'category':category}
    return render(request, '/rate_the_game_app/category/<slug:category_name_slug>/add_game/', context=context_dict)
    
@login_required   
def add_review(request, game_name_slug, user):
    try:
        game = Game.objects.get(slug=game_name_slug)
        user = UserProfile.objects.get(user=user)
    except:
        game = None
    
    if game is None:
        return redirect('/rate_the_game_app/')
        
    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            if category:
                review = form.save(commit=False)
                review.user = user
                review.name = game
                review.save()
                #redirect back to the game page were this review has been allocated
                return redirect(reverse('rate_the_game_app:show_game', kwargs={'game_name_slug': game_name_slug}))
            else:
                print(form.errors)
    context_dict = {'form':form, 'game':game,'user':user}
    return render(request, '/rate_the_game_app/category/<slug:category_name_slug>/<slug:game_name_slug>/add_review/', context=context_dict)