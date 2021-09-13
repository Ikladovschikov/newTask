import json


from django.shortcuts import render
import requests


class SomeObject:
    def __init__(self, state):
        self.state = state

cat2 = SomeObject(False)
print(cat2.state)


def index(request):
    if request.method == "POST":
        get_post(request)
    else:
        return render(request, 'index.html')


    

def get_post(request):
    json_data = json.loads(request)
    cat2.state = json_data['state']
    print(cat2.state)
    return cat2.state