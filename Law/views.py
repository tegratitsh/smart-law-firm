from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Area, Title, Service, Contact, Member, Folder
from .forms import LoginForm,ContactForm, MeetingForm, AreaForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages


def law_user_signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse('Les deux mots de passe sont différents, Entrez deux mots de passe identique ')

        else:
            law_user = User.objects.create_user(
                username, password1, password2
            )
            law_user.save()

        return redirect('law-user-login')


    return render(request, 'Law/law_user_signup.html')

def law_user_login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('law-home')
        
        else:

            return HttpResponse('Nom d\'utilsateur ou mots de passe Incorrect !')

    return render(request, 'Law/law_user_login.html')


def law_user_logout_view(request):

    logout(request)

    return redirect('law-user-login')


 
def law_user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('law-home')
        
        else:
            messages.error(request, "Nom d'utlisateur ou mot de passe incorrect.")

           
    return render(request, 'Law/law_user_login.html')



def law_home_view(request):

    areas = Area.objects.all()
    titles = Title.objects.all()
    services = Service.objects.all()


    if request.method == 'POST':
        form = ContactForm(request.POST)  # Traiter les données du formulaire
        if form.is_valid():
            form.save()  # Enregistrer l'objet dans la base de données
            return redirect('law-home/')  # Rediriger après soumission réussie
    else:
        form = ContactForm()  # Afficher un formulaire vide
    
    

 
    context = {'areas':areas, 'titles':titles, 'services':services, 'form': form}

    print('le title', titles)

    return render(request, 'Law/index.html', context)


def law_contact_view(request):

    contacts = Contact.objects.all()
    titles = Title.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('law-area')  # Redirige vers une page de confirmation
    else:
        form = ContactForm()

    context = {"form": form, 'contacts':contacts, 'titles':titles, }

    return render(request, "Law/law_contact.html", context)


def law_contact_list_view(request):

    contacts = Contact.objects.all()
    titles = Title.objects.all()

    context = {'contacts':contacts, 'titles':titles}

    return render(request, 'Law/law_contact_list.html', context)



def law_area_view(request):

    areas = Area.objects.prefetch_related('title_set__service_set')
    titles = Title.objects.all()  # Précharger les relations pour optimiser la base de données
    context = {'areas': areas, 'titles':titles}

    return render(request,'Law/law_area.html', context)



def law_area_detail_view(request, area_id):



    area = get_object_or_404(Area, id=area_id)
    services = Service.objects.all()

    return render(request, 'Law/law_area_detail.html', {'area':area, 'services':services})

def law_title_detail_view(request, title_id):

    title = get_object_or_404(Title, id=title_id)
    titles = Title.objects.all()
    services = Service.objects.all()

    context = {'title':title, 'titles':titles, 'services':services}


    return render(request, 'Law/law_title_detail.html', context)



def law_team_view(request):


    members = Member.objects.all()
    areas = Area.objects.all()
    titles = Title.objects.all()

    context = {'members':members, 'areas':areas, 'titles':titles}


    return render(request, 'Law/law_team.html', context)







def law_case_view(request):

    # case : boite (notifications)



    contacts = Contact.objects.all()

    return render(request, 'Law/law_case.html', {'contacts':contacts})

def law_contact_management_view(request):

    # listes des contacts



    contacts = Contact.objects.all()

    return render(request, 'Law/law_contact_management.html', {'contacts':contacts})







def law_folder_view(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le rendez-vous dans la base de données
            return redirect('/')  # Redirige après la soumission
    else:
        form = FolderForm()
    return render(request, 'Law/law_folder.html', {'form': form})


def law_meeting_view(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le rendez-vous dans la base de données
            return redirect('law-home/')  # Redirige après la soumission
    else:
        form = MeetingForm()
    return render(request, 'Law/law_meeting.html', {'form': form})



def law_about_view(request):

    titles = Title.objects.all()
    context = {'titles':titles}

    return render(request, 'Law/law_about.html',context)




def smart_law_firm_view(request):

    pass



def law_folder_management_view(request):


    folders = Folder.objects.all()

    context = {'folders':folders}

    return render(request, 'Law/law_folder_management.html', context)



def law_file_manager_view(request):

    areas = Area.objects.all()
    titles = Title.objects.all()
    services = Service.objects.all()

    context = {'areas':areas, 'titles':titles, 'services':services}

    return render(request, 'Law/law_file_manager.html', context)


def law_edit_area_view(request, area_id):
    area = get_object_or_404(Area, id=area_id)  # Récupère l'élément à modifier
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES, instance=area)  # Formulaire pré-rempli
        if form.is_valid():
            form.save()  # Sauvegarde des modifications
            return redirect('law-file-manager')  # Redirection après sauvegarde
        else:
            print("Formulaire non valide :", form.errors) 
    else:
        form = AreaForm(instance=area)

    return render(request, 'Law/law_edit_area.html', {'form': form, 'area': area})



def law_edit_title_view(request, title_id):
    # Récupérer l'objet Title à modifier
    title = get_object_or_404(Title, id=title_id)
    areas = Area.objects.all()  # Récupérer toutes les options pour "area"
    services = Service.objects.all()
    
    if request.method == 'POST':
        # Mise à jour des champs du modèle
        area_id = request.POST.get('area')  # Obtenir l'ID de l'area du formulaire
        area = get_object_or_404(Area, id=area_id)
        title.area = area
        title.name = request.POST.get('name')  # Mettre à jour le champ "name"
        title.save()
        return redirect('law-home')  # Redirection après la sauvegarde (modifier selon vos besoins)
    
    # Envoyer les données au template
    context = {
        'title': title,
        'areas': areas,
        'services' : services,
    }
    return render(request, 'Law/law_edit_title.html', context)



def law_edit_service_view(request, service_id):
    # Récupérer le service spécifique à modifier
    service = get_object_or_404(Service, id=service_id)

    # Récupérer les titres disponibles (hérités du modèle Title)
    titles = Title.objects.all()
    
    if request.method == 'POST':
        # Mise à jour des champs du modèle Service
        title_id = request.POST.get('title')  # Champ hérité 'title'
        service.title = get_object_or_404(Title, id=title_id)
        service.name = request.POST.get('name')  # Champ 'name'
        service.save()  # Sauvegarder les modifications
        
        return redirect('law-file-manager')  # Redirection après la sauvegarde
    
    # Passer les données au template
    context = {
        'service': service,
        'titles': titles,
    }
    return render(request, 'Law/law_edit_service.html', context)
