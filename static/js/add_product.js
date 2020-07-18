function NameAnimal(){
    var letternumber = /^[a-zA-Z]+$/;
    console.log("hhh")
    var first_name=$("#name_animal").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#name_animal").removeClass("has-success");
        $("#name_animal").addClass("has-error");
        $("#name_animal_label").show();
        $("#name_animal_label").text("This Field is required");
        
        return false;
    }
    else{
        if (first_name.length >15 || first_name.length <3){
            $("#name_animal").removeClass("has-success");
            $("#name_animal").addClass("has-error");
            $("#name_animal_label").text("It only contains 3 to 15 characters");
            $("#name_animal_label").show();
            return false;
        }
        else{
            $("#name_animal").addClass("has-success");
            $("#name_animal_label").text("");
            
            $("#name_animal_label").hide();
            return true;
           
        }
    }
}
$("#name_animal").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


////

function PriceCheck(){
    var letternumber = /^[a-zA-Z]+$/;
    console.log("hhh")
    var first_name=$("#price_text").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#price_text").removeClass("has-success");
        $("#price_text").addClass("has-error");
        $("#price_check_label").show();
        $("#price_check_label").text("This Field is required");
        
        return false;
    }
    else{
        $("#price_text").addClass("has-success");
        $("#price_check_label").text("");
        $("#price_check_label").hide();
        return true;
    }

}
$("#price_text").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})
///
function PhoneCheck(){
    var letternumber = /^[a-zA-Z]+$/;
    console.log("hhh")
    var first_name=$("#mobilenumber").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#mobilenumber").removeClass("has-success");
        $("#mobilenumber").addClass("has-error");
        $("#mobile_label").show();
        $("#mobile_label").text("This Field is required");
        
        return false;
    }
    else{
        $("#mobilenumber").addClass("has-success");
        $("#mobile_label").text("");
        $("#mobile_label").hide();
        return true;
    }

}
$("#mobilenumber").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})

//


/////////

function checkforblank() {
    var check_type = $("#countary_check_text_found").val();
    if (check_type == 'Select') {
        document.getElementById("countary_check_text_found").classList.remove("has-success");
        document.getElementById("countary_check_text_found").classList.add("has-error");
        document.getElementById('label_your_account').style.display = 'block';
        return false;
    } else {
        document.getElementById("countary_check_text_found").classList.add("has-success");
        document.getElementById('label_your_account').style.display = 'none';
        return true;
    }
}

$("#countary_check_text_found").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})
////

function checkImage(){
    var image_val = $("#getFile1_found").val();
    if (image_val == '' || image_val == null){
        $("#images_sec_check_label_found").show();
        $("#images_sec_check_label_found").text("required");
        return false;
    }
    else{
        $("#images_sec_check_label_found").hide();

        $("#images_sec_check_label_found").text("")
        return true;
    }
}
////////
$("#add_animal_js").on('submit', function(){
    if (NameAnimal() && PhoneCheck() && PriceCheck() && checkImage() && checkforblank() == true){
        return true;
    }
    else{
        NameAnimal();
        PhoneCheck();
        PriceCheck();
        checkImage();
        checkforblank();
        return false;
    }
})



///
$("#countary_check_text_found").on('change', function(){

    var check_type = $("#countary_check_text_found").val();
    if (check_type == 'Select') {
        document.getElementById("countary_check_text_found").classList.remove("has-success");
        document.getElementById("countary_check_text_found").classList.add("has-error");
        document.getElementById('label_your_account').style.display = 'block';
        return false;
    } else {
        document.getElementById("countary_check_text_found").classList.add("has-success");
        document.getElementById('label_your_account').style.display = 'none';
        return true;
    }
})
    

/////////////

var msg_succ = document.getElementById("msg_Sucess_log");

setTimeout(function () {
    msg_succ.style.display = "none";
}, 4000);


var msg_err = document.getElementById("msg_err_log");

setTimeout(function () {
    msg_err.style.display = "none";
}, 2500);



/////

function readURLMySecond_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      $("#display_none_found").hide();
      reader.onload = function(e) {
         $("#blah2_found").show();
         $('#blah2_found').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}












/////////////



function readURLMySecond1_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      $("#display_none_found").hide();
      reader.onload = function(e) {
         $("#blah3_found").show();
         $('#blah3_found').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}


///////////




function readURLMySecond4_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#blah4_found").show();
         $('#blah4_found').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}


//////////






function MyreadURLSecond4_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#blah5_found").show();
         $('#blah5_found').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}











///////////
function MyfourthImage(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#fourth_image_show").show();
         $('#fourth_image_show').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}





//////////


function MyfourthImage(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#fourth_image_show").show();
         $('#fourth_image_show').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}








////////






function fifth_imageCheck(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#fifth_show").show();
         $('#fifth_show').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}