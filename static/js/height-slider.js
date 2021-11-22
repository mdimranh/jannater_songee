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

$('input[type="range"]').rangeslider({
  // Feature detection the default is `true`.
  // Set this to `false` if you want to use
  // the polyfill also in Browsers which support
  // the native <input type="range"> element.
  polyfill: false,

  // Default CSS classes
  rangeClass: "rangeslider",
  disabledClass: "rangeslider--disabled",
  horizontalClass: "rangeslider--horizontal",
  fillClass: "rangeslider__fill",
  handleClass: "rangeslider__handle",

  // Callback function
  onInit: function () {
    $rangeEl = this.$range;
    // add value label to handle
    var $handle = $rangeEl.find(".rangeslider__handle");
    let height = this.value;
    let feet = Math.floor(height / 12);
    let inches = height - feet * 12;
    var feetnumberbn = feet.toString().getDigitBanglaFromEnglish();
    var inchesnumberbn = inches.toString().getDigitBanglaFromEnglish();
    var vlubn = vlu.toString().getDigitBanglaFromEnglish();
    var handleValue =
      '<div class="rangeslider__handle__value">' + feetnumberbn + "'" + inchesnumberbn + "''" + "</div>";
    $handle.append(handleValue);

    // get range index labels
    var rangeLabels = this.$element.attr("labels");
    rangeLabels = rangeLabels.split(", ");

    // add labels
    $rangeEl.append('<div class="rangeslider__labels"></div>');
    $(rangeLabels).each(function (index, value) {
      $rangeEl
        .find(".rangeslider__labels")
        .append(
          '<span class="rangeslider__labels__label">' + value + "</span>"
        );
    });
  },

  // Callback function
  onSlide: function (position, value) {
    var $handle = this.$range.find(".rangeslider__handle__value");
    let height = this.value;
    let feet = Math.floor(height / 12);
    let inches = height - feet * 12;
    var feetnumberbn = feet.toString().getDigitBanglaFromEnglish();
    var inchesnumberbn = inches.toString().getDigitBanglaFromEnglish();
    $handle.text(feetnumberbn + "'" + inchesnumberbn + "''");
    $(".height").text(feetnumberbn + "'" + inchesnumberbn + "''");
  },

  // Callback function
  onSlideEnd: function (position, value) {},
});
