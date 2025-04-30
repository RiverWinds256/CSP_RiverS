
function point(image){

    image.src="https://www.nps.gov/cany/planyourvisit/images/RhodesSmartt1_1.jpg?maxwidth=1300&autorotate=false&quality=78&format=webp"

}

function leave(image){

    image.src="https://www.nps.gov/cany/planyourvisit/images/RhodesSmartt1_1.jpg?maxwidth=1300&autorotate=false&quality=78&format=webp"
}



function toggle(){ 

    const thing=document.getElementById("hidden")
    if(thing.style.display=="none"){
        thing.style.display=""

    }else{
        thing.style.display="none"
    }




}