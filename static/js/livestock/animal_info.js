/// session storage

$(document).on('click', '#pills-home-tab', function(){
    var set_value = sessionStorage.setItem('value', "Health");
    $("#check_family_tab").hide();
    $("#check_health_tab").show()
    $("#check_milking_atb").hide();
    $("#check_gallery_tab").hide();
    $("#check_description_tab").hide();

})
//
$(document).on('click', '#pills-profile-tab', function(){
    var set_value = sessionStorage.setItem('value', "Family");
    $("#check_family_tab").show();
    $("#check_health_tab").hide()
    $("#check_milking_atb").hide();
    $("#check_gallery_tab").hide();
    $("#check_description_tab").hide();


})
//


$(document).on('click', '#pills-miking-tab', function(){
    var set_value = sessionStorage.setItem('value', "Milking");
    $("#check_family_tab").hide();
    $("#check_health_tab").hide()
    $("#check_milking_atb").show();
    $("#check_gallery_tab").hide();
    $("#check_description_tab").hide();


})

//
$(document).on('click', '#pills-gallery-tab', function(){
    var set_value = sessionStorage.setItem('value', "Gallery");
    $("#check_family_tab").hide();
    $("#check_health_tab").hide()
    $("#check_milking_atb").hide();
    $("#check_gallery_tab").show();
    $("#check_description_tab").hide();


})
//

$(document).on('click', '#pills-description-tab', function(){
    var set_value = sessionStorage.setItem('value', "Description");
    $("#check_family_tab").hide();
    $("#check_health_tab").hide()
    $("#check_milking_atb").hide();
    $("#check_gallery_tab").hide();
    $("#check_description_tab").show();


})

//

$(document).ready(function () {
    var lastTab = sessionStorage.getItem('value');
    if (lastTab == 'Description') {
        $('#pills-description-tab').addClass("active");
        $('#pills-gallery-tab').removeClass("active");
        $('#pills-miking-tab').removeClass("active");
        $('#pills-profile-tab').removeClass("active");
        $('#pills-home-tab').removeClass("active");

        $('#Description').addClass("show active");

        $('#Family').removeClass("show active");
        $('#Milking').removeClass("show active");
    
        $('#Gallery').removeClass("show active");
        $('#Health').removeClass("show active");


        $("#check_family_tab").hide();
        $("#check_health_tab").hide()
        $("#check_milking_atb").hide();
        $("#check_gallery_tab").hide();
        $("#check_description_tab").show();


        
    }
   if (lastTab == 'Gallery') {
        $('#pills-description-tab').removeClass("active");
        $('#pills-gallery-tab').addClass("active");
        $('#pills-miking-tab').removeClass("active");
        $('#pills-profile-tab').removeClass("active");
        $('#pills-home-tab').removeClass("active");

        $('#Description').removeClass("show active");
        $('#Family').removeClass("show active");
        $('#Milking').removeClass("show active");
        $('#Gallery').addClass("show active");
        $('#Health').removeClass("show active");

        $("#check_family_tab").hide();
        $("#check_health_tab").hide()
        $("#check_milking_atb").hide();
        $("#check_gallery_tab").show();
        $("#check_description_tab").hide();


        
    }
    if (lastTab == 'Milking') {
        $('#pills-description-tab').removeClass("active");
        $('#pills-gallery-tab').removeClass("active");
        $('#pills-miking-tab').addClass("active");
        $('#pills-profile-tab').removeClass("active");
        $('#pills-home-tab').removeClass("active");

        $('#Description').removeClass("show active");
        $('#Family').removeClass("show active");
        $('#Milking').addClass("show active");
        $('#Gallery').removeClass("show active");
        $('#Health').removeClass("show active");
        

        $("#check_family_tab").hide();
        $("#check_health_tab").hide()
        $("#check_milking_atb").show();
        $("#check_gallery_tab").hide();
        $("#check_description_tab").hide();




    }
    if (lastTab == 'Family') {
        $('#pills-description-tab').removeClass("active");
        $('#pills-gallery-tab').removeClass("active");
        $('#pills-miking-tab').removeClass("active");
        $('#pills-profile-tab').addClass("active");
        $('#pills-home-tab').removeClass("active");

        $('#Description').removeClass("show active");
        $('#Family').addClass("show active");
        $('#Milking').removeClass("show active");
        $('#Gallery').removeClass("show active");
        $('#Health').removeClass("show active");


        $("#check_family_tab").show();
        $("#check_health_tab").hide()
        $("#check_milking_atb").hide();
        $("#check_gallery_tab").hide();
        $("#check_description_tab").hide();



        
    }
    if (lastTab == 'Health') {
        $('#pills-description-tab').removeClass("active");
        $('#pills-gallery-tab').removeClass("active");
        $('#pills-miking-tab').removeClass("active");
        $('#pills-profile-tab').removeClass("active");
        $('#pills-home-tab').addClass("active");

        $('#Description').removeClass("show active");
        $('#Family').removeClass("show active");
        $('#Milking').removeClass("show active");
        $('#Gallery').removeClass("show active");
        $('#Health').addClass("show active");
        

        $("#check_family_tab").hide();
        $("#check_health_tab").show()
        $("#check_milking_atb").hide();
        $("#check_gallery_tab").hide();
        $("#check_description_tab").hide();

    }

})





/////


     $('.health_delete').click(function(){
       swal({
     
          title : "Confirmation",
          text : "Are you sure you want to Delete ?",
          buttons : {
             cancel : true,
             confirm : "Confirm"
          }
     
     
       }).then(val =>{

        var ids = $(this).attr('data-id');
        if (val){
            var url = '/accounts/title_delete/?title_id='+ids; 
            window.location.href = url

             swal({
                title : "Thanks !",
                text : "You have Sucessfully Logout Your Account",
                icon : "success"
     
             })
          }
       })
     
     })


///// milk deleion

    $('.milk_delete').click(function(){
       swal({
     
          title : "Confirmation",
          text : "Are you sure you want to Delete ?",
          buttons : {
             cancel : true,
             confirm : "Confirm"
          }
     
     
       }).then(val =>{

        var ids = $(this).attr('data-id');
        if (val){
            var url = '/accounts/milk_delete/?milk_id='+ids; 
            window.location.href = url

             swal({
                title : "Thanks !",
                text : "You have Sucessfully Logout Your Account",
                icon : "success"
     
             })
          }
       })
     
     })


///////////////







    $('.delete_Descritpion').click(function(){
       swal({
     
          title : "Confirmation",
          text : "Are you sure you want to Delete ?",
          buttons : {
             cancel : true,
             confirm : "Confirm"
          }
     
     
       }).then(val =>{

        var ids = $(this).attr('data-id');
        if (val){
            var url = '/accounts/delete_description/?delete_desc_id='+ids; 
            window.location.href = url

             swal({
                title : "Thanks !",
                text : "You have Sucessfully Logout Your Account",
                icon : "success"
     
             })
          }
       })
     
     })





//// image tab

    $('.delete_image_faltu').click(function(){
       swal({
     
          title : "Confirmation",
          text : "Are you sure you want to Delete ?",
          buttons : {
             cancel : true,
             confirm : "Confirm"
          }
     
     
       }).then(val =>{

        var image_id_new = $(this).attr('data-id');
        if (val){
            var url = '/accounts/delete_image/?image_id='+image_id_new; 
            window.location.href = url

             swal({
                title : "Thanks !",
                text : "You have Sucessfully Logout Your Account",
                icon : "success"
     
             })
          }
       })
     
     })




///////////////parent

     $('#male_delete_tab_del').click(function(){
       swal({
     
          title : "Confirmation",
          text : "Are you sure you want to Delete ?",
          buttons : {
             cancel : true,
             confirm : "Confirm"
          }
     
     
       }).then(val =>{

        var ids = $(this).attr('data-id');
        if (val){
            var url = '/accounts/delete_male/?delete_male_id='+ids; 
            window.location.href = url

             swal({
                title : "Thanks !",
                text : "You have Sucessfully Logout Your Account",
                icon : "success"
     
             })
          }
       })
     
     })


///////////// child

     $('#female_delete_tab_dl').click(function(){
       swal({
     
          title : "Confirmation",
          text : "Are you sure you want to Delete ?",
          buttons : {
             cancel : true,
             confirm : "Confirm"
          }
     
     
       }).then(val =>{

        var ids = $(this).attr('data-id');
        if (val){
            var url = '/accounts/delete_female/?delete_female_id='+ids; 
            window.location.href = url

             swal({
                title : "Thanks !",
                text : "You have Sucessfully Logout Your Account",
                icon : "success"
     
             })
          }
       })
     
     })


    /////female

         $('.delete_child').click(function(){
       swal({
     
          title : "Confirmation",
          text : "Are you sure you want to Delete ?",
          buttons : {
             cancel : true,
             confirm : "Confirm"
          }
     
     
       }).then(val =>{

        var ids = $(this).attr('data-id');
        if (val){
            var url = '/accounts/delete_child/?delete_child_id='+ids; 
            window.location.href = url

             swal({
                title : "Thanks !",
                text : "You have Sucessfully Logout Your Account",
                icon : "success"
     
             })
          }
       })
     
     })











//////////////
function DetailTagAnimalLive(){
    var letternumber = /^[a-zA-Z]+$/;
    var first_name=$("#tag_Edit_animal").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#tag_Edit_animal").removeClass("has-success");
        $("#tag_Edit_animal").addClass("has-error");
        $("#tag_Edit_animal_label").show();
        $("#tag_Edit_animal_label").text("This Field is required");
        
        return false;
    }
    else{
        if (first_name.length >50 || first_name.length <3){
            $("#tag_Edit_animal").removeClass("has-success");
            $("#tag_Edit_animal").addClass("has-error");
            $("#tag_Edit_animal_label").text("It only contains 3 to 50 characters");
            $("#tag_Edit_animal_label").show();
            return false;
        }
        else{
            $("#tag_Edit_animal").addClass("has-success");
            $("#tag_Edit_animal_label").text("");
            
            $("#tag_Edit_animal_label").hide();
            return true;
           
        }
    }
}
$("#tag_Edit_animal").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


////


////

////////





function HealthTitleAnimal(){
    var letternumber = /^[a-zA-Z]+$/;
    var first_name=$("#health_title_input").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#health_title_input").removeClass("has-success");
        $("#health_title_input").addClass("has-error");
        $("#title_health_label").show();
        $("#title_health_label").text("This Field is required");
        
        return false;
    }
    else{
        if (first_name.length >30 || first_name.length <3){
            $("#health_title_input").removeClass("has-success");
            $("#health_title_input").addClass("has-error");
            $("#title_health_label").text("It only contains 3 to 30 characters");
            $("#title_health_label").show();
            return false;
        }
        else{
            $("#health_title_input").addClass("has-success");
            $("#title_health_label").text("");
            
            $("#title_health_label").hide();
            return true;
           
        }
    }
}
$("#health_title_input").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})



function AddContentAnimal(){
    var letternumber = /^[a-zA-Z]+$/;
    var first_name=$("#edit_editor1_2").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#edit_editor1_2").removeClass("has-success");
        $("#edit_editor1_2").addClass("has-error");
        $("#content_ist_tab_label").show();
        $("#content_ist_tab_label").text("This Field is required");
        
        return false;
    }
    
        else{
            $("#edit_editor1_2").addClass("has-success");
            $("#content_ist_tab_label").text("");
            
            $("#content_ist_tab_label").hide();
            return true;
           
    }
}
$("#edit_editor1_2").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})



function HealthCostAnimal(){
    var letterNumber = /^[+0-9 ]*$/;
    var first_name=$("#cost_of_animal_input").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#cost_of_animal_input").removeClass("has-success");
        $("#cost_of_animal_input").addClass("has-error");
        $("#cost_of_animal_input_label").show();
        $("#cost_of_animal_input_label").text("This Field is required");
        
        return false;
    }
    else{
        if (first_name.match(letterNumber)) {
            $("#cost_of_animal_input").addClass("has-success");
            $("#cost_of_animal_input_label").text("");
            $("#cost_of_animal_input_label").hide();
            return true;

        }
        else{
            $("#cost_of_animal_input").removeClass("has-success");
            $("#cost_of_animal_input").addClass("has-error");
            $("#cost_of_animal_input_label").text("It must contains only Numbers");
            $("#cost_of_animal_input_label").show();
            return false;

           
        }
    }
}
$("#cost_of_animal_input").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})














$("#health_Add_form_popup").on('submit', function(e){
    if (HealthTitleAnimal() && HealthCostAnimal() && AddContentAnimal() == true){


        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        e.preventDefault();

        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success:function(response){
                response_by_api = JSON.parse(response)
                console.log("response_by_api is -------->", response_by_api)
                if (response_by_api['status'] == 200){
                    console.log(response_by_api)
                    $("#health_popup_suceess").text(response_by_api["message"]);
                    $('#health_popup_suceess').css("display", "block");
                    var msg_ajax = document.getElementById("health_popup_suceess");
                    setTimeout(function () {
                        $(msg_ajax).css("display", "none");
                    }, 1500);


                    setTimeout(function(){
                        window.location.reload(1);
                    }, 2000);

                }
                else{

                    $("#health_popup_error").text(response_by_api["error_message"]);
                    $('#health_popup_error').css("display", "block");
                    var msg_ajax = document.getElementById("health_popup_error");
                    setTimeout(function () {
                        $(msg_ajax).css("display", "none");
                    }, 5000);

                }

            },
        })

    }
    else{
        HealthTitleAnimal();
        HealthCostAnimal();
        AddContentAnimal();
        return false;
    }
})

//////////// milking tabs ajax

function MorningMilk(){
    var letterNumber = /^[+0-9 ]*$/;

    var first_name=$("#morning_milk").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#morning_milk").removeClass("has-success");
        $("#morning_milk").addClass("has-error");
        $("#morning_milk_label").show();
        $("#morning_milk_label").text("This Field is required");
        
        return false;
    }
    else{
        if (first_name.match(letterNumber)) {
            $("#morning_milk").addClass("has-success");
            $("#morning_milk_label").text("");
            $("#morning_milk_label").hide();
            return true;

        }
        else{
            $("#morning_milk").removeClass("has-success");
            $("#morning_milk").addClass("has-error");
            $("#morning_milk_label").text("It must contains only Numbers");
            $("#morning_milk_label").show();
            return false;

           
        }
    }
}
$("#morning_milk").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})


function EveningMilk(){
    var letterNumber = /^[+0-9 ]*$/;
    var first_name=$("#evening_milk").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#evening_milk").removeClass("has-success");
        $("#evening_milk").addClass("has-error");
        $("#evening_milk_label").show();
        $("#evening_milk_label").text("This Field is required");
        
        return false;
    }
    else{
        if (first_name.match(letterNumber)) {
            $("#evening_milk").addClass("has-success");
            $("#evening_milk_label").text("");
            $("#evening_milk_label").hide();
            return true;

        }
        else{
            $("#evening_milk").removeClass("has-success");
            $("#evening_milk").addClass("has-error");
            $("#evening_milk_label").text("It must contains only Numbers");
            $("#evening_milk_label").show();
            return false;

           
        }
    }
}
$("#evening_milk").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})









$("#milkig_add_popup_form").on('submit', function(e){
    if (MorningMilk() && EveningMilk() == true){


        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        e.preventDefault();

        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success:function(response){
                response_by_api = JSON.parse(response)
                console.log("response_by_api is -------->", response_by_api)
                if (response_by_api['status'] == 200){
                    console.log(response_by_api)
                    $("#milk_popup_suceess").text(response_by_api["message"]);
                    $('#milk_popup_suceess').css("display", "block");
                    var msg_ajax = document.getElementById("milk_popup_suceess");
                    setTimeout(function () {
                        $(msg_ajax).css("display", "none");
                    }, 1500);


                    setTimeout(function(){
                        window.location.reload(1);
                    }, 2000);

                }
                else{

                    $("#milk_popup_error").text(response_by_api["error_message"]);
                    $('#milk_popup_error').css("display", "block");
                    var msg_ajax = document.getElementById("milk_popup_error");
                    setTimeout(function () {
                        $(msg_ajax).css("display", "none");
                    }, 5000);

                }

            },
        })

    }
    else{
        MorningMilk();
        EveningMilk();
        return false;
    }
})











//////////////////

function AddDescriptionLastAnimal(){
    var letternumber = /^[a-zA-Z]+$/;
    var first_name=$("#description_popup").val();
    if(first_name.length == '' || first_name.length == null) {
        $("#description_popup").removeClass("has-success");
        $("#description_popup").addClass("has-error");
        $("#description_popup_found_label").show();
        $("#description_popup_found_label").text("This Field is required");
        
        return false;
    }
    
        else{
            $("#description_popup").addClass("has-success");
            $("#description_popup_found_label").text("");
            
            $("#description_popup_found_label").hide();
            return true;
           
    }
}
$("#description_popup").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})
//////

$("#description_Add_form").on('submit', function(e){
    if (AddDescriptionLastAnimal() == true){


        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        e.preventDefault();

        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success:function(response){
                response_by_api = JSON.parse(response)
                console.log("response_by_api is -------->", response_by_api)
                if (response_by_api['status'] == 200){
                    console.log(response_by_api)
                    $("#desc_popup_suceess").text(response_by_api["message"]);
                    $('#desc_popup_suceess').css("display", "block");
                    var msg_ajax = document.getElementById("desc_popup_suceess");
                    setTimeout(function () {
                        $(msg_ajax).css("display", "none");
                    }, 1500);


                    setTimeout(function(){
                        window.location.reload(1);
                    }, 2000);

                }
                else{

                    $("#desc_popup_error").text(response_by_api["error_message"]);
                    $('#desc_popup_error').css("display", "block");
                    var msg_ajax = document.getElementById("desc_popup_error");
                    setTimeout(function () {
                        $(msg_ajax).css("display", "none");
                    }, 5000);

                }

            },
        })

    }
    else{
        AddDescriptionLastAnimal();
        return false;
    }
})










//////////////////

function CheckFormGalleryImagetabRead(){
    var image_val = $("#gallery_tab_image").val();
    if (image_val == '' || image_val == null){
        $("#gallery_tab_image_label").show();
        $("#gallery_tab_image_label").text("required");
        return false;
    }
    else{
        $("#gallery_tab_image_label").hide();

        $("#gallery_tab_image_label").text("")
        return true;
    }
}



function GalleryImagetabRead(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {

        $("#gallery_tab_image_label").hide();
        $("#gallery_tab_image_label").text("")
        $("#gallery_tab_image_show").show();
        $('#gallery_tab_image_show').attr('src', e.target.result).width(130).height(100);
      }
      reader.readAsDataURL(input.files[0]);
   }
}










/////

var msg_succ = document.getElementById("msg_Sucess_log");

setTimeout(function () {
    msg_succ.style.display = "none";
}, 4000);


var msg_err = document.getElementById("msg_err_log");

setTimeout(function () {
    msg_err.style.display = "none";
}, 2500);



/////

function EditLivestock_readURLMySecond_Found(input) {
   if (input.files && input.files[0]) {
      var reader = new FileReader();
      var getimgfield = $(input).closest('div').
      next('div').find('img');
      reader.onload = function(e) {
         $("#edit_Livestock_blah4_found").show();
         $('#edit_Livestock_blah4_found').attr('src', e.target.result).width(70).height(50);
      }
      reader.readAsDataURL(input.files[0]);
   }
}










//// deacativate

$(document).on("click", ".root", function(){
    var id = $(this).attr('data-id');
    $.ajax({
        type:'GET',
        url : '/accounts/deactivate_animal/?id=' + id,
        data : '',
        success : function(response){
            console.log(response)
            var json_parse = JSON.parse(response);
            if (json_parse['status'] = 'success'){
                window.location.reload();
            }
            else{
                window.location.reload();
            }

        }
    })


})



























////////////////////////////     parents 


function CheckParentRecord() {
    var check_type = $("#male_parent_check_id").val();
    if (check_type == 'Select') {
        document.getElementById("male_parent_check_id").classList.remove("has-success");
        document.getElementById("male_parent_check_id").classList.add("has-error");
        document.getElementById('male_parent_label_detail_live').style.display = 'block';
        return false;
    } else {
        document.getElementById("male_parent_check_id").classList.add("has-success");
        document.getElementById('male_parent_label_detail_live').style.display = 'none';
        return true;
    }
}

$("#male_parent_check_id").focusout(function () {
    if ($(this).hasClass("has-success")) {
        $(this).removeClass("has-success");
        $(this).removeClass("has-error");
    }
})



$(document).on('change','#male_parent_check_id', function(){
    var check_type = $("#male_parent_check_id").val();
    if (check_type == 'Select') {
        document.getElementById("male_parent_check_id").classList.remove("has-success");
        document.getElementById("male_parent_check_id").classList.add("has-error");
        document.getElementById('male_parent_label_detail_live').style.display = 'block';
        return false;
    } else {
        document.getElementById("male_parent_check_id").classList.add("has-success");
        document.getElementById('male_parent_label_detail_live').style.display = 'none';
        return true;
    }
})


$("#family_add_popup_new_form").on('submit', function(e){
    if (CheckParentRecord() == true){


        var form = $(this);
        data = (form).serialize();
        var Url = form.attr('action');
        e.preventDefault();

        $.ajax({
            type: 'POST',
            data: data,
            url: Url,
            success:function(response){
                response_by_api = JSON.parse(response)
                console.log("response_by_api is -------->", response_by_api)
                if (response_by_api['status'] == 200){
                    console.log(response_by_api)
                    $("#family_popup_suceess").text(response_by_api["message"]);
                    $('#family_popup_suceess').css("display", "block");
                    var msg_ajax = document.getElementById("family_popup_suceess");
                    setTimeout(function () {
                        $(msg_ajax).css("display", "none");
                    }, 1500);


                    setTimeout(function(){
                        window.location.reload(1);
                    }, 2000);

                }
                else{

                    $("#family_popup_error").text(response_by_api["error_message"]);
                    $('#family_popup_error').css("display", "block");
                    var msg_ajax = document.getElementById("family_popup_error");
                    setTimeout(function () {
                        $(msg_ajax).css("display", "none");
                    }, 5000);

                }

            },
        })

    }
    else{
        CheckParentRecord();
        return false;
    }
})

