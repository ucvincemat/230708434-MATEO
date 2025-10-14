<?php

$math_score = 75;
$english_score = 86;
$science_score = 90;

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