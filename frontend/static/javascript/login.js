
document.addEventListener("DOMContentLoaded",function(){
    //adding theme
    var HTMLComponent=document.documentElement
    var theme=window.localStorage.getItem("theme")
    HTMLComponent.setAttribute("data-theme",theme)
})


document.getElementById("loginbtn").addEventListener('click',function(){
    var loginID=document.getElementById("Login-ID").value
    var emaiID=document.getElementById("Password").value
    console.log(loginID,emaiID)
    var valid=email_validation(emaiID)
    if (valid){
        axios
    }
})

function email_validation(email_value){
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    if (email_value.match(validRegex)){
        return true
    }
    else{
        error_message("Please enter a Valid Email")
        return false

    }
}

function error_message(message){
    //getting div
    var eventhandle=document.getElementById("error-handle")
    //creating main div
    var errordiv= document.createElement("div")
    errordiv.classList.add("alert")
    errordiv.classList.add("alert-error")
    //create message
    var errormessage=document.createElement("span")
    errormessage.innerHTML=message
    //adding error message inside div
    errordiv.appendChild(errormessage)
    //adding div to error handler
    eventhandle.appendChild(errordiv)
    //animation functions
    setTimeout(function() {
        // Element fade animation
        var op = 1;
        var intervalId = setInterval(function() {
            if (op <= 0.1) {
                clearInterval(intervalId);
                errordiv.style.opacity = 0;
                errordiv.style.filter = 'alpha(opacity=0)';
                // Element delete
                errordiv.remove();
            } else {
                errordiv.style.opacity = op;
                errordiv.style.filter = 'alpha(opacity=' + op * 100 + ")";
                op -= 0.04;
            }
        }, 50);
    }, 3000);
    
}