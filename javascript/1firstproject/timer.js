function counting() {
	var currentDate = new Date();
	
	var second = currentDate.getSeconds();
	if (second<10) second = '0'+second;
	var minute = currentDate.getMinutes();
	if (minute<10) minute = '0'+minute;
	var hour = currentDate.getHours();
	if (hour<10) hour = '0'+hour;
	
	var day = currentDate.getDate();
	var month = currentDate.getMonth()+1;
	if (month<10) month = '0'+month;
	var year = currentDate.getFullYear();

	document.getElementById("clock").innerHTML = day+'/'+month+'/'+year+' | '+hour+':'+minute+':'+second;

	setTimeout("counting()", 1000);
}