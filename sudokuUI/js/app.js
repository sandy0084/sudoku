$(function() {
	
	$(document).on("click", "#sendValue", function(e) {
		var valuesArray = {};
		valuesArray["sudoku"] = {};
		
		$(".case").each(function(index) {
			var id =    $(this).attr('id');
			var value = $(this).find('input').val();
			
			/*if (value=="")
			value = "X";*/
			
			valuesArray["sudoku"][id] = value;
		});
		json = JSON.stringify(valuesArray);
		
		$.ajax({
		  url : "http://127.0.0.1:8000/demo",
		  type : "POST",
		  data : { json : json},
		  success : function(response){
		       console.log(response);
			  remplirSudoku(response);
		  }
		});
		
	});

	$(document).on("click", "#remplirTest", function(e) {
		var jsonTest = '{"sudoku":{"10":"1","11":"","12":"8","13":"","14":"","15":"6","16":"","17":"","18":"","20":"","21":"4","22":"","23":"","24":"8","25":"","26":"","27":"","28":"","30":"","31":"1","32":"","33":"","34":"","35":"4","36":"3","37":"","38":"","40":"","41":"","42":"","43":"","44":"","45":"7","46":"","47":"1","48":"2","50":"","51":"2","52":"","53":"3","54":"","55":"8","56":"9","57":"","58":"","60":"8","61":"","62":"4","63":"","64":"6","65":"5","66":"","67":"","68":"1","70":"9","71":"","72":"","73":"","74":"7","75":"","76":"","77":"4","78":"3","80":"","81":"","82":"","83":"","84":"4","85":"","86":"5","87":"6","88":"","00":"3","01":"","02":"","03":"","04":"5","05":"","06":"","07":"2","08":""}}';
		remplirSudoku(jsonTest);
	});	
	
	$(document).on("click", "#clear", function(e) {
		viderSudoku();
	});
	
	$(document).ready(function() {
		loadSudoku();
	});

	function loadSudoku(){
		var json = '{"sudoku":{"10":1,"11":"","12":8,"13":"","14":"","15":6,"16":"","17":"","18":"","20":"","21":4,"22":"","23":"","24":8,"25":"","26":"","27":"","28":"","30":"","31":1,"32":"","33":"","34":"","35":4,"36":3,"37":"","38":"","40":"","41":"","42":"","43":"","44":"","45":7,"46":"","47":1,"48":2,"50":"","51":2,"52":"","53":3,"54":"","55":8,"56":9,"57":"","58":"","60":8,"61":"","62":4,"63":"","64":6,"65":5,"66":"","67":"","68":1,"70":9,"71":"","72":"","73":"","74":7,"75":"","76":"","77":4,"78":3,"80":"","81":"","82":"","83":"","84":4,"85":"","86":5,"87":6,"88":"","00":3,"01":"","02":"","03":"","04":5,"05":"","06":"","07":2,"08":""}}';
		remplirSudoku(json,true);
	}
	
	function remplirSudoku(json,first=false) {
		var obj = JSON.parse(json);
		
		$(".case").each(function(index) {
			var id = $(this).attr('id');
			$(this).find('input').val(obj["sudoku"][id]);
			if (first && obj["sudoku"][id]!="")
			    $(this).find('input').attr('style','color:blue;');
		});
	}	

	function viderSudoku() {
		$(".case").each(function(index) {
			$(this).find('input').val("");
		});
	}
});
