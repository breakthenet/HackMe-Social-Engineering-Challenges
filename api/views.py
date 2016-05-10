from django.http import HttpResponse
import datetime
import json
from django.http import HttpResponseRedirect

def email_challenge_1(request):
    
    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

    
def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")

