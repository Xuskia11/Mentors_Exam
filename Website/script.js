const form = document.getElementById("form")
const passowrd = document.getElementById("password")
const reapetedPassword = document.getElementById("reapetedpass")

const table1 = document.getElementById("table1")
const roled = document.getElementById("roles")

const main = document.getElementById("main1")

const table2 = document.getElementById("table2");

const parent = document.getElementById("parent");

table.style.display = "none";

const array = []

form.addEventListener("submit", function(e){
    e.preventDefault()

    const passowrdValue = form.elements.password.value;
    const reapetedPassValue = form.elements.reapetedpass.value;

    array.push(passowrdValue);
    array.push(reapetedPassValue);
    

    if(array[0] !== array[1]){
        p = document.createElement("p");
        content = document.createTextNode("Passwords don't match!!!");
        p.appendChild(content);
        parent.appendChild(p)
    } else {
        table.style.display = "block";
        main.style.display = "none";
    }
    
    
    
    
    const viewrValue = form.elements.role.value
    console.log(viewrValue)

    if(viewrValue === "moderator"){
        table2.style.display = "none";
    } else {
        table1.style.display = "none";
    }
    
})

