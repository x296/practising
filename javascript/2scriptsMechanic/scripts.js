var actualSlide = Math.floor(Math.random()*3)+1;
var timer1 = 0;
var timer2 = 0;

function setSlide(slideNr) {
	clearTimeout(timer1);
	clearTimeout(timer2);
	actualSlide = slideNr-1;
	hide();
	setTimeout("changeSlide()", 500);
}

function hide() {
	$("#slider").fadeOut(500)
}

function changeSlide() {
	actualSlide ++; if (actualSlide > 3) actualSlide = 1;
	var file = "<img src=\"pic" + actualSlide + ".jpg\" />";
	document.getElementById("slider").innerHTML = file;
	$("#slider").fadeIn(500)

	timer1 = setTimeout("changeSlide()", 5000);
	timer2 = setTimeout("hide()", 4500)
}