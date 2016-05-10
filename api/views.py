from django.http import HttpResponse
import json
from django.http import HttpResponseRedirect
import os, sys
import requests
import sendgrid

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
            
        reply_to_address = from_address
        try:
            reply_to_address = request.POST.get('Reply-To', '')
            if type(reply_to_address) is list:
                reply_to_address = reply_to_address[0]
        except:
            pass

        try:
            from_address = from_address.split('<')[1].split('>')[0]
        except:
            pass

        try:
            to_address = to_address.split('<')[1].split('>')[0]
        except:
            pass

        try:
            reply_to_address = reply_to_address.split('<')[1].split('>')[0]
        except:
            pass

        print "to_address", to_address
        print "from_address", from_address
        print "reply_to_address", reply_to_address
        
        if to_address == "bobdole@"+os.environ.get('MAILGUN_DOMAIN', ''):
            if from_address == "tedjones@"+os.environ.get('MAILGUN_DOMAIN', ''):
                plaintext = 'Hey! You may not have lost the password, as I just recently updated it so that could be why you are having trouble logging in. The new password is "eggroll". \n-Bob Dole\nCEO, Veritas Inc.'
                
                sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME', ''), os.environ.get('SENDGRID_PASSWORD', ''))
                
                message = sendgrid.Mail()
                message.add_to(reply_to_address)
                message.set_subject("Re: "+request.POST['subject'])
                message.set_html(plaintext)
                message.set_text(plaintext)
                message.set_from("Bob Dole <bobdole@"+os.environ.get('MAILGUN_DOMAIN', '')+">")
                status, msg = sg.send(message)
                print status
                print msg
            else:
                plaintext = "Hey, I just got an email from you, but don't know who you are! Only my CFO Ted Jones ("+"tedjones@"+os.environ.get('MAILGUN_DOMAIN', '')+") ever emails me at this address, and you emailed me from: "+from_address
                
                sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME', ''), os.environ.get('SENDGRID_PASSWORD', ''))

                message = sendgrid.Mail()
                message.add_to(reply_to_address)
                message.set_subject("Re: "+request.POST['subject'])
                message.set_html(plaintext)
                message.set_text(plaintext)
                message.set_from("Bob Dole <bobdole@"+os.environ.get('MAILGUN_DOMAIN', '')+">")
                status, msg = sg.send(message)
                print status
                print msg
                
                
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
        "mailgun_domain": os.environ.get('MAILGUN_DOMAIN', '')
    }), content_type='application/json', status=200)

def catch_sms(request):
    return HttpResponse(json.dumps({
        "status": "success"
    }), content_type='application/json', status=200)

def catch_phone_call(request):
    return HttpResponse(json.dumps({
        "status": "success"
    }), content_type='application/json', status=200)
    
def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")

