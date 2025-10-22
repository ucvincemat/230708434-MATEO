<html>
<body>

<form method="GET">
<input type="text" name="celcius"> &deg;C <br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$celsius = $_GET["celcius"] ?? 30;

$fahrenheit = ($celsius * 9 / 5) + 32;

echo "<b>$celsius&deg;C</b> (degrees Celcius) is <b>$fahrenheit&deg;F (degrees Fahrenheit)</b>."

?>

<link rel="stylesheet" type="text/css" href="style.css">