from django.shortcuts import render
# Create your views here.

# Cat model
class Cat:
    def __init__(self, name, breed, description,age=0):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


cats = [
    Cat('Mr. Worms', 'Blue Russian', 'Very Cool', 5),
    Cat('Mr. Kitty', 'Blue Russian', 'Lazy',5),
    Cat('Jerry', 'Lost & Found', 'Cry Baby',3),
    Cat('Raven', 'Black', 'Too Young to assece', 0),

]
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})