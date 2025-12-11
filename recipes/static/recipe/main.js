function searchRecipes(){
    let q=document.getElementById("search").value

    fetch("/search/?q=" +q)
        .then(r=>r.json())
        .then(data=>{
            let box=document.getElementById("result")
            box.innerHTML="";

        if(!data.meals){
            box.innerHTML="no result";
            return
        }
        data.meals.forEach(meal => {
            box.innerHTML +=`
            <div>
                <a href="/recipe/${meal.idMeal}/">${meal.strMeal}</a>
            </div>
              `;       
        });
        });
}