/*
sample code from
https://developers.google.com/maps/documentation/javascript/geocoding#GetStarted
*/

var geocoder; //To use later
var map; //Your map

function initialize() {
  geocoder = new google.maps.Geocoder();
  //Default setup
  var latlng = new google.maps.LatLng(39.5, -98.35);
  var mapOptions = {
    zoom: 4,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById("starbucksmap"), mapOptions);
}

//Call this wherever needed to actually handle the display
function codeAddress(zipCode) {
    geocoder.geocode( { 'address': zipCode}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        //Got result, center the map and put it out there
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location
        });
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });
  }