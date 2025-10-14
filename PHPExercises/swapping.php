<?php

$var1 = 67;
$var2 = 69;

echo "First is <b>$var1</b>, then Second is <b>$var2</b>";

$temp = $var1;
$var1 = $var2;
$var2 = $temp;

echo "<br>but maybe the First is <b>$var1</b>, then Second is <b>$var2</b>?";

?>

<link rel="stylesheet" type="text/css" href="style.css">