<?php

$weight = 50;
$height = 1.65;

$bmi = number_format($weight / ($height * $height),1);

echo "If you weight $weight kilogram, and is $height meters high,<br>You have a BMI of <b>$bmi</b>."

?>

<link rel="stylesheet" type="text/css" href="style.css">