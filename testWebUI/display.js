
function pullAllRecipes(){
    //Open JSON database 
    let file = "recipeDatabase.json";



    
    //Insert json objects into parent element recipeBox
    let recipeBox = document.getElementById("recipes");



        let newBox = document.createElement('div');
        newBox.innerHTML = "Testing the system";
        recipeBox.appendChild(newBox);
}


// for (let x = 0; x< actualData.length ; x++)
// {
// let newBox = document.createElement('div');
// newBox.classList.add('box');
// newBox.classList.add(actualData[x].color);
// boxes.appendChild(newBox);
// } 




