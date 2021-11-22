

function mdl() {
    $('.modal').modal('show');
}

// $(function(){
//     $('.modal').modal('show');
// });

tail.select('#gender',{
    width: 260,
});

tail.select('#biodatatype',{
    width: 260,
});

tail.select('#district',{
    width: 260,
    height: 330,
    search: true,
    locale: "district",
    multiSelectAll: true,
});

tail.select('#color',{
    width: 260,
    search: true,
    locale: "color",
    multiSelectAll: true,
});

tail.select('#educationtype',{
    width: 260,
});

// document.getElementById('login').addEventListener('click', function(e) {
//     $('#loginmodal').modal('show');
// });

// let signupbtn = document.getElementById('signup-alt-btn');
// document.getElementById('signup-alt-btn').addEventListener('click', function(e) {
//     signupbtn.classList.add("active");
// });



// $('.toggle').click(function(){
//     $('.form').animate({
//         height: "toggle",
//         'padding-top': 'toggle',
//         'padding-bottom': 'toggle',
//         opacity: "toggle"
//     }, "slow");
//     var signuptoggle = document.getElementById("signup-toggle");
//     var logintoggle = document.getElementById("login-toggle");
//     if (signuptoggle.style.display === "none") {
//         signuptoggle.style.display = "block";
//         logintoggle.style.display = "none";
//     } else {
//         signuptoggle.style.display = "none";
//         logintoggle.style.display = "block";
//     }
// });


// let scrollbtn = document.getElementById("arrow");
// scrollbtn.onclick = function() {
//     window.scrollTo(0,0);
// };


var height1 = document.getElementById('height1');
var height2 = document.getElementById('height2');
var age1 = document.getElementById('age1');
var age2 = document.getElementById('age2');

height1.onkeyup = function(){
    document.getElementById('heightbtn').innerHTML = "উচ্চতা ("+height1.value+" থেকে "+height2.value+" )";
}
height2.onkeyup = function(){
    document.getElementById('heightbtn').innerHTML = "উচ্চতা ("+height1.value+" থেকে "+height2.value+" )";
}

age1.onkeyup = function(){
    document.getElementById('agebtn').innerHTML = "বয়স ("+age1.value+" থেকে "+age2.value+" )";
}
age2.onkeyup = function(){
    document.getElementById('agebtn').innerHTML = "বয়স ("+age1.value+" থেকে "+age2.value+" )";
}