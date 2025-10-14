<?php

$distance = 100 /* km */;
$fuel_consumption = 12 /* km/L */;
$fuel_price = 172 /* PHP/L */;

$cost = number_format(($distance / $fuel_consumption) * $fuel_price, 2);

echo "Distance: $distance km<br>
Fuel Consumption: $fuel_consumption km/L<br>
Fuel Price: $fuel_price PHP/L<br><br>
Total Cost: PHP $cost";
?>

<link rel="stylesheet" type="text/css" href="style.css">