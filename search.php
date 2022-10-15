<?php
    // open the recipe database and send back in string form
    $find = $_POST['find'];
    exec("python3 recipeBookProject.py $find", $output, $status);

    print($output[0]);
?>
