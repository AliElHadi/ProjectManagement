function $(id) { return document.getElementById(id) };
window.onload = function () {


    /*   GETTING LOCATION OF THE USER   */
    var req = new XMLHttpRequest();
    req.overrideMimeType("application/json");
    req.open('GET', 'https://ipapi.co/json/', true);
    req.onload = function () {
        /*alert(req.responseText)*/
        var data = JSON.parse(req.responseText);
        var country_name = data.country_name;
        var city = data.city;
        var country_code = data.country_code;
        var timezone = data.timezone;
        var userlocation = $("UserLocation");
        var P = document.createElement("p");
        var text = document.createTextNode("Country Name: " + country_name);
        P.appendChild(text);
        userlocation.appendChild(P);
        P = document.createElement("p");
        text = document.createTextNode("Country Code: " + country_code);
        P.appendChild(text);
        userlocation.appendChild(P);
        P = document.createElement("p");
        text = document.createTextNode("City: " + city);
        P.appendChild(text);
        userlocation.appendChild(P);
        P = document.createElement("p");
        text = document.createTextNode("Timezone: " + timezone);
        P.appendChild(text);
        userlocation.appendChild(P);
    };
    req.send(null);
    /*     LOCATION CODE ENDS HERE    */



}