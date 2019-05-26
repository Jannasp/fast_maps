
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return '''<!DOCTYPE html>
<html>
  <head>
    <style>
       /* Set the size of the div element that contains the map */
      #map {
        height: 200px;  /* The height is 400 pixels */
        width: 1000px;  /* The width is the width of the web page */
       }
    </style>
  </head>
  <body>
    <!--The div element for the map -->
    <div id="map"></div>
    <script>
// Initialize and add the map
function initMap() {
  // The location of El Pan
  var pan = {lat: -2.778050, lng: -78.660564};
  // The map, centered at El Pan
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 18, center: pan});
  // The marker, positioned at el pan
  var marker = new google.maps.Marker({position: uluru, map: map});
}
    </script>
    <!--Load the API from the specified URL
    * The async attribute allows the browser to render the page while the API loads
    * The key parameter will contain your own API key (which is not needed for this tutorial)
    * The callback parameter executes the initMap() function
    -->
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBsX62x2sjskoUXyOSY-wRhhCtLVIUtLJs&callback=initMap">
    </script>
  </body>
</html>'''

if __name__ == "__main__":
    app.run(debug=True)
