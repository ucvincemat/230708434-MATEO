<html>
<body>

<form method="GET">
<p>Rectangle</p>
Length: <input type="text" name="length"><br>
Width: <input type="text" name="width"><br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$length = $_GET["length"] ?? 5;
$width = $_GET["width"] ?? 7;

$area = $length * $width;
$perimeter = 2 * ($length + $width);

echo "A rectangle that is $length long and $width wide has: <br>
<ol><li>An area of $area </li>
<li>A perimeter of $perimeter </li></ol>";

?>

<link rel="stylesheet" type="text/css" href="style.css">