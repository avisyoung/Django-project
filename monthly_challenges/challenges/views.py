from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    "january": "<h1>Eat no meat for the entire month of January!</h1>",
    "february": "<h1>Walk for at least 20 minutes every day on February!</h1>",
    "march": "<h1>Learn Django at least 30 minutes a day on March!</h1>",
    "april": "<h1>Learn SQLite on April!</h1>",
    "may": "<h1>Keep learning SQLite on the month of May!</h1>",
    "june": "<h1>Take a break in June!</h1>",
    "july": "<h1><center>Start your Django learning again on July!</center></h1>",
    "august": "<h1>Make it 1 hours a day in August!</h1>",
    "september": "<h1>Follow up your SQLite learning on September!</h1>",
    "october": "<h1>Join Django and SQLite in October!</h1>",
    "november": "<h1>Compile your project in November!</h1>",
    "december": "<h1>Deploy you finished project by December</h1>!"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

