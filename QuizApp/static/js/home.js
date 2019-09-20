$(document).ready(function() {
	var id = 1;
	$(window).on('load', function(){
		$("#1").show();
	});
	$("#btn_next").on('click', function(){
		var a = $(".question_number").text();
		console.log(a);
		$("#1").hide();
		$("#2").show();
	})
	$("#btn_prev").on('click', function(){
		var a = $(".question_number").text();
		console.log(a);
		$("#2").hide();
		$("#1").show();
	})

})