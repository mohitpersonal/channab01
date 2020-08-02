$(document).on('click', '#pills-home-tab', function(){
    var set_value = sessionStorage.setItem('milk_tab', "Daily");
    console.log("sessionStorage is ---------->", set_value)

})
//
$(document).on('click', '#pills-profile-tab', function(){
    var set_value = sessionStorage.setItem('milk_tab', "Weekly");

})
//


$(document).on('click', '#pills-miking-tab', function(){
    var set_value = sessionStorage.setItem('milk_tab', "Monthly");
})

//
$(document).on('click', '#pills-gallery-tab', function(){
    var set_value = sessionStorage.setItem('milk_tab', "Yearly");

})
//


//

$(document).ready(function () {
    var lastTab = sessionStorage.getItem('milk_tab');
    console.log(lastTab)
    if (lastTab == 'Daily') {
        $('#pills-home-tab').addClass("active");
        $('#pills-gallery-tab').removeClass("active");
        $('#pills-miking-tab').removeClass("active");
        $('#pills-profile-tab').removeClass("active");

        $('#Health').addClass("show active");
        $('#Weekly').removeClass("show active");
        $('#Monthly').removeClass("show active");
        $('#Yearly').removeClass("show active");
        sessionStorage.clear();
        
    }
   if (lastTab == 'Weekly') {
        $('#pills-home-tab').removeClass("active");
        $('#pills-gallery-tab').removeClass("active");
        $('#pills-miking-tab').removeClass("active");
        $('#pills-profile-tab').addClass("active");


        $('#Health').removeClass("show active");
        $('#Weekly').addClass("show active");
        $('#Monthly').removeClass("show active");
        $('#Yearly').removeClass("show active");
        sessionStorage.clear();
        
    }
    if (lastTab == 'Monthly') {
        $('#pills-home-tab').removeClass("active");
        $('#pills-gallery-tab').removeClass("active");
        $('#pills-miking-tab').addClass("active");
        $('#pills-profile-tab').removeClass("active");

        $('#Health').removeClass("show active");
        $('#Weekly').removeClass("show active");
        $('#Monthly').addClass("show active");
        $('#Yearly').removeClass("show active");
        sessionStorage.clear();
    }
    if (lastTab == 'Yearly') {
        $('#pills-home-tab').removeClass("active");
        $('#pills-gallery-tab').addClass("active");
        $('#pills-miking-tab').removeClass("active");
        $('#pills-profile-tab').removeClass("active");

        $('#Health').removeClass("show active");
        $('#Weekly').removeClass("show active");
        $('#Monthly').removeClass("show active");
        $('#Yearly').addClass("show active");
        sessionStorage.clear();
 
    }
 
})


