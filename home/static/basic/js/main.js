
// function copyText() {
//     var copyText = document.getElementById("copyText");
//     copyText.select();
//     copyText.setSelectionRange(0, 99999)
//     alert("Copied : " + copyText.value);
// }




jQuery(function ($) {
    'use strict';

    // Sticky Nav1
    $(document).on("scroll", function () {
        if ($(document).scrollTop() > 150) {
            $(".main-nav").addClass("is-sticky ");
        } else {
            $(".main-nav").removeClass("is-sticky ");
        }
    });

    // Sticky Nav2
    $(document).on("scroll", function () {
        if ($(document).scrollTop() > 0) {
            $(".mobile-nav").addClass("is-sticky ");
        } else {
            $(".mobile-nav").removeClass("is-sticky ");
        }
    });

    // Mean Menu
    jQuery('.mean-menu').meanmenu({
        meanScreenWidth: "991"
    });

    // Disable Button
    $(document).ready(function () {
        $('#privacyCheck').click(function () {
            $('#submit').prop("disabled", !$("#privacyCheck").prop("checked"));
        })
    });

    // Preloader
    jQuery(window).on('load', function () {
        jQuery(".loader-content").fadeOut(500);
    });


}(jQuery));
