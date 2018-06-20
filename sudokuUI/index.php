<!doctype html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Sudoku Solver</title>
		<link href="img/favicon.ico" rel="shortcut icon" type="image/x-icon">
		<link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800" rel="stylesheet"> 
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
		<link rel="stylesheet" href="css/style.css">
	</head>
	<body>
	
	
		<table class="global">
			<tr>
				<td id="A">
					<table>
						<tr>
							<td id="00"><input type="text" maxlength="1"></td>
							<td id="10"><input type="text" maxlength="1"></td>
							<td id="20"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="01"><input type="text" maxlength="1"></td>
							<td id="11"><input type="text" maxlength="1"></td>
							<td id="21"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="02"><input type="text" maxlength="1"></td>
							<td id="12"><input type="text" maxlength="1"></td>
							<td id="22"><input type="text" maxlength="1"></td>
						</tr>
					</table>
				</td>
				<td id="B">
					<table>
						<tr>
							<td id="30"><input type="text" maxlength="1"></td>
							<td id="40"><input type="text" maxlength="1"></td>
							<td id="50"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="31"><input type="text" maxlength="1"></td>
							<td id="41"><input type="text" maxlength="1"></td>
							<td id="51"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="32"><input type="text" maxlength="1"></td>
							<td id="42"><input type="text" maxlength="1"></td>
							<td id="52"><input type="text" maxlength="1"></td>
						</tr>
					</table>					
				</td>
				<td id="C">
					<table>
						<tr>
							<td id="60"><input type="text" maxlength="1"></td>
							<td id="70"><input type="text" maxlength="1"></td>
							<td id="80"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="61"><input type="text" maxlength="1"></td>
							<td id="71"><input type="text" maxlength="1"></td>
							<td id="81"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="62"><input type="text" maxlength="1"></td>
							<td id="72"><input type="text" maxlength="1"></td>
							<td id="82"><input type="text" maxlength="1"></td>
						</tr>
					</table>					
				</td>
			</tr>		
			<tr>
				<td id="D">
					<table>
						<tr>
							<td id="03"><input type="text" maxlength="1"></td>
							<td id="13"><input type="text" maxlength="1"></td>
							<td id="23"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="04"><input type="text" maxlength="1"></td>
							<td id="14"><input type="text" maxlength="1"></td>
							<td id="24"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="05"><input type="text" maxlength="1"></td>
							<td id="15"><input type="text" maxlength="1"></td>
							<td id="25"><input type="text" maxlength="1"></td>
						</tr>
					</table>					
				</td>
				<td id="E">
					<table>
						<tr>
							<td id="33"><input type="text" maxlength="1"></td>
							<td id="43"><input type="text" maxlength="1"></td>
							<td id="53"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="34"><input type="text" maxlength="1"></td>
							<td id="44	"><input type="text" maxlength="1"></td>
							<td id="54"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="35"><input type="text" maxlength="1"></td>
							<td id="45"><input type="text" maxlength="1"></td>
							<td id="55"><input type="text" maxlength="1"></td>
						</tr>
					</table>					
				</td>
				<td id="F">
					<table>
						<tr>
							<td id="63"><input type="text" maxlength="1"></td>
							<td id="73"><input type="text" maxlength="1"></td>
							<td id="83"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="64"><input type="text" maxlength="1"></td>
							<td id="74"><input type="text" maxlength="1"></td>
							<td id="84"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="65"><input type="text" maxlength="1"></td>
							<td id="75"><input type="text" maxlength="1"></td>
							<td id="85"><input type="text" maxlength="1"></td>
						</tr>
					</table>					
				</td>
			</tr>		
			<tr>
				<td id="G">
					<table>
						<tr>
							<td id="06"><input type="text" maxlength="1"></td>
							<td id="16"><input type="text" maxlength="1"></td>
							<td id="26"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="07"><input type="text" maxlength="1"></td>
							<td id="17"><input type="text" maxlength="1"></td>
							<td id="27"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="08"><input type="text" maxlength="1"></td>
							<td id="18"><input type="text" maxlength="1"></td>
							<td id="28"><input type="text" maxlength="1"></td>
						</tr>
					</table>					
				</td>
				<td id="H">
					<table>
						<tr>
							<td id="36"><input type="text" maxlength="1"></td>
							<td id="46"><input type="text" maxlength="1"></td>
							<td id="56"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="37"><input type="text" maxlength="1"></td>
							<td id="47"><input type="text" maxlength="1"></td>
							<td id="57"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="38"><input type="text" maxlength="1"></td>
							<td id="48"><input type="text" maxlength="1"></td>
							<td id="58"><input type="text" maxlength="1"></td>
						</tr>
					</table>					
				</td>
				<td id="I">
					<table>
						<tr>
							<td id="66"><input type="text" maxlength="1"></td>
							<td id="76"><input type="text" maxlength="1"></td>
							<td id="86"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="67"><input type="text" maxlength="1"></td>
							<td id="77"><input type="text" maxlength="1"></td>
							<td id="87"><input type="text" maxlength="1"></td>
						</tr>		
						<tr>
							<td id="68"><input type="text" maxlength="1"></td>
							<td id="78"><input type="text" maxlength="1"></td>
							<td id="88"><input type="text" maxlength="1"></td>
						</tr>
					</table>					
				</td>
			</tr>
		</table>
		

	
	
		<script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
		<script src="js/app.js"></script>
	</body>
</html>