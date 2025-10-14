<?php

$sentence = "According to all known laws of aviation, there is no way a bee should be able to fly.";

echo $sentence;
echo "<br><br> number of characters: " . strlen($sentence);
echo "<br> number of words: " . str_word_count($sentence);
echo "<br> uppercase: " . strtoupper($sentence);
echo "<br> lowercase: " . strtolower($sentence);

?>

<link rel="stylesheet" type="text/css" href="style.css">