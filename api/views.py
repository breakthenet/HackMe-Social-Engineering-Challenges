from django.http import HttpResponse
import json
from django.http import HttpResponseRedirect
import os
import requests

def catch_email(request):
    """
        catch_all()
        forward("http://hm-spoof.herokuapp.com/catch_email")	
    """
    
    print "request.POST['to'].split('@')[0]", request.POST['to'].split("@")[0]
    print "request.POST['sender'][0]", request.POST['sender'][0]
    
    if request.POST['to'].split("@")[0] == "bobdole":
        if request.POST['sender'][0] == "joe@"+os.environ.get('MAILGUN_DOMAIN', ''):
            plaintext = 'Hey! You may not have lost the password, as I just recently updated it so that could be why you are having trouble logging in. The new password is "eggroll". -Bob Dole'
        
            email_data = {
                "from": "Bob Dole <bobdole@"+os.environ.get('MAILGUN_DOMAIN', '')+">",
                "to": [request.POST['from']],
                "subject": request.POST['subject'],
                "html": plaintext,
                "text": plaintext
            }
            print "email_data", email_data
            #response = requests.post(
            #    "https://api.mailgun.net/v3/{domain}/messages".format(domain=os.environ.get('MAILGUN_DOMAIN', '')),
            #    auth=("api", os.environ.get('MAILGUN_API_KEY', '')),
            #    data=email_data,
            #    verify=False
            #)
            #print "[MAILGUN EMAIL API CALL=", response.status_code, response.text
            #if response.status_code == 400:
            #    print response.json()['message']
    
    return HttpResponse(json.dumps({
        "status": "success"
    }), content_type='application/json', status=200)

def get_config(request):
    return HttpResponse(json.dumps({
        "challenge_1_email_to": "bobdole@"+os.environ.get('MAILGUN_DOMAIN', ''),
        "challenge_1_email_from": "tedjones@"+os.environ.get('MAILGUN_DOMAIN', '')
    }), content_type='application/json', status=200)

    
def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")

