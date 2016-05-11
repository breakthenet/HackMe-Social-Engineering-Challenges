// Locally: phantomjs fake_admin_browser.js --url test.com 
// Heroku: /app/vendor/phantomjs/bin/phantomjs fake_admin_browser.js --url test.com 

var system = require('system');
var killTimeout = 0;
var base_url = "http://localhost:8888/";

if (system.args.length === 1) {
    console.log('Try to pass some args when invoking this script!');
} else {
    system.args.forEach(function (arg, i) {
        if (i == 2) {
            base_url = arg;
        }
    });
}

var loginpage = require('webpage').create();

loginpage.open(base_url, function (status) {
    if (status !== 'success') {
        console.log("Unable to load "+base_url+" because of network issues");
    } else {
        loginpage.evaluate(function() {
            document.getElementById('id_username').value = 'scotty';
            document.getElementById('id_password').value = 'goldfish';
            document.forms[0].submit();
        });
    }
});


killTimeout = setTimeout(function(){
    phantom.exit(0);
}, 5000);
