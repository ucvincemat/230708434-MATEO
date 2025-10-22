<html>
<body>

<form method="GET">
First is: <input type="text" name="first"><br>
Second is: <input type="text" name="second"><br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$var1 = $_GET["first"] ?? 67;
$var2 = $_GET["second"] ?? 69;

echo "You say First is <b>$var1</b>, then Second is <b>$var2</b>";

$temp = $var1;
$var1 = $var2;
$var2 = $temp;

echo "<br>but maybe the First is <b>$var1</b>, then Second is <b>$var2</b>?";

?>

<link rel="stylesheet" type="text/css" href="style.css">