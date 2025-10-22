<html>
<body>

<form method="GET">
Name: <input type="text" name="name"><br>
Age: <input type="text" name="age"><br>
Favorite Color: <input type="text" name="favorite_color"><br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$name = $_GET["name"] ?? 'Vince';
$age = $_GET["age"] ?? 22;
$favorite_color = $_GET["favorite_color"] ?? 'blue';

echo "Hi, I'm <b>$name</b>, I am <b>$age</b> years old, and my favorite color is <b>$favorite_color</b>.";

?>

<link rel="stylesheet" type="text/css" href="style.css">