document.addEventListener("DOMContentLoaded", (event) =>{
    "use strict";

    const regExpEmail = /[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}/igm;
    const regExpPassword = /^((?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z])).{8}$/;

    
    const form = document.querySelector("form");

    const Inputs = form.querySelectorAll('input')

    const psw = form.querySelector('.psw')
    const psw_repeat = form.querySelector('.psw_repeat')

    let flag = "0";

    console.log(psw)
    console.log(psw_repeat)


    function validateElem(elem){
        if(elem.name == 'email'){
            if(!regExpEmail.test(elem.value) && elem.value != ''){
                removeError(elem)
                createError(elem, 'email GG')
                flag = "1";
            }
            else removeError(elem)
        }
        if(elem.name == 'psw'){
            if(!regExpPassword.test(elem.value) && elem.value != ''){
                removeError(elem)
                createError(elem, 'Password GG')
                flag = "1";
            }
            else removeError(elem)
            if(psw.value != psw_repeat.value && psw_repeat != ''){
                removeError(psw_repeat)
                createError(psw_repeat, "Пароли не совпадают")
                flag = "1";
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
        flag = "0";

        
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
        flag = '1'
    }

    form.addEventListener("submit", (even)=>{
        even.preventDefault();


        const allInputs = form.querySelectorAll('input')

        if(psw.value != psw_repeat.value){
            removeError(psw_repeat)
            createError(psw_repeat, "пароли не совпадают")
            flag = "1";
        }
        
        for (let input of allInputs) {
            input.addEventListener("blur", () => {
                validateElem(input);
            });
        }
    });

    document.getElementById("regbtn").onclick = function(){
        if (flag=="0")
        {
            alert("Вы успешно зарегистрированны")
            let tg = {
                token: "5696896333:AAHmgirmrAwUA0NvyeZiJKOOrnSHqpqHXFM", // Your bot's token that got from @BotFather
                chat_id: "1015603317" // The user's(that you want to send a message) telegram chat id
            }
            
            /**
             * By calling this function you can send message to a specific user()
             * @param {String} the text to send
             *
            */
            function sendMessage(text)
            {
                const url = `https://api.telegram.org/bot${tg.token}/sendMessage?chat_id=${tg.chat_id}&text=${text}`; // The url to request
                const xht = new XMLHttpRequest();
                xht.open("GET", url);
                xht.send();
            }
            
            // Now you can send any text(even a form data) by calling sendMessage function.
            // For example if you want to send the 'hello', you can call that function like this:
            
            sendMessage("hello");
        }
      }    
});