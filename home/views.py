from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'djangocms-twitter', 'url': 'http://pypi.python.org/pypi/djangocms-twitter/0.0.5'},
	{'name':'cmsplugin-twitter', 'url': 'http://pypi.python.org/pypi/cmsplugin-twitter/1.1.2'},
	{'name':'django-paypal', 'url': 'http://pypi.python.org/pypi/django-paypal/0.4.1'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-76',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
