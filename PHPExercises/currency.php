<html>
<body>

<form action="currency.php" method="GET">
PHP <input type="text" name="pesos"><br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$php = $_GET["pesos"] ?? 100;

$usd = number_format($php * 0.017,2);
$eur = number_format($php * 0.015,2);
$jpy = number_format($php * 2.63,2);

echo "Exchange Rates<br><br>";
echo "PHP $php &rarr; USD $usd <br>
PHP $php &rarr; EUR $eur <br>
PHP $php &rarr; JPY $jpy";

?>

<link rel="stylesheet" type="text/css" href="style.css">