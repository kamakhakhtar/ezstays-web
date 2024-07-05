// js Document

// Created on   : 01/01/2024.
// Theme Name   : Homy-Real Estate HTML5 Template & Dashboard
// Version      : 1.0.
// Developed by : (me@heloshape.com) / (www.me.heloshape.com)


(function($) {
    "use strict";

      //-------------- Click event to scroll to top
      $(window).on('scroll', function (){
        if ($(this).scrollTop() > 200) {
          $('.scroll-top').fadeIn();
        } else {
          $('.scroll-top').fadeOut();
        }
      });
      $('.scroll-top').on('click', function() {
        $('html, body').animate({scrollTop : 0});
        return false;
      });

      // --------------------- Add .active class to current navigation based on URL
      var pgurl = window.location.href.substr(window.location.href.lastIndexOf("/")+1);
      $(".navbar-nav > li  a").each(function(){
      if($(this).attr("href") == pgurl || $(this).attr("href") == '' )
      $(this).addClass("active");
      // $(this).parent("li").addClass("active");
      })

    
     


      

        // ------------------------ Navigation Scroll
        $(window).on('scroll', function (){   
          var sticky = $('.sticky-menu'),
          scroll = $(window).scrollTop();
          if (scroll >= 180) sticky.addClass('fixed');
          else sticky.removeClass('fixed');

        });


     



        // ------------------------ Hero Slider One
        if($(".hero-slider-one").length) {
          $('.hero-slider-one').slick({
              dots: false,
              arrows: false,
              lazyLoad: 'ondemand',
              centerPadding: '0px',
              slidesToShow: 1,
              slidesToScroll: 1,
              autoplay: true,
              fade: true,
              autoplaySpeed: 7000,
            });
        }



        // ------------------------ Feedback Slider One
        if($(".feedback-slider-one").length) {
          $('.feedback-slider-one').slick({
              dots: true,
              arrows: false,
              lazyLoad: 'ondemand',
              centerPadding: '0px',
              slidesToShow: 1,
              slidesToScroll: 1,
              fade: true,
              autoplay: true,
              autoplaySpeed: 300000
            });
        }

        // ------------------------ Feedback Slider Two
        if($(".feedback-slider-two").length) {
          $('.feedback-slider-two').slick({
              dots: false,
              arrows: true,
              prevArrow: $('.prev_c'),
              nextArrow: $('.next_c'),
              lazyLoad: 'ondemand',
              centerPadding: '0px',
              slidesToShow: 3,
              slidesToScroll: 1,
              centerMode: true,
              autoplay: true,
              autoplaySpeed: 3000,
              responsive: [
                {
                  breakpoint: 1200,
                  settings: {
                    slidesToShow: 2
                  }
                },
                {
                  breakpoint: 768,
                  settings: {
                    slidesToShow: 1
                  }
                }
              ]
            });
        }



        // ------------------------ Listing Slider
        if ($(".listing-slider-one").length) {
          $('.listing-slider-one').slick({
              dots: false,
              arrows: true,
              prevArrow: $('.prev_b'),
              nextArrow: $('.next_b'),
              lazyLoad: 'ondemand',
              centerPadding: '0px',
              slidesToShow: 4,
              slidesToScroll: 1,  // Changed this from 4 to 1
              autoplay: true,
              autoplaySpeed: 1000,
              responsive: [
                  {
                      breakpoint: 1400,
                      settings: {
                          slidesToShow: 3
                      }
                  },
                  {
                      breakpoint: 992,
                      settings: {
                          slidesToShow: 2
                      }
                  },
                  {
                      breakpoint: 768,
                      settings: {
                          slidesToShow: 1
                      }
                  }
              ]
          });
  
          // Button click events for individual sliding
          $('.prev_b').on('click', function() {
              $('.listing-slider-one').slick('slickPrev');
          });
  
          $('.next_b').on('click', function() {
              $('.listing-slider-one').slick('slickNext');
          });
      }

       

    
$(window).on ('load', function (){ // makes sure the whole site is loaded

// -------------------- Site Preloader
        $('#ctn-preloader').fadeOut(); // will first fade out the loading animation
        $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
        $('body').delay(350).css({'overflow':'visible'});



// ------------------------------------- Chart
      var chartP = $ ("#property-chart");
      
      $('img.lazy-load').each(function() {
        var img = $(this); // Reference to the current image
        img.hide(); // Initially hide the image
        img.attr('src', img.attr('data-src')).removeAttr('data-src'); // Set src from data-src
        img.on('load', function() {
            img.fadeIn(); // Fade in the image once it's loaded
        });
    });


    });  //End On Load Function



})(jQuery);