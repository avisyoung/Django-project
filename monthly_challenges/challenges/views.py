from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month of January!",
    "february": "Walk for at least 20 minutes every day on February!",
    "march": "Learn Django at least 30 minutes a day on March!",
    "april": "Learn SQLite on April!",
    "may": "Keep learning SQLite on the month of May!",
    "june": "Take a break in June!",
    "july": "Start your Django learning again on July!",
    "august": "Make it 1 hours a day in August!",
    "september": "Follow up your SQLite learning on September!",
    "october": "Join Django and SQLite in October!",
    "november": "Compile your project in November!",
    "december": "Deploy you finished project by December!"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args = [month])
        list_items += f"<li><h1><a href=\"{month_path}\">{capitalized_month}</a></h1></li>"
        #list_items += f"<li><h1><a href={month_path}>{capitalized_month}</a></h1></li>"

# <li><a href="...">January</a></li> <li><a href="...">February</a></li>

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])# /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

