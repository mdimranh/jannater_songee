// $(document).ready(function(){
//   setInterval(function(){
//     $.ajax({
//       type: "GET",
//       url: "/notifications",
//       success: function(response){
//         if (response.no_notification == 0){
//           document.getElementById("badge").style["visibility"]= 'hidden';
//         }
//         else if (response.no_notification > 9){
//           document.getElementById("badge").style["visibility"]= 'visible';
//           document.getElementById("badge").innerHTML = '9+';
//         }
//         else{
//           document.getElementById("badge").style["visibility"]= 'visible';
//           document.getElementById("badge").innerHTML = response.no_notification;
//         }
//         if(response.no_all != 0){
//         $("#n-show").empty();
//         for (var key in response.notification){
//           var temp1 = '<a href="/b_'+response.userlist[key]+'" class="d-flex align-items-center py-1 px-2">';
//           var temp2 = '<img src="../static/img/'+response.profile+'" class="profile"></img>';
//           var temp3 = '<div class="d-flex flex-column">';
//           var temp4 = '<p class="ps-2 m-0">বায়োডাটা:' +response.userlist[key]+' '+response.notification[key].details+'</p>';
//           var temp5 = '<small class="time">'+response.timelist[key]+'</small></div></a>';
//           var temp6 = temp1+temp2+temp3+temp4+temp5;
//           $("#n-show").append(temp6);
//         }
//         }
//       }
//     });
//   }, 1500);
// });


document.getElementById('notificationbtn').addEventListener('click', function (event) {
  event.preventDefault();
  document.getElementById("badge").style["visibility"]= 'hidden';
   document.getElementById("badge").innerHTML = '0';
  var formData = new FormData();
  formData.append("id", id);
  var xhr=new XMLHttpRequest();
  xhr.open("POST", "http://localhost:8000/notification_seen_time", true);
  xhr.send(formData);
});


function getNotification(user_id){
let socket = new WebSocket('ws://localhost:8000/ws/notification/' + user_id);
socket.onopen = function (e) {
  console.log('Connection established');
};

socket.onmessage = function (e) {
  var data = JSON.parse(e.data)
  var sender = data.notification.sender;
  var details = data.notification.details;
  var time = data.notification.time;
  var profile = data.notification.profile;
  var no_notification = document.getElementById("badge").innerHTML;
  document.getElementById("badge").innerHTML = (parseInt(no_notification) + 1);
  document.getElementById("badge").style["visibility"]= 'visible';
  if ($(".not-get").length > 0){
    $("#n-show").empty();
  }
  var temp1 = '<a href="/b_'+sender+'" class="d-flex align-items-center py-1 px-2">';
  var temp2 = '<img src="../static/img/'+profile+'" class="profile"></img>';
  var temp3 = '<div class="d-flex flex-column">';
  var temp4 = '<p class="ps-2 m-0">বায়োডাটা: '+sender+' '+details+'</p>';
  var temp5 = '<small class="time">'+time+'</small></div></a>';
  var temp6 = temp1+temp2+temp3+temp4+temp5;
  $("#n-show").prepend(temp6);
  console.log(data);
};
socket.onclose = function (e) {
  console.log('Connection closed');
};
}