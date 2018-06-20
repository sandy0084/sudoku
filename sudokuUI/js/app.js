$(function() {
	
	$(document).on("click", "#sendValue", function(e) {
		var valuesArray = {};
		
		$(".case").each(function(index) {
			var id =    $(this).attr('id');
			var value = $(this).find('input').val();
			
			if (value=="")
				value = "X";
			
			valuesArray[id] = value;
		});
		console.log(valuesArray);
		console.log(JSON.stringify(valuesArray));
	});
	
	$(document).on("click", "#remplirTest", function(e) {
		var jsonTest = '{ "sudoku" : { "00" : "1", "01" : "2", "02" : "3", "03" : "4", "04" : "5", "05" : "6", "06" : "7", "07" : "8", "08" : "9", "10" : "1", "11" : "2", "12" : "3", "13" : "4", "14" : "5", "15" : "6", "16" : "7", "17" : "8", "18" : "9", "20" : "1", "21" : "2", "22" : "3", "23" : "4", "24" : "5", "25" : "6", "26" : "7", "27" : "8", "28" : "9", "30" : "1", "31" : "2", "32" : "3", "33" : "4", "34" : "5", "35" : "6", "36" : "7", "37" : "8", "38" : "9", "40" : "1", "41" : "2", "42" : "3", "43" : "4", "44" : "5", "45" : "6", "46" : "7", "47" : "8", "48" : "9", "50" : "1", "51" : "2", "52" : "3", "53" : "4", "54" : "5", "55" : "6", "56" : "7", "57" : "8", "58" : "9", "60" : "1", "61" : "2", "62" : "3", "63" : "4", "64" : "5", "65" : "6", "66" : "7", "67" : "8", "68" : "9", "70" : "1", "71" : "2", "72" : "3", "73" : "4", "74" : "5", "75" : "6", "76" : "7", "77" : "8", "78" : "9", "80" : "1", "81" : "2", "82" : "3", "83" : "4", "84" : "5", "85" : "6", "86" : "7", "87" : "8", "88" : "9" } }';
		remplirSudoku(jsonTest);
	});
	
	function remplirSudoku(json) {
		var obj = JSON.parse(json);
		
		console.log(obj);
		
		$(".case").each(function(index) {
			var id = $(this).attr('id');
			$(this).find('input').val(obj.sudoku.id);
		});
	}
});
