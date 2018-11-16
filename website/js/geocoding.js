var geocoder; //To use later
var map; //Your map

function initMap() {
   var usa = {lat: 39.5, lng: -98.35};
   var map = new google.maps.Map(document.getElementById('map'), {zoom: 4, center: usa});
   //var marker = new google.maps.Marker({position: usa, map: map});
}

function initialize() {
  geocoder = new google.maps.Geocoder();
  //Default setup
  var latlng = new google.maps.LatLng(-34.397, 150.644);
  var myOptions = {
    zoom: 8,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
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