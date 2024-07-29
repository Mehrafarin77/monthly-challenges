from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.
months = {
    'January':'Setting 3 priorities for the day and completing them, no matter what',
    'February':'Publishing something every day (a blog post, a tweet, a book summary, a post on FB)',
    'March':'Detox: sugar-free, news-free.',
    'April':'No sugar, again.',
    'May': 'Reading a paper book for 30 minutes.',
    'June': 'Waking up before 9 AM.',
    'July': 'Cold showers in the morning.',
    'August': 'No alcohol.',
    'September': 'One hour of learning every day.',
    'October': 'No coffee.',
    'November': 'Daily post on Instagram.',
    'December': None,
}

def by_number(request, index):
    try:
        list_months = list(months.keys())
        if index not in range(1, 13):
            return HttpResponseNotFound('<h1>Not a valid month.</h1>')

        # in order to redirect to some other url
        # "{% url 'challenges:month' list_months[index - 1] %}"
        redirect_path = reverse('challenges:month', args=[list_months[index - 1]])
        return HttpResponseRedirect(redirect_path)
    except:
        result = render_to_string('not_found.html')
        return HttpResponseNotFound(result)

def list_of_months(request):
    try:
        context ={
            'months': months
        }
        return render(request, 'months.html', context)
    except:
        result = render_to_string('not_found.html')
        return HttpResponseNotFound(result)

def challenges(request, month):
    try:
        month = month.capitalize()
        context = {
            'challenge': months[month],
            'month': month
        }
        return render(request, 'challenge.html', context)
    except:
        result = render_to_string('not_found.html')
        return HttpResponseNotFound(result)