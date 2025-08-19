from django.shortcuts import render

def details(request,question_id):
    return HttpResponse("Your are looking at Question %s. " %question_id)


def results(request,question_id):
    response="your are looking at the result of Question %s. "
    return HttpResponse(response % question_id)


def vote(request,question_id)
    return HttpResponse("you are voting on question %s. " question_id)
# Create your views here.
