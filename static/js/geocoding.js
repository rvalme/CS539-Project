/*
sample code from
https://developers.google.com/maps/documentation/javascript/geocoding#GetStarted
*/

//initialize map
var geocoder;
var map;
var markers;

function initialize() {
    var latlng = new google.maps.LatLng(39.5, -98.35);
    var mapOptions = {
        zoom: 4,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map(document.getElementById("starbucksmap"), mapOptions);

    geocoder = new google.maps.Geocoder();
    markers = []

    //var button = document.getElementById("floating-panel");
    var button = document.getElementById("searchButton");
    button.addEventListener('click', function() {codeAddress(geocoder, map);
        });
    if(button == null){
        alert("Not Initialized");
    }

}

var ws = new WebSocket('ws://cs539-starbucks.herokuapp.com/ws');
//var ws = new WebSocket('ws://www.example.com/ws/foobar?subscribe-broadcast&publish-broadcast&echo');
ws.onopen = function() {
    console.log("websocket connected");
};

ws.onmessage = function(e) {
    console.log("Received: " + e.data);
    clearMarkers()
    markers = []
    add_markers(e.data)
};

ws.onerror = function(e) {
    console.log("connection closed");
};

function send_message(msg) {
    ws.send(msg);
}


//re-center the map according to the zipcode input
//Call this wherever needed to actually handle the display
function codeAddress(geocoder, map) {
    //get zipcode
    var zipCode = document.getElementById('location').value;
    //only search within USA
    send_message(zipCode);
    geocoder.geocode( { 'address': zipCode, "componentRestrictions":{"country":"USA"}},
     function(results, status) {
      if (status === google.maps.GeocoderStatus.OK) {
        //zoom factor: 4 --> 8
        map.setZoom(12);
        map.setCenter(results[0].geometry.location);
///TODO reset the map when a new zipcode/address is entered when implement markers
//        var marker = new google.maps.Marker({
//            map: map,
//            position: results[0].geometry.location
//        });
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });
  }
function add_markers(num_markers) {
    //get zipcode
    var zipCode = document.getElementById('location').value;
    //only search within USA
    geocoder.geocode( { 'address': zipCode, "componentRestrictions":{"country":"USA"}},
     function(results, status) {
      if (status === google.maps.GeocoderStatus.OK) {
///TODO reset the map when a new zipcode/address is entered when implement markers
        for(i = 0; i< num_markers; i++){
            var position = new google.maps.LatLng(results[0].geometry.location.lat() + (Math.random() *.02), results[0].geometry.location.lng() + (Math.random() * .2))
            var marker = new google.maps.Marker({
                map: map,
                position: position
            });
            markers.push(marker);
        }
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });
  }

function clearMarkers(){
    for(i = 0; i < markers.length; i++){
        markers[i].setMap(null)
    }
}
