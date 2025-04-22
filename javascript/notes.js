let images = ["https://t4.ftcdn.net/jpg/11/55/89/89/360_F_1155898967_OroAp8ja1bGnN5PqE1usF6oIKfWWDRcS.jpg", "https://t4.ftcdn.net/jpg/11/55/89/89/360_F_1155898967_OroAp8ja1bGnN5PqE1usF6oIKfWWDRcS.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/1200px-Cat_November_2010-1a.jpg"]
let counter = 0

function change(){
    if (counter < images.length){
        document.getElementById("img").
        src = images[counter] 
        counter += 1
    }else{
        counter = 0
        document.getElementById("img").src = images[counter]
    }
}

function hello(){
    document.getElementById("title").innerHTML = "Hello World!"
}
function hover(){
    document.getElementById
    ("img").src = "https://t4.ftcdn.net/jpg/11/55/89/89/360_F_1155898967_OroAp8ja1bGnN5PqE1usF6oIKfWWDRcS.jpg"
}
function leave(){
    document.getElementById
    ("img").src = "https://t4.ftcdn.net/jpg/11/55/89/89/360_F_1155898967_OroAp8ja1bGnN5PqE1usF6oIKfWWDRcS.jpg"
}