function flag(text) {
    text = text.toString().replace('Finland', "&#x1F1EB;&#x1F1EE;");
    text = text.toString().replace('Sweden', "&#x1F1F8;&#x1F1EA;");
    text = text.toString().replace('Denmark', "&#x1F1E9;&#x1F1F0;");
    text = text.toString().replace('Iceland', "&#x1F1EE;&#x1F1F8;");
    text = text.toString().replace('Norway', "&#x1F1F8;&#x1F1EF;");
    return text
    
}

function keysToList(dict) {
    var keys = []
    Object.keys(dict).forEach(function(key) {
		keys.push(key)
    });
    return keys
}


function renderMeta() {
	document.getElementById('header').innerHTML = meta_siteName;
}

function badgify(badgeString) {
    if (badgeString.length < 2)
        return ''
    badge_display = "<div class='value'>"
    badges = badgeString.split(",")
    badges.forEach(function(e) {
        badge_display += "<div class='badge'>" + e + "</div>"
    });
    badge_display += "</div>"
    return badge_display

}

function starify(int) {
    if (int == 'na') {
        return "n/a"
    }
    int = parseInt(int)
	return "&#x1f333;".repeat(int) + "<span class='nostar'>" + "&#x1f333;".repeat(5-int) + "</span>"
}

function display(key, value, styles) {

	display_style = styles[key]
	switch (display_style) {
		//case 'yes':
		//	return "<div class='value'>" + value + "</div>" +  "<div class='label'>" + key + '</div>'
		case 'flag':
			return "<div class='flag'>" + flag(value) + "</div>"
		case 'normal':
			return "<div class='value'>" + value + "</div>"
		case 'title':
            return "<div class='title'>" + value + "</div>"
        case 'star':
            return starify(value)
		case 'badges':
			return badgify(value)
	}
}


function displayItem(key, value, styles) {
    display_style = styles[key]
    switch(display_style) {
        case 'title':
            return "<h1>" + value + "</h1>"
        default:
            return display(key, value, styles)
    }
}