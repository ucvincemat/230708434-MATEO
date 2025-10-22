<?php

$balance = $_GET["balance"] ?? 2000;
$mode = $_GET["transaction"] ?? "deposit";
$amount = $_GET["amount"] ?? 0;

if ($mode == "withdraw") {
    $balance = $balance - $amount;
} else $balance = $balance + $amount;

echo "Current Balance: $balance";

?>

<html>
<body>
<br><br>
<hr>

<form method="GET">
Transaction: <select name="transaction">
  <option value="deposit">Deposit</option>
  <option value="withdraw">Withdraw</option>
</select>
Amount: <input type="number" name="amount"><br>
<input type="hidden" name="balance" value = <?php echo $balance ?>>
<input type="submit">
</form>

</body>
</html>

<link rel="stylesheet" type="text/css" href="style.css">