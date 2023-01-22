function myMap() {
  var mapProp = {
    center: new google.maps.LatLng(51.508742, -0.12085),
    zoom: 5,
  };
  var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}
var nav = document.querySelector("nav");
var button = document.querySelector(".hamburger-menu");
button.addEventListener("click", (event) => {
  nav.classList.toggle("open");
});
