jQuery(function ($) {
    'use strict';

    // Sticky Nav1
    $(document).on("scroll", function () {
        if ($(document).scrollTop() > 40) {
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

    // Read More

    $(document).ready(function () {
        var maxLength = 220;
        $(".show-read-more").each(function () {
            var myStr = $(this).text();
            if ($.trim(myStr).length > maxLength) {
                var newStr = myStr.substring(0, maxLength);
                var removedStr = myStr.substring(maxLength, $.trim(myStr).length);
                $(this).empty().html(newStr);
                $(this).append(' <a href="javascript:void(0);" class="read-more">..See more</a>');
                $(this).append('<span class="more-text">' + removedStr + '</span>');
            }
        });
        $(".read-more").click(function () {
            $(this).siblings(".more-text").contents().unwrap();
            $(this).remove();
        });
    });




}(jQuery));
