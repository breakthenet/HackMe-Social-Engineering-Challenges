from django.http import HttpResponse
import json
from django.http import HttpResponseRedirect
import os

def catch_email(request):
    """
        catch_all()
        forward("http://hm-spoof.herokuapp.com/catch_email")	
    """
    
    mailgun_domain = os.environ.get('MAILGUN_DOMAIN', '')
    
    print "request.POST", str(request.POST)
    print "request.GET", str(request.GET)
    
    print "request.POST['recipient']", request.POST['recipient']
    to_address = request.POST['recipient']
    to_prefix = hash_email.split("@")[0]  # hash@email.com
    print "request.POST['stripped-text']", request.POST['stripped-text']
    
    return HttpResponse(json.dumps({
        "status": "success"
    }), content_type='application/json', status=200)

    
def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")

