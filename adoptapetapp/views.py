from django.shortcuts import render,redirect
from django.contrib.auth.views import login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from . import models
from .templates.CommentObj import CommentObj

def editPet(request, editingPet):
    if request.method == "POST":
            name = request.POST.get('name',False)
            variety = request.POST.get('variety',False)
            gender = request.POST.get('gender',False)
            address = request.POST.get('address',False)
            weight = request.POST.get('weight',False)
            age = request.POST.get('age',False)
            description = request.POST.get('description', False)

            pet = models.Pet.objects.get(name = name)
            pet.name = name
            pet.gender = gender
            pet.variety = variety
            pet.address = address
            pet.weight = weight
            pet.age = age
            pet.description = description
            pet.save()
            return redirect('/adoptApetApp/details/' + pet.name)
    else:
        user = request.user
        if user.is_authenticated():
                pet = models.Pet.objects.get(name = editingPet)
                return render(request, 'editPet.html', {'pet': pet})
        else:
                return redirect('/adoptApetApp/')

def mypets(request):
    if request.user.is_authenticated():
        user = request.user
        pets = models.Pet.objects.filter(user=user)
        return render(request, 'mypets.html',{'pets':pets})
    else:
        return redirect('/adoptApetApp/')


def index(request):
    return render(request,"home.html")

def details (request,petname):

    p = models.Pet.objects.get(name = petname)

    return render(request,"viewDetailsOne1.html", {'pet': p})

def home (request):

    if request.method == "POST" and request.POST.get('user',False) != False:
        username = request.POST.get('user',False)
        password = request.POST.get('password',False)
        user = authenticate(username = username,password = password)
        print("1")

        if user is not None:
            login(request,user)

        else:
            pass

    elif request.method == "POST" and request.POST.get('user',False) == False:
        print("2")
        searchPet = request.POST.get('searchPet', False)
        if searchPet == "":
            pets = models.Pet.objects.all()
        else:
            pets = models.Pet.objects.filter(variety = searchPet)

        return render(request,"home.html",{'pets': pets})


    pets = models.Pet.objects.all()
    return render(request,"home.html",{'pets': pets})






def signUp (request):

    return render(request,"signUp.html")


def registerUsr (request):

    if request.method == "POST":
        username = request.POST.get('user',False)
        password = request.POST.get('password',False)
        fname = request.POST.get('fname',False)
        lname = request.POST.get('lname',False)
        email = request.POST.get('email',False)
        address = request.POST.get('address',False)
        city = request.POST.get('city',False)
        state = request.POST.get('state',False)
        zip_num = request.POST.get('zipnum',False)
        phone_number = request.POST.get('phone_number',False)

        user = User.objects.create_user(username,email,password)

        user.first_name = fname
        user.last_name = lname

        person = models.Person(user = user, first_name = fname, last_name = lname, address = address, city = city, state = state, zipnum = zip_num, phone_number = phone_number, email = email)
        person.save()
        user.save()
        login(request,user)




    return redirect("../adoptApetApp/")

def profile(request):

    if request.user.is_authenticated():
        user = request.user
        person = models.Person.objects.get(user = user)
        return render(request,"profile.html", {'username': user ,'fname': person.first_name, 'lname' : person.last_name, 'email': person.email, 'address': person.address, 'city': person.city, 'state': person.state, 'zipnum': person.zipnum, 'phonenum': person.phone_number})
    return render(request, "profile.html")

def createMessage(request):
    return render(request,"createMessage.html")

def dialogues(request,petname):
    print(petname)
    pet = models.Pet.objects.get(name = petname)
    try:
        CommentArr = []
        comment = models.Comment.objects.filter(pet = pet)
        for a in comment:
            usr = models.Person.objects.get(user = a.commenter)
            _commentObj = CommentObj(a.comment,usr.first_name)
            CommentArr.append(_commentObj)
        return render(request,"dialogues.html", {'comments': CommentArr})
    except models.Comment.DoesNotExist:
        comment = None
    return render(request,"dialogues.html")




def editProfile(request):

    if request.user.is_authenticated():
        if request.method == "POST":
            editUserName = request.POST.get('editUserName',False)
            edifFirstName = request.POST.get('edifFirstName',False)
            editLastName = request.POST.get('editLastName',False)
            editEmail = request.POST.get('editEmail',False)
            editAddress = request.POST.get('editAddress',False)
            editCity = request.POST.get('editCity',False)
            editState = request.POST.get('editState', False)
            editZipNum = request.POST.get('editZipNum', False)
            editPhoneNum = request.POST.get('editPhoneNum', False)
            user = request.user
            user.username = editUserName
            user.email = editEmail
            person = models.Person.objects.get(user = user)
            person.user = user
            person.first_name = edifFirstName
            person.last_name = editLastName
            person.address = editAddress
            person.city = editCity
            person.state = editState
            person.zipnum = editZipNum
            person.phonenum = editPhoneNum
            person.email = editEmail
            person.save()
            user.save()
            return redirect('/adoptApetApp')


        else:
            user = request.user
            person = models.Person.objects.get(user = user)
            return render(request,"editProfile.html", {'username': user ,'fname': person.first_name, 'lname' : person.last_name, 'email': person.email, 'address': person.address, 'city': person.city, 'state': person.state, 'zipnum': person.zipnum, 'phonenum': person.phone_number})
    else:
        return redirect('/adoptApetApp')

def logout_view(request):
    logout(request)
    return redirect("../adoptApetApp")

def insertAd(request):
    if request.method == "POST":
        name = request.POST.get('name',False)
        variety = request.POST.get('variety',False)
        gender = request.POST.get('gender',False)
        address = request.POST.get('address',False)
        weight = request.POST.get('weight',False)
        age = request.POST.get('age',False)
        photo = request.FILES['photo']
        description = request.POST.get('description', False)


        if request.user.is_authenticated():
            user = request.user
            pet = models.Pet(user = user, description = description, name = name, variety = variety, gender = gender, age = age, address = address, weight = weight, photo = photo)
            pet.save()
            return redirect('/adoptApetApp')
    return render(request, "insertAd.html")

def comments(request, petname):
    p = models.Pet.objects.get(name = petname)

    if request.method == "POST" and request.user.is_authenticated():
        user = request.user
        pet = request.POST.get('petname',False)
        description = request.POST.get('description',False)
        comment = models.Comment(commenter = user, pet=p, comment=description)
        comment.save()
        return redirect('/adoptApetApp/dialogues/' + petname)
    elif request.method == "GET" and request.user.is_authenticated():
        return render(request,"comments.html", {'pet' : p})
    else:
        return redirect("/adoptApetApp", {'pet' : p})
