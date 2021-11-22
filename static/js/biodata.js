$('.nav-pills .nav-link').click(function (e) {     

    var serial = $(this).attr('serial');
    $('.nav-pills .nav-link').removeClass('active');

    var sp = document.getElementsByClassName(serial);
    sp[0].classList.add("active");
    sp[1].classList.add("active");
    // pos = sp[1].offsetLeft;
    // alert(pos);
    // document.getElementById("v-pills-tab").scrollX = 10;
})


var finalEnlishToBanglaNumber={'0':'০','1':'১','2':'২','3':'৩','4':'৪','5':'৫','6':'৬','7':'৭','8':'৮','9':'৯'};
 
String.prototype.getDigitBanglaFromEnglish = function() {
    var retStr = this;
    for (var x in finalEnlishToBanglaNumber) {
         retStr = retStr.replace(new RegExp(x, 'g'), finalEnlishToBanglaNumber[x]);
    }
    return retStr;
};


var sp = $(".tab-pane");
for (var i=0; i<sp.length; i++) {
    var num = $(sp[i].getElementsByClassName("number"));
    for (var j=0; j<num.length; j++) {
        var newValue = (j+1).toString();
        var numberbn=newValue.getDigitBanglaFromEnglish();
        num[j].innerHTML  = numberbn;
    }
}


// height customization
var node = document.getElementById('height'),
height = node.textContent;
let feet = Math.floor(height / 12);
let inches = height - feet * 12;
var feetnumberbn = feet.toString().getDigitBanglaFromEnglish();
var inchesnumberbn = inches.toString().getDigitBanglaFromEnglish();
document.getElementById("height").innerHTML = ""+feetnumberbn + "'" + inchesnumberbn + "''";
// end height customization
