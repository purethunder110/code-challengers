
document.addEventListener("DOMContentLoaded",function(){
    //adding theme
    var HTMLComponent=document.documentElement
    var theme=window.localStorage.getItem("theme")
    HTMLComponent.setAttribute("data-theme",theme)
})


document.getElementById("Signupbtn").addEventListener('click',function(){
    var emailID=document.getElementById("Email-ID").value
    var valid=email_validation(emailID)

    if (valid){
        var EPassword=document.getElementById("E-Password").value
        var CPassword=document.getElementById("C-Password").value
        var Username=document.getElementById("Username-ID").value
        //error checks
        if (CPassword==null || CPassword=="" || EPassword==null || EPassword==""){
            error_message("Please Enter a Password")
            return;
        }
        if (EPassword != CPassword){
            error_message("Password are Not Equal")
            CPassword==""
            return;
        }
        if (CPassword.length<10){
            error_message("Please Enter A Password with more than 10 Characters")
            return;
        }

        if (Username==null || Username==""){
            error_message("Enter A Username")
            return;
        }

        if (Username.length<9){
            error_message("Please Enter a Username with more than 9 characters")
            return;
        }

        var message={
            "Username":Username,
            "EmailID":emailID,
            "Password":CPassword
        }
        axios.post("/auth/create/",message)
        .then(response=>console.log(response))
        .catch(error=>{
            var status=error.response.status
            if (status==='422'){
                error_message("Error Occured. Please reload and try again")
            }
        })
    }
})

function email_validation(email_value){
    var validRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
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

