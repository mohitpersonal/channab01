function TagAnimalLive(){
    var letternumber = /^[a-zA-Z]+$/;
    console.log("hhh")
    var first_name=$("#tag_name_live").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#tag_name_live").removeClass("has-success");
        $("#tag_name_live").addClass("has-error");
        $("#tag_animal_live_label").show();
        $("#tag_animal_live_label").text("This Field is required");
        
        return false;
    }
    else{
        if (first_name.length >50 || first_name.length <3){
            $("#tag_name_live").removeClass("has-success");
            $("#tag_name_live").addClass("has-error");
            $("#tag_animal_live_label").text("It only contains 3 to 50 characters");
            $("#tag_animal_live_label").show();
            return false;
        }
        else{
            $("#tag_name_live").addClass("has-success");
            $("#tag_animal_live_label").text("");
            
            $("#tag_animal_live_label").hide();
            return true;
           
        }
    }
}
$("#tag_name_live").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


////






$("#animal_bread_live").on('change', function(){

    var check_type = $("#animal_bread_live").val();
    if (check_type == 'Select') {
        document.getElementById("animal_bread_live").classList.remove("has-success");
        document.getElementById("animal_bread_live").classList.add("has-error");
        document.getElementById('animal_bread_label_text').style.display = 'block';
        return false;
    } else {
        document.getElementById("animal_bread_live").classList.add("has-success");
        document.getElementById('animal_bread_label_text').style.display = 'none';
        return true;
    }
})







///////


function CheckLabelAnimalBreed(){

    var check_type = $("#animal_bread_live").val();
    if (check_type == 'Select') {
        document.getElementById("animal_bread_live").classList.remove("has-success");
        document.getElementById("animal_bread_live").classList.add("has-error");
        document.getElementById('animal_bread_label_text').style.display = 'block';
        return false;
    } else {
        document.getElementById("animal_bread_live").classList.add("has-success");
        document.getElementById('animal_bread_label_text').style.display = 'none';
        return true;
    }
}
//////
$("#category_live_Animal").on('change', function(){

    var check_type = $("#category_live_Animal").val();
    if (check_type == 'Select') {
        document.getElementById("category_live_Animal").classList.remove("has-success");
        document.getElementById("category_live_Animal").classList.add("has-error");
        document.getElementById('Category_live_Animal_label').style.display = 'block';
        return false;
    } else {
        document.getElementById("category_live_Animal").classList.add("has-success");
        document.getElementById('Category_live_Animal_label').style.display = 'none';
        return true;
    }
})







///////

function MaleAnimalCheckLiveStock(){

    var check_type = $("#mail_gendercheck_live").val();
    if (check_type == 'Select') {
        document.getElementById("mail_gendercheck_live").classList.remove("has-success");
        document.getElementById("mail_gendercheck_live").classList.add("has-error");
        document.getElementById('gender_live_label').style.display = 'block';
        return false;
    } else {
        document.getElementById("mail_gendercheck_live").classList.add("has-success");
        document.getElementById('gender_live_label').style.display = 'none';
        return true;
    }
}
//////
$("#mail_gendercheck_live").on('change', function(){

    var check_type = $("#mail_gendercheck_live").val();
    if (check_type == 'Select') {
        document.getElementById("mail_gendercheck_live").classList.remove("has-success");
        document.getElementById("mail_gendercheck_live").classList.add("has-error");
        document.getElementById('gender_live_label').style.display = 'block';
        return false;
    } else {
        document.getElementById("mail_gendercheck_live").classList.add("has-success");
        document.getElementById('gender_live_label').style.display = 'none';
        return true;
    }
})


/////////////
function CheckCategoryLiveAnimal(){

    var new_check = $("#category_live_Animal").val();
    if (new_check == 'Select') {
        document.getElementById("category_live_Animal").classList.remove("has-success");
        document.getElementById("category_live_Animal").classList.add("has-error");
        document.getElementById('Category_live_Animal_label').style.display = 'block';
        return false;
    } else {
        document.getElementById("category_live_Animal").classList.add("has-success");
        document.getElementById('Category_live_Animal_label').style.display = 'none';
        return true;
    }
}

//


/////////


$("#animal_type_live_stock").on('change', function(){

    var check_type = $("#animal_type_live_stock").val();
    if (check_type == 'Select') {
        document.getElementById("animal_type_live_stock").classList.remove("has-success");
        document.getElementById("animal_type_live_stock").classList.add("has-error");
        document.getElementById('animal_type_label').style.display = 'block';
        return false;
    } else {
        document.getElementById("animal_type_live_stock").classList.add("has-success");
        document.getElementById('animal_type_label').style.display = 'none';
        return true;
    }
})


//////
function AnimalTableLiveType() {
    var check_type = $("#animal_type_live_stock").val();
    if (check_type == 'Select') {
        document.getElementById("animal_type_live_stock").classList.remove("has-success");
        document.getElementById("animal_type_live_stock").classList.add("has-error");
        document.getElementById('animal_type_label').style.display = 'block';
        return false;
    } else {
        document.getElementById("animal_type_live_stock").classList.add("has-success");
        document.getElementById('animal_type_label').style.display = 'none';
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

function checkImageLivestock(){
    var image_val = $("#Livestock_getFile1_found").val();
    if (image_val == '' || image_val == null){
        $("#Livestock_images_sec_check_label_found").show();
        $("#Livestock_images_sec_check_label_found").text("required");
        return false;
    }
    else{
        $("#Livestock_images_sec_check_label_found").hide();

        $("#Livestock_images_sec_check_label_found").text("")
        return true;
    }
}
////////
$("#live_Stock_add_animal_js").on('submit', function(){
    if (TagAnimalLive() && checkImageLivestock() && CheckLabelAnimalBreed() && CheckCategoryLiveAnimal() && MaleAnimalCheckLiveStock() && AnimalTableLiveType() == true){
        return true;
    }
    else{
        TagAnimalLive();
        checkImageLivestock();
        CheckLabelAnimalBreed();
        CheckCategoryLiveAnimal();
        MaleAnimalCheckLiveStock();
        AnimalTableLiveType();
        return false;
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

function Livestock_readURLMySecond_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      $("#Livestock_display_none_found").hide();
      reader.onload = function(e) {
         $("#Livestock_blah2_found").show();
         $('#Livestock_blah2_found').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}












/////////////



function Livestock_readURLMySecond1_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      $("#Livestock_display_none_found").hide();
      reader.onload = function(e) {
         $("#Livestock_blah3_found").show();
         $('#Livestock_blah3_found').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}


///////////




function Livestock_readURLMySecond4_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#Livestock_blah4_found").show();
         $('#Livestock_blah4_found').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}


//////////






function Livestock_MyreadURLSecond4_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#Livestock_blah5_found").show();
         $('#Livestock_blah5_found').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}











///////////
function Livestock_MyfourthImage(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#Livestock_fourth_image_show").show();
         $('#Livestock_fourth_image_show').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}





//////////


function Livestock_MyfourthImage(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#Livestock_fourth_image_show").show();
         $('#Livestock_fourth_image_show').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}








////////






function Livestock_fifth_imageCheck(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#Livestock_fifth_show").show();
         $('#Livestock_fifth_show').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}