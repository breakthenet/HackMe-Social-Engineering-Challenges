from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^email_challenge_1$', "api.views.email_challenge_1"),
    url(r'^email_challenge_2$', "api.views.email_challenge_2"),
    url(r'^email_challenge_3$', "api.views.email_challenge_3"),
    url(r'^sms_challenge_1$', "api.views.sms_challenge_1"),
    url(r'^phone_challenge_1$', "api.views.phone_challenge_1"),
    url(r'^$', "api.views.load_frontend")
)
