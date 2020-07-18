function Password_Register(){
    var password= $("#registerPassword").val();
    if(password.length == '' || password.length == null) {
        $("#registerPassword").addClass("has-error");
        $("#password_label").show();

        $("#password_label").text("This Field is required");
        return false;
    }
    else{
        if(password.length < 6){
            $("#registerPassword").addClass("has-error");
            $("#password_label").show();

            $("#password_label").text("It must contains minmum 6 characters");
            return false;
        }
        else{
        
        $("#registerPassword").removeClass("has-success");
        $("#password_label").hide();
        $("#password_label").text("");
        return true;
        }
        }
    }
$("#registerPassword").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


////////////////


function PasswordConfirmCheck() {
    var password = $("#registerPassword").val()
    var confirm_pas = $("#confirmpasswordReg").val()
    if (confirm_pas.length == null || confirm_pas.length == "") {
        $("#confirm_password_label").show();

        $("#confirmpasswordReg").addClass("has-error");
        $("#confirm_password_label").text("This Field is required");
        return false;
    } 
    else {
        if(confirm_pas != password) {
            $("#confirmpasswordReg").addClass("has-error");
            $("#confirm_password_label").show();

            $("#confirm_password_label").text("Password is not match");
            return false;
        } 
        else {
            $("#confirmpasswordReg").removeClass("has-error");
            $("#confirm_password_label").hide();
            $("#confirm_password_label").text("");
            return true;
            }
        }

}

$("#confirmpasswordReg").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})







///////////////
function MobileNumberCheckRegister(){
    var legal =$("#mobile_number").val();
    var letterNumber = /^[+0-9 ]*$/;
    if(legal.length == '' || legal.length == null) {
        $("#mobile_number").removeClass("has-success");
        $("#mobile_number").addClass("has-error");
        $("#mobile_reg_label").show();
        $("#mobile_reg_label").text("This Field is required");
        return false;
    }
    else{
        if (legal.match(letterNumber)) {
            if (legal.length > 15 || legal.length < 10) {
                $("#mobile_number").removeClass("has-success");
                $("#mobile_number").addClass("has-error");
                $("#mobile_reg_label").show();
                $("#mobile_reg_label").text("It must contains only 10 to 15 numbers");
                return false;
            }
            else{
                $("#mobile_number").removeClass("has-error");

                $("#mobile_reg_label").hide();
                $("#mobile_reg_label").text("");
                return true;
            }
        }else{
            $("#mobile_number").removeClass("has-success");
            $("#mobile_reg_label").show();
            $("#mobile_number").addClass("has-error");
            $("#mobile_reg_label").text("It must contains only numbers");
            return false;
        }
    }
}

$("#mobile_number").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})







////////////

function Email_valid_check(){
    var letternumber = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var email=$("#email_reg").val();
    if(email.match(letternumber)){
        $("#email_check_label").hide();
        $("#email_reg").removeClass("has-error");
        $("#email_check_label").text("");
        return true;
    }
    else{
        $("#email_check_label").show();
        
        $("#email_reg").addClass("has-error");
        $("#email_check_label").text("please enter a valid email address");
        return false;
    }
}

$("#email_reg").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})



/////////////

var message_ele = document.getElementById("msg_Sucess");

setTimeout(function () {
    $(message_ele).css("display", "none");
}, 7000);

var msg_sign_errer = document.getElementById("msg_sign_err");

setTimeout(function () {
    $(msg_sign_errer).css("display", "none");
}, 2500);








///////////

$(document).on('submit', '#registerViewIdForm', function(){
    if (Email_valid_check()  &&
        MobileNumberCheckRegister() && Password_Register() && PasswordConfirmCheck() == true) {
        return true;
    } else {
        Email_valid_check();
        MobileNumberCheckRegister();
        Password_Register();
        PasswordConfirmCheck();

        return false;
    }

}) 

//////////


