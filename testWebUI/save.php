<?php
//Get elements via post
  $name = $_POST['name'];
  $description = $_POST['description'];
  $ingredients = $_POST['ingredients'];
  $instructions = $_POST['instructions'];

  //create new JSON obj
  $obj->Name = $name;
  $obj->Description = $description;
  $obj->Ingredients = explode(",",$ingredients);
  $obj->Instructions = explode(",",$instructions);

  $nested->$name = $obj;
  
  //Get JSON file and add the new obj above
  $filename = "recipeDatabase.json";
  $data = json_decode(file_get_contents($filename), true);
  array_push($data, $nested);

  //re code the json file and write it 
  $encoded = json_encode($data);
  file_put_contents($filename, $encoded);

  //quit
  print "success";
 ?>