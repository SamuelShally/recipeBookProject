<?php
    // open the recipe database and send back in string form
    $filename = "recipeDatabase.json";
    $data = file_get_contents($filename);

    print($data);
    exit(); 
?>