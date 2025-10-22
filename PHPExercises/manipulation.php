<html>
<body>

<form method="GET">
<p>Type a sentence:</p>
<textarea name="sentence" rows="5" cols="40"></textarea><br><br>
<input type="submit">
</form>

<hr>
<br><br>

</body>
</html>

<?php

$sentence = $_GET["sentence"] ??
"According to all known laws of aviation, there is no way a bee should be able to fly.";

echo $sentence;
echo "<br><br> number of characters: " . strlen($sentence);
echo "<br> number of words: " . str_word_count($sentence);
echo "<br> uppercase: " . strtoupper($sentence);
echo "<br> lowercase: " . strtolower($sentence);

?>

<link rel="stylesheet" type="text/css" href="style.css">