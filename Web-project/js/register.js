document.addEventListener("DOMContentLoaded", (event) =>{
    "use strict";

    const regExpEmail = /[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}/igm;
    const regExpPassword = /^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$/;

    
    const form = document.querySelector("form");

    const Inputs = form.querySelectorAll('input')

    function validateElem(elem){
        if(elem.name == 'email'){
            if(!regExpEmail.test(elem.value) && elem.value != ''){
                createError(elem, 'email GG')
            }
            else removeError(elem)
        }
        if(elem.name == 'psw'){
            if(!regExpPassword.test(elem.value) && elem.value != ''){
                createError(elem, 'Password GG')
            }
            else removeError(elem)
        }
    }

    for (let input of Inputs) {
        input.addEventListener("blur", () => {
            validateElem(input);
        });
    }

    function removeError(input){
        const parent = input.parentNode;
        
        if(parent.classList.contains('error')){
            parent.querySelector('.error-label').remove()
            parent.classList.remove('error')
        }
    }
    
    function createError(input, text){
        const parent = input.parentNode;
        const errorLabel = document.createElement('label')

        errorLabel.classList.add('error-label')
        errorLabel.textContent = text

        parent.classList.add('error')

        parent.append(errorLabel)
    }

    form.addEventListener("submit", (even)=>{
        even.preventDefault();


        const allInputs = form.querySelectorAll('input')

        if(psw.value != psw_repeat.value){
            removeError(psw_repeat)
            createError(psw_repeat, "пароли не совпадают")
        }
        
        for (let input of allInputs) {
            input.addEventListener("blur", () => {
                validateElem(input);
            });
        }
    });
});