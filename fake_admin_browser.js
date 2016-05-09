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

function scan_user_list() {
    var userlistpage = require('webpage').create();
    
    userlistpage.onConsoleMessage = function(msg) {
        if (msg.indexOf("viewuser.php") > -1) {
            //Found user profile, run it and scan for links
            scan_user_profile(msg);
        }
    };
    
    userlistpage.open(base_url+"userlist.php", function (status) {
        // Check for page load success
        if (status !== "success") {
            console.log("Unable to load "+base_url+"userlist.php because of network issues");
        } else {
            userlistpage.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js", function() {
                console.log("Extracting user profile links from userlist.php...");
                userlistpage.evaluate(function() {
                    $(".userprofilelink").each(function() {
                        console.log(jQuery(this).attr('href'));
                    });
                });
            });
            killTimeout = setTimeout(function(){
                phantom.exit(0);
            }, 3000);
        }
    });
}

function scan_user_profile(profileurl) {
    clearTimeout(killTimeout);
    var userprofilepage = require('webpage').create();
    userprofilepage.onAlert = function(alertmsg) {
        //Found link on user profile, just run it
        scan_external_age(alertmsg);
    }
    userprofilepage.open(base_url+profileurl, function (status) {
        if (status !== "success") {
            console.log("Failed opening "+base_url+profileurl);
        } else {
            console.log("Successfully opened "+base_url+profileurl);
            userprofilepage.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js", function() {
                console.log("Extracting any links in profile signature...");
                userprofilepage.evaluate(function() {
                    jQuery(".profile_sig").find('a').each(function() {
                        alert(jQuery(this).attr('href'));
                    });
                });
            });
        }
        killTimeout = setTimeout(function(){
            phantom.exit(0);
        }, 3000);
    });
}

function scan_external_age(url) {    
    if (url.indexOf("googleapis") > -1) {
        //pass
    }
    else {
        clearTimeout(killTimeout);
        console.log("Found link on user profile: "+url);
        var externalpage = require('webpage').create();
        externalpage.open(url, function (status) {
            if (status !== "success") {
                console.log("Failed opening "+url);
            } else {
                console.log("Successfully opened "+url);
            }
            killTimeout = setTimeout(function(){
                phantom.exit(0);
            }, 3000);
        });
    }
}

var loginpage = require('webpage').create();
loginpage.open(base_url+'authenticate.php', 'post', 'username=admin&password=cupcake&save=OFF', function (status) {
    if (status !== 'success') {
        console.log('********Login failed!!!!');
        console.log(loginpage.content);
    } else {
        console.log('Login successful.');
    }
    
    scan_user_list();
});
