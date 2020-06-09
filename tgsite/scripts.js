function getEmail(button) {
    console.log("capturing email... ")
    var email = button.previousSibling
    if (!email.validity.patternMismatch) {
        email = email.value
        var HOOKURL = "https://hooks.slack.com/services/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"
        var body = JSON.stringify({
            "text": "New website signup: " + email
        })
        var xhttp = new XMLHttpRequest();
        xhttp.open("POST", HOOKURL, true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        // xhttp.send(body);
        console.log("capturing email... DONE")
    }
}