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
        userlistpage.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js", function() {
            userlistpage.evaluate(function() {
                $('#id_username').value('scotty');
                $('#id_password').value('goldfish');
                $('.submit-row').find('input').click();
            });
        });
        setTimeout(function(){
            phantom.exit(0);
        }, 3000);
    }
});
