from django.http import HttpResponse
import json
from django.http import HttpResponseRedirect
import os, sys
import requests

def catch_email(request):
    """
        catch_all()
        forward("http://hm-spoof.herokuapp.com/catch_email")	
    """
    try:

        print "request.POST", request.POST

        from_address = request.POST['From']
        if type(from_address) is list:
            from_address = from_address[0]

        to_address = request.POST['To']
        if type(to_address) is list:
            to_address = to_address[0]

        try:
            from_address = from_address.split('<')[1].split('>')[0]
        except:
            pass

        try:
            to_address = to_address.split('<')[1].split('>')[0]
        except:
            pass

        print "to_address", to_address
        print "from_address", from_address
        
        if to_address == "bobdole@"+os.environ.get('MAILGUN_DOMAIN', ''):
            if from_address == "tedjones@"+os.environ.get('MAILGUN_DOMAIN', ''):
                plaintext = 'Hey! You may not have lost the password, as I just recently updated it so that could be why you are having trouble logging in. The new password is "eggroll". -Bob Dole'
            
                email_data = {
                    "from": "Bob Dole <bobdole@"+os.environ.get('MAILGUN_DOMAIN', '')+">",
                    "to": [from_address],
                    "subject": request.POST['subject'],
                    "html": plaintext,
                    "text": plaintext
                }
                print "email_data", email_data
                response = requests.post(
                    "https://api.mailgun.net/v3/{domain}/messages".format(domain=os.environ.get('MAILGUN_DOMAIN', '')),
                    auth=("api", os.environ.get('MAILGUN_API_KEY', '')),
                    data=email_data,
                    verify=False
                )
                print "[MAILGUN EMAIL API CALL=", response.status_code, response.text
                if response.status_code == 400:
                    print response.json()['message']
                
    except:

        exc_type, exc_value, exc_traceback = sys.exc_info()
        print "exc_type", exc_type
        print "exc_value", exc_value
        raise
    
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

