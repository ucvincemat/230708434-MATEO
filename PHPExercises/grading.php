<html>
<body>

<form method="GET">
Math Score: <input type="text" name="math_scr"><br>
English Score: <input type="text" name="eng_scr"><br>
Science Score: <input type="text" name="sci_scr"><br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$math_score = $_GET["math_scr"] ?? 75;
$english_score = $_GET["eng_scr"] ?? 86;
$science_score = $_GET["sci_scr"] ?? 90;

$average = (int)(($math_score + $english_score + $science_score) / 3);

echo "Grade: $average";
echo "<br>Rank: ";
if ($average>=90) {
    echo  "A";
} elseif ($average>=80) {
    echo "B";
} elseif ($average>=75) {
    echo "C";
} else {
    echo "F";
}

?>

<link rel="stylesheet" type="text/css" href="style.css">