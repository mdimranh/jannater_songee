const allbtn = ["#all", "#male", "#female", "#couple", "#suggest", "#love", "#masala", "#notificationbtn", '.profile'];
        const contnt = ["সকল বায়োডাটা", "পাত্রের বায়োডাটাসমূহ", "পাত্রীর বায়োডাটাসমূহ", "সফলতার গল্প", "প্রস্তাবিত বায়োডাটাসমূহ", "পছন্দের বায়োডাটাসমূহ", "মাসআলা", "নোটিফিকেশান", 'প্রোফাইল'];
        for (key in allbtn) {
        tippy(allbtn[key], {
            content: contnt[key],
            arrow: true,
            animation: 'scale-extreme',
            offset: [0, 20],
            theme: 'light',
            hideOnClick: true,
        });
        }

tippy("#emailtoast", {
  content: '<strong>Bolded <span style="color: aqua;">content</span></strong>',
  allowHTML: true,
});