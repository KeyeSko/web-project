document.addEventListener("DOMContentLoaded", (event) =>{
    "use strict";
    
    const form = document.querySelector("form");
    
    form.addEventListener("submit", (even)=>{
        even.preventDefault();
        
        for (let elem of form.elements) {
            console.log(elem);
            if (elem.value == ""){elem.nextElementSibling.textContent = "Данное поле не заполнено! ";}
        }
    });
});