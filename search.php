<?php
    // open the recipe database and send back in string form
    $find = $_POST['find'];
    exec("python3 app.py $find", $output, $status);

    print($output[0]);
?>
