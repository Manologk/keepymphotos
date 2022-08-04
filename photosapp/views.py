from django.shortcuts import render, redirect
from .models import Category, Photo


# Create your views here.
def home(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__contains=category)

    categories = Category.objects.all()
    # photos = Photo.objects.all()
    context = {
        'categories': categories,
        'photos': photos,
    }
    return render(request, 'photosapp/home.html', context)


def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photosapp/viewphoto.html', {
        'photo': photo,
    })


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

        return redirect('homepage')

    return render(request, 'photosapp/addphoto.html', {
        'categories': categories,
    })
