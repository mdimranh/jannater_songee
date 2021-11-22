

$( window ).resize(function() {
    if ($(window).width() > 640) {
        $('#offcanvasWithBackdrop').removeClass('show');
        document.getElementById('offcanvasWithBackdrop').style.visibility = 'hidden';
        $('.offcanvas-backdrop').removeClass('show');
    }
});




$( window ).resize(function() {
    let intViewportHeight = window.innerHeight;
    if (intViewportHeight < 750){
        document.getElementById("notification-menu").style["height"] = (intViewportHeight-150).toString()+"px";
    }
    else if (intViewportHeight > 750){
        document.getElementById("notification-menu").style["height"] = "600px";
    }
});



function act(a) {
    document.getElementById(a).classList.add("active");
    document.getElementById("side-"+a).classList.add("active");
    if (a === 'about'){
        var myCollapse = document.getElementById('collapseExample')
        var bsCollapse = new bootstrap.Collapse(myCollapse, {
        toggle: true
        });
    }
}

// document.getElementById('login').addEventListener('click', function(e) {
//     $('#loginmodal').modal('show');
// });
// document.addEventListener('contextmenu', event => event.preventDefault());

$( "#side-about" ).click(function() {
  $( this ).toggleClass( "show" );
});

$('.toggle').click(function(){
    $('.form').animate({
        height: "toggle",
        'padding-top': 'toggle',
        'padding-bottom': 'toggle',
        opacity: "toggle"
    }, "slow");
    var signuptoggle = document.getElementById("signup-toggle");
    var logintoggle = document.getElementById("login-toggle");
    if (signuptoggle.style.display === "none") {
        signuptoggle.style.display = "block";
        logintoggle.style.display = "none";
    } else {
        signuptoggle.style.display = "none";
        logintoggle.style.display = "block";
    }
});


let scrollbtn = document.getElementById("arrow");
scrollbtn.onclick = function() {
    window.scrollTo(0,0);
};