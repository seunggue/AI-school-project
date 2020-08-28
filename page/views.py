from django.shortcuts import render

# Create your views here.

def index(request):
    print('???')
    posts = [
        {
            'movie':'테넨',
            'genre':'sf',
        },
        {
            'movie':'다만 악에서 구하호서',
            'genre':'액션',
        },
        {
            'movie':'반도',
            'genre':'액션'
        }
    ]
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def result(request, movie):
    print(movie)
    print('result')
    return render(request, 'result.html')