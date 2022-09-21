function onshort(){
    var xmlhr = new XMLHttpRequest();
    xmlhr.open( "GET", "genlink", false);
    link = document.getElementById("inputlink").value;
    xmlhr.setRequestHeader("link", link);
    xmlhr.send( null );
    data = xmlhr.responseText

    document.getElementById("inputlink").value = data;
}