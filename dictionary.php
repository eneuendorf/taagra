<!doctype html>
<html lang="en">

	<head>
		<meta charset="utf-8">
		<title>The Ta'agra Project</title>
		<meta http-equiv="x-ua-compatible" content="ie=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

		<!-- Stylesheets -->
		<link rel="stylesheet" href="css/normalize.css">
		<link rel="stylesheet" href="css/styles.css">
		<link href="https://fonts.googleapis.com/css?family=Medula+One&#124;Forum&#124;Open+Sans" rel="stylesheet">
		<link rel="stylesheet" href="//use.fontawesome.com/releases/v5.0.7/css/all.css">




		<!--[if lte IE 9]>
			<p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/">upgrade your browser</a> to improve your experience and security.</p>
		<![endif]-->
	<link href="https://fonts.googleapis.com/css?family=Encode+Sans+Condensed" rel="stylesheet">
    <link rel="shortcut icon" type="image/ico" href="images/favicon.ico"/>
	</head>

	<body>

<?php include("header.php"); ?>

<main class="content_main search_form">


<form action="dict_web.cgi" method="post">
	<h1 class="content_title">Ta'agra Dictionary</h1>	

	<div class="search_tools">

	<div class="search_bar">
	<input type="text" name="search_term" autocomplete="off" placeholder="  What would you like to search..."><br>
    	<button type="submit" class="submit_button"><i class="fas fa-search"></i></button>
	</div>
	<label class="switch">
		<input type="checkbox" id="togBtn" name="language" value="taagra">
		<div class="slider round">
		<span class="tag">TA'AGRA</span><span class="eng">ENGLISH</span>
		</div>
	</label>

	</div>

</form>


</main>

<script>
/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
</script>

	</body>
</html>
