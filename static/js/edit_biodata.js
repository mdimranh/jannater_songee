// height customization
var finalEnlishToBanglaNumber = {
  0: "০",
  1: "১",
  2: "২",
  3: "৩",
  4: "৪",
  5: "৫",
  6: "৬",
  7: "৭",
  8: "৮",
  9: "৯",
};

String.prototype.getDigitBanglaFromEnglish = function () {
  var retStr = this;
  for (var x in finalEnlishToBanglaNumber) {
    retStr = retStr.replace(new RegExp(x, "g"), finalEnlishToBanglaNumber[x]);
  }
  return retStr;
};


    var height = document.getElementById("height").value;
    let feet = Math.floor(height / 12);
    let inches = height - feet * 12;
    var feetnumberbn = feet.toString().getDigitBanglaFromEnglish();
    var inchesnumberbn = inches.toString().getDigitBanglaFromEnglish();
    document.getElementById("ht").innerHTML = ""+feetnumberbn + "'" + inchesnumberbn + "''";

// end height customization




$('#paddress').on('change', function ()
{
    var label = $(this.options[this.selectedIndex]).closest('optgroup').prop('label');
    var text = this.options[this.selectedIndex].text;
    $('.district').text(text);
});

document.getElementById('presentaddress').addEventListener('change', function() {
    var text = this.options[this.selectedIndex].text;
});

$('#color').on('change', function ()
{
    var text = this.options[this.selectedIndex].text;;
    $('.color').text(text);
});


document.getElementById('marital-status').addEventListener('change', function() {
    var text = this.options[this.selectedIndex].text;
    $('.marital-status').text(text);
});

document.getElementById('blood-group').addEventListener('change', function() {
    var text = this.options[this.selectedIndex].text;
    $('.blood').text(text);
});

document.getElementById('what-do').addEventListener('change', function() {
    const val = [];
    $('#what-do :selected').each(function(i, sel){
        valu = " "+$(sel).val();
        if (valu == ' study'){
            valu = 'ছাত্রী';
            document.getElementById('study').style.display = 'block';
        }
        else if (valu == ' job'){
            valu = 'চাকরি';
        }
        else if (valu == ' seek-job'){
            valu = 'চাকরি খুঁজছি';
        }
        else if (valu == ' business'){
            valu = 'ব্যবসা';
        }
        val.push(valu);
    });
    if(val.length === 0){
        $('.work').text("--");
    }
    else{
        $('.work').text(val);
    }
});


document.getElementById('partner-marital-status').addEventListener('change', function() {
    const val = [];
    $('#partner-marital-status :selected').each(function(i, sel){
        valu = $(sel).val();
        val.push(valu);
    });
    if(val.indexOf("বিবাহিত") === -1){
        document.getElementById('masna').style.display = 'none';
    }
    else{
        document.getElementById('masna').style.display = 'block';
    }
});


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







var finalEnlishToBanglaNumber={'0':'০','1':'১','2':'২','3':'৩','4':'৪','5':'৫','6':'৬','7':'৭','8':'৮','9':'৯'};
 
String.prototype.getDigitBanglaFromEnglish = function() {
    var retStr = this;
    for (var x in finalEnlishToBanglaNumber) {
         retStr = retStr.replace(new RegExp(x, 'g'), finalEnlishToBanglaNumber[x]);
    }
    return retStr;
};


$('#birthyear').calendar({
    type: 'year',
    onChange: function (year, text) {
    var newValue = text;
    var numberbn=newValue.getDigitBanglaFromEnglish();
    $('.birth').text(numberbn);
    },
});

$('#daorayehadith').calendar({
    type: 'year'
});

$('#takhacchoryear').calendar({
    type: 'year'
});

$('#sscyear').calendar({
    type: 'year'
});

$('#hscyear').calendar({
    type: 'year'
});

$('#graduateyear').calendar({
    type: 'year'
});
    



tail.select('#marital-status',{
});

tail.select('#paddress',{
    search: true,
    locale: "district",
    multiSelectAll: true,
});

tail.select('#presentaddress',{
    height: 300,
    search: true,
    locale: "district",
    multiSelectAll: true,
});

tail.select('#color',{
});

tail.select('#blood-group',{
   height: 160
});

tail.select('#division',{
   height: 185
})

tail.select('#what-do',{
   locale: "what_do",
   placeholder: "পেশা নির্বাচন করুণ"
})

tail.select('#education',{
   placeholder: "মাধ্যম নির্বাচন করুণ"
});

tail.select('#ssc',{
});

tail.select('#ssc-department',{
});

tail.select('#sscresult',{
    height: 160
});

tail.select('#hsc',{
});

tail.select('#hsc-department',{
});

tail.select('#hscresult',{
    height: 160
});

tail.select('#graduate',{
    height: 160
});

tail.select('#hafez',{
});

tail.select('#brother',{
    height: 160
});

tail.select('#sister',{
    height: 160
});

tail.select('#children',{
    height: 160
});

tail.select('#children-address',{
});

tail.select('#weakness',{
});

tail.select('#mehnot',{
});

tail.select('#partner-marital-status',{
    placeholder: "বৈবাহিক অবস্থা নির্বাচন করুণ"
});

tail.select('#partner-color',{
    placeholder: "গাত্রবর্ণ নির্বাচন করুণ"
});

tail.select('#daora-hadith',{
});

tail.select('#takhassur',{
});

tail.select('#partner-district',{
    height: 290,
    search: true,
    locale: "district",
    multiSelectAll: true,
});

tail.select('#partner_financial_status',{
    placeholder: "পারিবারিক/আর্থিক অবস্থা নির্বাচন করুণ"
});

tail.select('#partner_aqida',{
    placeholder: "আকিদা/মাজহাব নির্বাচন করুণ",
    locale: "district",
    multiSelectAll: true,
});





// particlesJS.load('getdetails', '../assets/json/details1.json', function(){
// });

$(function() {
  $(".heart").click(function() {
    $(this).toggleClass("animate");
  });
});
  

document.getElementById('marital-status').addEventListener('change', function() {
    var selected = $('#marital-status').val();
    if(selected.indexOf("ডিভোর্সড") !== -1 ) {
        var sp = document.getElementById('cldren').style.display = 'block';
        var sp = document.getElementById('why-divorced').style.display = 'block';
    }
    else if(selected.indexOf("বিধবা") !== -1) {
        var sp = document.getElementById('cldren').style.display = 'block';
        var sp = document.getElementById('why-divorced').style.display = 'none';
    }
    else{
        var sp = document.getElementById('cldren').style.display = 'none';
        var sp = document.getElementById('why-divorced').style.display = 'none';
    }
});

    
document.getElementById('what-do').addEventListener('change', function() {
   var selected = $('#what-do').val();
   if(selected.indexOf("চাকরি করতেছি") !== -1)  {  
      document.getElementById('job').style.display = 'block';
   }
   if(selected.indexOf("চাকরি করতেছি") === -1){
      document.getElementById('job').style.display = 'none';
   }
   if(selected.indexOf("ব্যবসা করতেছি") !== -1)  {  
      document.getElementById('business').style.display = 'block';
   }
   if(selected.indexOf("ব্যবসা করতেছি") === -1){
      document.getElementById('business').style.display = 'none';
   }
   if(selected.indexOf("চাকরি করতেছি") !== -1 || selected.indexOf("ব্যবসা করতেছি") !== -1)  {  
      document.getElementById('salary').style.display = 'block';
   }
   if(selected.indexOf("চাকরি করতেছি") === -1 && selected.indexOf("ব্যবসা করতেছি") === -1)  {  
      document.getElementById('salary').style.display = 'none';
   }
   if(selected.indexOf("লেখাপড়া") !== -1)  {  
      document.getElementById('study').style.display = 'block';
   }
   if(selected.indexOf("লেখাপড়া") === -1){
      document.getElementById('study').style.display = 'none';
   }
});


document.getElementById('education').addEventListener('change', function() {
    var selected = $('#education').val();
    if(selected.indexOf("লেখাপড়া করিনাই") !== -1) {
        var sp = document.getElementsByClassName('ed');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'none';
        }
        document.getElementById('yed').style.display = 'block';
    }
    else if(selected.indexOf("জেনারেল") !== -1) {
        var sp = document.getElementsByClassName('ed');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
        var sp1 = document.getElementsByClassName('mad');
        for (var i=0; i<sp1.length; i++) {
            sp1[i].style.display = 'none';
        }
        document.getElementById('yed').style.display = 'none';
    }
    else if(selected.indexOf("লেখাপড়া করিনাই") === -1 && selected.indexOf("জেনারেল") === -1){
        var sp = document.getElementsByClassName('ed');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
        var spp = document.getElementsByClassName('mad');
        for (var i=0; i<spp.length; i++) {
            spp[i].style.display = 'block';
        }
        document.getElementById('yed').style.display = 'none';
    }
});


document.getElementById('ssc').addEventListener('change', function() {
    var selected = $('#ssc').val();
    if(selected.indexOf("না") !== -1) {
        var sp = document.getElementById('class').style.display = 'block';
        var sp = document.getElementsByClassName('sp');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'none';
        }
    }
    else if(selected.indexOf("না") === -1) {
        var sp = document.getElementById('class').style.display = 'none';
        var sp = document.getElementsByClassName('sp');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
    }
});

document.getElementById('hsc').addEventListener('change', function() {
    var selected = $('#hsc').val();
    if(selected.indexOf("হ্যাঁ") === -1) {
        var sp = document.getElementsByClassName('hp');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'none';
        }
    }
    else if(selected.indexOf("হ্যাঁ") !== -1) {
        var sp = document.getElementsByClassName('hp');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
    }
});


document.getElementById('graduate').addEventListener('change', function() {
    var selected = $('#graduate').val();
    if(selected.indexOf("হ্যাঁ পড়তেছি") === -1 && selected.indexOf("হ্যাঁ পড়েছি") === -1) {
        var sp = document.getElementsByClassName('gp');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'none';
        }
        var sp = document.getElementsByClassName('gn');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'none';
        }
    }
    else if(selected.indexOf("হ্যাঁ পড়েছি") !== -1) {
        var sp = document.getElementsByClassName('gp');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
        var sp = document.getElementsByClassName('gn');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
    }
    else if(selected.indexOf("হ্যাঁ পড়তেছি") !== -1) {
        var sp = document.getElementsByClassName('gn');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
        var sp = document.getElementsByClassName('gp');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'none';
        }
    }
});


document.getElementById('hafez').addEventListener('change', function() {
   var selected = $('#hafez').val();
   if(selected.indexOf("হিফয করতেছি") !== -1)  {  
      document.getElementById('para').style.display = 'block';
      document.getElementById('hifz').classList.add('col-md-6');
   }
   if(selected.indexOf("হিফয করতেছি") === -1)  {  
      document.getElementById('para').style.display = 'none';
      document.getElementById('hifz').classList.remove('col-md-6');
   }
});


document.getElementById('children').addEventListener('change', function() {
    var selected = $('#children').val();
    if(selected.indexOf("নাই") != -1) {
        document.getElementById('c-address').style.display = 'none';
    }
    else if(selected.indexOf("১") != -1){
        document.getElementById('c-address').style.display = 'block';
        $("#c-address label").html("আপনার সন্তান কি আপনার কাছেই থাকে?")
    }
    else{
        document.getElementById('c-address').style.display = 'block';
        $("#c-address label").html("আপনার সন্তানেরা কি আপনার কাছেই থাকে?")
    }
});

document.getElementById('weakness').addEventListener('change', function() {
    var selected = $('#weakness').val();
    if(selected.indexOf("না") != -1) {
        document.getElementById('about-weak').style.display = 'none';
        document.getElementById('bondha').style.display = 'none';
    }
    else{
        document.getElementById('about-weak').style.display = 'block';
        document.getElementById('bondha').style.display = 'block';
    }
});

document.getElementById('mehnot').addEventListener('change', function() {
    var selected = $('#mehnot').val();
    if(selected.indexOf("না") != -1) {
        document.getElementById('about-mehnot').style.display = 'none';
    }
    else{
        document.getElementById('about-mehnot').style.display = 'block';
    }
});

document.getElementById('brother').addEventListener('change', function() {
    var selected = $('#brother').val();
    if(selected.indexOf("নাই") !== -1) {
        document.getElementById('no-brother').style.display = 'none';
    }
    else if(selected.indexOf("১") !== -1){
        document.getElementById('no-brother').style.display = 'block';
        $("#no-brother label").html("ভাইয়ের সম্পর্কে লিখুন")
    }
    else{
        document.getElementById('no-brother').style.display = 'block';
        $("#no-brother label").html("ভাইদের সম্পর্কে লিখুন")
    }
});

document.getElementById('sister').addEventListener('change', function() {
    var selected = $('#sister').val();
    if(selected.indexOf("নাই") !== -1) {
        document.getElementById('no-sister').style.display = 'none';
    }
    else if(selected.indexOf("১") !== -1){
        document.getElementById('no-sister').style.display = 'block';
        $("#no-sister label").html("বোনের সম্পর্কে লিখুন")
    }
    else{
        document.getElementById('no-sister').style.display = 'block';
        $("#no-sister label").html("বোনদের সম্পর্কে লিখুন")
    }
});

document.getElementById('daora-hadith').addEventListener('change', function() {
    var selected = $('#daora-hadith').val();
    if(selected.indexOf("হ্যাঁ") !== -1) {
        var sp = document.getElementsByClassName('dh');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
    }
    else{
        var sp = document.getElementsByClassName('dh');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'none';
        }
    }
});

document.getElementById('takhassur').addEventListener('change', function() {
    var selected = $('#takhassur').val();
    if(selected.indexOf("হ্যাঁ") !== -1) {
        var sp = document.getElementsByClassName('tak');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'block';
        }
    }
    else{
        var sp = document.getElementsByClassName('tak');
        for (var i=0; i<sp.length; i++) {
            sp[i].style.display = 'none';
        }
    }
});












// $("#smartwizard").on("showStep", function(e, anchorObject, stepNumber, stepDirection, stepPosition) {
//    if(stepPosition === 'last'){
//        $('.sw-btn-prev').show();
//        $('.sw-btn-next').hide();
//    }
//    else if(stepPosition === 'first'){
//        $('.sw-btn-prev').hide();
//        $('.sw-btn-next').show();
//    }else{
//        $('.sw-btn-next').show();
//        $('.sw-btn-prev').show();
//    }
// });

    
var btnFinish = $("<button class='sbmitbtn'></button>")
  .text("Update")
  .addClass("btn btn-fnsh")
  .attr('type', 'submit');
var brr = $("</br>");
//   .on("click", function () {
//       var x = others_education +" "+ dini_qualification;
//     alert(x);
//   });
var btnCancel = $("<button class='mt-2'></button>")
  .text("Cancel")
  .addClass("btn btn-cancel")
  .on("click", function () {
    $("#wizard").smartWizard("reset");
  });



$('#smartwizard').smartWizard({
  selected: 0, // Initial selected step, 0 = first step
  theme: 'default', // theme for the wizard, related css need to include for other than default theme
  justified: true, // Nav menu justification. true/false
  darkMode:false, // Enable/disable Dark Mode if the theme supports. true/false
  autoAdjustHeight: true, // Automatically adjust content height
  keyNavigation: true,
  transitionEffect: 'fade',
  cycleSteps: false, // Allows to cycle the navigation of steps
  backButtonSupport: true, // Enable the back button support
  enableURLhash: true, // Enable selection of the step based on url hash
  transition: {
      animation: 'fade', // Effect on navigation, none/fade/slide-horizontal/slide-vertical/slide-swing
      speed: '400', // Transion animation speed
      easing:'' // Transition animation easing. Not supported without a jQuery easing plugin
  },
  toolbarSettings: {
      toolbarPosition: 'bottom', // none, top, bottom, both
      toolbarButtonPosition: 'center', // left, right, center
      showNextButton: true, // show/hide a Next button
      showPreviousButton: true, // show/hide a Previous button
      toolbarExtraButtons: [brr, btnFinish], // Extra buttons to show on toolbar, array of jQuery input/buttons elements
  },
  anchorSettings: {
      anchorClickable: true, // Enable/Disable anchor navigation
      enableAllAnchors: true, // Activates all anchors clickable all times
      markDoneStep: true, // Add done state on navigation
      markAllPreviousStepsAsDone: false, // When a step selected by url hash, all previous steps are marked done
      removeDoneStepOnNavigateBack: false, // While navigate back done step after active step will be cleared
      enableAnchorOnDoneStep: true // Enable/Disable the done steps navigation
  },
  keyboardSettings: {
      keyNavigation: false, // Enable/Disable keyboard navigation(left and right keys are used if enabled)
      keyLeft: [37], // Left key code
      keyRight: [39] // Right key code
  },
  lang: { // Language variables for button
      next: '→',
      previous: '←'
  },
  disabledSteps: [], // Array Steps disabled
  errorSteps: [], // Highlight step with errors
  hiddenSteps: [], // Hidden steps
})








// const textarea1 = document.getElementById("textarea1");
// const textarea2 = document.getElementById("textarea2");
// const textarea3 = document.getElementById("textarea3");
// const textarea4 = document.getElementById("textarea4");
// const textarea5 = document.getElementById("textarea5");

// function setHeight(elemnt) {
//   const style = getComputedStyle(elemnt, null);
//   const verticalBorders = Math.round(parseFloat(style.borderTopWidth) + parseFloat(style.borderBottomWidth));
//   const maxHeight = parseFloat(style.maxHeight) || 300;
  
//   elemnt.style.height = "auto";

//   const newHeight = elemnt.scrollHeight + verticalBorders;
  
//   elemnt.style.overflowY = newHeight > maxHeight ? "auto" : "hidden";
//   elemnt.style.height = Math.min(newHeight, maxHeight) + "px";
// }

// textarea1.addEventListener("input", (e) => {
//   setHeight(e.target);
// });

// textarea2.addEventListener("input", (e) => {
//   setHeight(e.target);
// });

// textarea3.addEventListener("input", (e) => {
//   setHeight(e.target);
// });

// textarea4.addEventListener("input", (e) => {
//   setHeight(e.target);
// });

// textarea5.addEventListener("input", (e) => {
//   setHeight(e.target);
// });

// setHeight(textarea1);
// setHeight(textarea2);
// setHeight(textarea3);
// setHeight(textarea4);
// setHeight(textarea5);




// new_scroll = 0
// old_scroll = 0
// $(".get-details").scroll( function() { 
//  var scrolled_val = $(".get-details").scrollTop().valueOf();
//  new_scroll = scrolled_val;
//  if(new_scroll > old_scroll){
//     $(".get-details .nav").removeClass( "up" );
//  }
//  else{
//     $(".get-details .nav").addClass( "up" );
//  }
//  old_scroll = new_scroll;
// });













// ******************************************************************************************

// $('.cng').on('change', function (){

//     const val = [];
//     $('#what-do :selected').each(function(i, sel){
//         valu = " "+$(sel).val();
//         if (valu == ' study'){
//             valu = 'ছাত্রী';
//             document.getElementById('study').style.display = 'block';
//         }
//         else if (valu == ' job'){
//             valu = 'চাকরি';
//         }
//         else if (valu == ' seek-job'){
//             valu = 'চাকরি খুঁজছি';
//         }
//         else if (valu == ' business'){
//             valu = 'ব্যবসা';
//         }
//         val.push(valu);
//     });
//     if(val.length === 0){
//         $('.work').text("--");
//     }
//     else{
//         $('.work').text(val);
//     }

//     $('#partner-marital-status :selected').each(function(i, sel){
//         valu = $(sel).val();
//         val.push(valu);
//     });
//     if(val.indexOf("বিবাহিত") === -1){
//         document.getElementById('masna').style.display = 'none';
//     }
//     else{
//         document.getElementById('masna').style.display = 'block';
//     }

//     var selected = $('#marital-status').val();
//     if(selected.indexOf("ডিভোর্সড") !== -1 ) {
//         var sp = document.getElementById('cldren').style.display = 'block';
//         var sp = document.getElementById('why-divorced').style.display = 'block';
//     }
//     else if(selected.indexOf("বিধবা") !== -1) {
//         var sp = document.getElementById('cldren').style.display = 'block';
//         var sp = document.getElementById('why-divorced').style.display = 'none';
//     }
//     else{
//         var sp = document.getElementById('cldren').style.display = 'none';
//         var sp = document.getElementById('why-divorced').style.display = 'none';
//     }

//    var selected = $('#what-do').val();
//    if(selected.indexOf("চাকরি করতেছি") !== -1)  {  
//       document.getElementById('job').style.display = 'block';
//    }
//    if(selected.indexOf("চাকরি করতেছি") === -1){
//       document.getElementById('job').style.display = 'none';
//    }
//    if(selected.indexOf("ব্যবসা করতেছি") !== -1)  {  
//       document.getElementById('business').style.display = 'block';
//    }
//    if(selected.indexOf("ব্যবসা করতেছি") === -1){
//       document.getElementById('business').style.display = 'none';
//    }
//    if(selected.indexOf("চাকরি করতেছি") !== -1 || selected.indexOf("ব্যবসা করতেছি") !== -1)  {  
//       document.getElementById('salary').style.display = 'block';
//    }
//    if(selected.indexOf("চাকরি করতেছি") === -1 && selected.indexOf("ব্যবসা করতেছি") === -1)  {  
//       document.getElementById('salary').style.display = 'none';
//    }
//    if(selected.indexOf("লেখাপড়া") !== -1)  {  
//       document.getElementById('study').style.display = 'block';
//    }
//    if(selected.indexOf("লেখাপড়া") === -1){
//       document.getElementById('study').style.display = 'none';
//    }

//     var selected = $('#education').val();
//     if(selected.indexOf("লেখাপড়া করিনাই") !== -1) {
//         var sp = document.getElementsByClassName('ed');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'none';
//         }
//         document.getElementById('yed').style.display = 'block';
//     }
//     else if(selected.indexOf("জেনারেল") !== -1) {
//         var sp = document.getElementsByClassName('ed');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'block';
//         }
//         var sp1 = document.getElementsByClassName('mad');
//         for (var i=0; i<sp1.length; i++) {
//             sp1[i].style.display = 'none';
//         }
//         document.getElementById('yed').style.display = 'none';
//     }
//     else if(selected.indexOf("লেখাপড়া করিনাই") === -1 && selected.indexOf("জেনারেল") === -1){
//         var sp = document.getElementsByClassName('ed');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'block';
//         }
//         var spp = document.getElementsByClassName('mad');
//         for (var i=0; i<spp.length; i++) {
//             spp[i].style.display = 'block';
//         }
//         document.getElementById('yed').style.display = 'none';
//     }

//     var selected = $('#ssc').val();
//     if(selected.indexOf("না") !== -1) {
//         var sp = document.getElementById('class').style.display = 'block';
//         var sp = document.getElementsByClassName('sp');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'none';
//         }
//     }
//     else if(selected.indexOf("না") === -1) {
//         var sp = document.getElementById('class').style.display = 'none';
//         var sp = document.getElementsByClassName('sp');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'block';
//         }
//     }

//     var selected = $('#hsc').val();
//     if(selected.indexOf("হ্যাঁ") === -1) {
//         var sp = document.getElementsByClassName('hp');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'none';
//         }
//     }
//     else if(selected.indexOf("হ্যাঁ") !== -1) {
//         var sp = document.getElementsByClassName('hp');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'block';
//         }
//     }

//     var selected = $('#graduate').val();
//     if(selected.indexOf("হ্যাঁ পড়তেছি") === -1 && selected.indexOf("হ্যাঁ পড়েছি") === -1) {
//         var sp = document.getElementsByClassName('gp');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'none';
//         }
//     }
//     else if(selected.indexOf("হ্যাঁ পড়তেছি") === -1 && selected.indexOf("হ্যাঁ পড়েছি") !== -1) {
//         var sp = document.getElementsByClassName('gp');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'block';
//         }
//     }
//     else if(selected.indexOf("হ্যাঁ পড়তেছি") !== -1 && selected.indexOf("হ্যাঁ পড়েছি") === -1) {
//         var sp = document.getElementsByClassName('gp');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'block';
//             document.getElementById("graduate-year").style.display = "none";
//         }
//     }

//    var selected = $('#hafez').val();
//    if(selected.indexOf("হিফয করতেছি") !== -1)  {  
//       document.getElementById('para').style.display = 'block';
//       document.getElementById('hifz').classList.add('col-md-6');
//    }
//    if(selected.indexOf("হিফয করতেছি") === -1)  {  
//       document.getElementById('para').style.display = 'none';
//       document.getElementById('hifz').classList.remove('col-md-6');
//    }

//     var selected = $('#children').val();
//     if(selected.indexOf("নাই") != -1) {
//         document.getElementById('c-address').style.display = 'none';
//     }
//     else if(selected.indexOf("১") != -1){
//         document.getElementById('c-address').style.display = 'block';
//         $("#c-address label").html("আপনার সন্তান কি আপনার কাছেই থাকে?")
//     }
//     else{
//         document.getElementById('c-address').style.display = 'block';
//         $("#c-address label").html("আপনার সন্তানেরা কি আপনার কাছেই থাকে?")
//     }

//     var selected = $('#weakness').val();
//     if(selected.indexOf("না") != -1) {
//         document.getElementById('about-weak').style.display = 'none';
//     }
//     else{
//         document.getElementById('about-weak').style.display = 'block';
//     }

//     var selected = $('#mehnot').val();
//     if(selected.indexOf("না") != -1) {
//         document.getElementById('about-mehnot').style.display = 'none';
//     }
//     else{
//         document.getElementById('about-mehnot').style.display = 'block';
//     }

//     var selected = $('#brother').val();
//     if(selected.indexOf("নাই") !== -1) {
//         document.getElementById('no-brother').style.display = 'none';
//     }
//     else if(selected.indexOf("১") !== -1){
//         document.getElementById('no-brother').style.display = 'block';
//         $("#no-brother label").html("ভাইয়ের সম্পর্কে লিখুন")
//     }
//     else{
//         document.getElementById('no-brother').style.display = 'block';
//         $("#no-brother label").html("ভাইদের সম্পর্কে লিখুন")
//     }

//     var selected = $('#sister').val();
//     if(selected.indexOf("নাই") !== -1) {
//         document.getElementById('no-sister').style.display = 'none';
//     }
//     else if(selected.indexOf("১") !== -1){
//         document.getElementById('no-sister').style.display = 'block';
//         $("#no-sister label").html("বোনের সম্পর্কে লিখুন")
//     }
//     else{
//         document.getElementById('no-sister').style.display = 'block';
//         $("#no-sister label").html("বোনদের সম্পর্কে লিখুন")
//     }

//     var selected = $('#daora-hadith').val();
//     if(selected.indexOf("হ্যাঁ") !== -1) {
//         var sp = document.getElementsByClassName('dh');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'block';
//         }
//     }
//     else{
//         var sp = document.getElementsByClassName('dh');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'none';
//         }
//     }

//     var selected = $('#takhassur').val();
//     if(selected.indexOf("হ্যাঁ") !== -1) {
//         var sp = document.getElementsByClassName('tak');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'block';
//         }
//     }
//     else{
//         var sp = document.getElementsByClassName('tak');
//         for (var i=0; i<sp.length; i++) {
//             sp[i].style.display = 'none';
//         }
//     }
// });