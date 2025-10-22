<html>
<body>

<form method="GET">
Number A: <input type="text" name="num_a"><br>
Number B: <input type="text" name="num_b"><br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$a = $_GET["num_a"] ?? 10;
$b = $_GET["num_b"] ?? 12;

echo "$a + $b = " . $a + $b . "<br>";
echo "$a - $b = " . $a - $b . "<br>";
echo "$a * $b = " . $a * $b . "<br>";
echo "$a / $b = " . $a / $b;

?>

<link rel="stylesheet" type="text/css" href="style.css">