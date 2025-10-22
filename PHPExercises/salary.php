<html>
<body>

<form method="GET">
Earning a basic salary of <input type="text" name="basic_salary"> and an allowance of <input type="text" name="allowance"> with a deduction of <input type="text" name="deduction"><br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$basic_salary = $_GET["basic_salary"] ?? 3000;
$allowance = $_GET["allowance"] ?? 1000;
$deduction = $_GET["deduction"] ?? 500;

$net_salary = $basic_salary + $allowance - $deduction;

echo "You have a net salary of <b>$net_salary</b>.";

?>

<link rel="stylesheet" type="text/css" href="style.css">