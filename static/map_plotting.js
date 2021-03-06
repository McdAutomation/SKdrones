function openWindow(name){
  var popupWindow = window.open("open_popup_window", "MsgWindow", "top=200, left=200, width=800, height=500");
  url = "{% url "visual:popup" %}";

  $.get(url, { d: name, stadium_name: name } )
    .done(function(data){
      popupWindow.window.onload = function() {

                  for(i=0;i<data['games_played'].length;i++){
                      var tr = document.createElement("tr");

                      var td = document.createElement('td');
                      var td_text = document.createTextNode(data['games_played'][i]['team_a']);
                      td.appendChild(td_text);
                      tr.appendChild(td);

                      var td = document.createElement('td');
                      var td_text = document.createTextNode(data['games_played'][i]['team_b']);
                      td.appendChild(td_text);
                      tr.appendChild(td);

                      var td = document.createElement('td');
                      var td_text = document.createTextNode(data['games_played'][i]['score']);
                      td.appendChild(td_text);
                      tr.appendChild(td);

                      var td = document.createElement('td');
                      var td_text = document.createTextNode(data['games_played'][i]['stage']);
                      td.appendChild(td_text);
                      tr.appendChild(td);


                      popupWindow.document.getElementById('game_list').appendChild(tr);
                  }
              }
    });

}
var markers = new Array();
function plotPoints(){
      url = "{% url "visual:filter_by_year" %}";
      var code = $("#sources option:selected").val();

      var markerIcon = L.icon({
      iconUrl: '{% static "leaflet/images/marker-icon.png" %}',
      shadowUrl: '{% static "leaflet/images/marker-shadow.png" %}',

      //iconSize:     [100, 41], // size of the icon
      //shadowSize:   [50, 64], // size of the shadow
      //iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
      //shadowAnchor: [4, 62],  // the same for the shadow
      //popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
      });

      $.get(url, { data: code} )
          .done(function(data){
            try{
              for(i=0;i<markers.length;i++) {
                map.removeLayer(markers[i]);
              }
              markers.splice(0,markers.length);
          }catch(err){
              //pass
            }
            $.get("/popup",{d:JSON.stringify(data)}).done(function(data){
              for(i=0;i<data['dj_data'].length;i++){
                marker = L.marker([data['dj_data'][i].lat, data['dj_data'][i].long],{icon:markerIcon}).addTo(map);

                var div = document.createElement("div");
                div.innerHTML = data['dj_data'][i].name + '<br>' +
                'Total Games Played: '+data['dj_data'][i].number_of_games + '<br><a href=\'#\' onclick="openWindow(\''+data['dj_data'][i].name+'\')">more info!!</a>';
                marker.bindPopup(div);
                markers.push(marker);
              }
            });
  });
}
function callFunctions(){
      $.when( plotPoints() ).done(function() {
      });
}
$( "select.selectYear" ).change(callFunctions);


// initialize the map
var map = L.map('map').setView([55.7093305, 37.55216446], 3);


L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
  maxZoom: 19,
  minZoom: 3,
  attribution: "&copy; <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a>"
}).addTo(map);
