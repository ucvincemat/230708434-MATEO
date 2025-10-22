<html>
<body>

<form method="GET">
Weight: <input type="text" name="weight"> kg<br>
Height: <input type="text" name="height"> m<br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$weight = $_GET["weight"] ?? 50;
$height = $_GET["height"] ?? 1.65;

$bmi = number_format($weight / ($height * $height),1);

echo "If you weight $weight kilogram, and is $height meters high,<br><br>You have a BMI of <b>$bmi</b>."

?>

<link rel="stylesheet" type="text/css" href="style.css">