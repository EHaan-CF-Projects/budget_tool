from django.shortcuts import render

def home_view(request):
    """Route to home view."""
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'generic/home.html', context)
    