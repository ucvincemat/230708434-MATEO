<html>
<body>

<form method="GET">
Distance: <input type="text" name="distance"> km<br>
Consumption Rate: <input type="text" name="fuel_consumption"> km/L<br>
Price of Gas: <input type="text" name="fuel_price"> PHP/L<br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$distance = $_GET["distance"] ?? 100 /* km */;
$fuel_consumption = $_GET["fuel_consumption"] ?? 12 /* km/L */;
$fuel_price = $_GET["fuel_price"] ?? 172 /* PHP/L */;

$cost = number_format(($distance / $fuel_consumption) * $fuel_price, 2);

echo "Total Cost: PHP $cost";
?>

<link rel="stylesheet" type="text/css" href="style.css">