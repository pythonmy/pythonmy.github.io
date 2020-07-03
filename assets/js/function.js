 $(document).on('ready', function() {
           $('.regular').slick({
           dots: false,
           arrows: true,
           infinite: false,
           speed: 300,
           slidesToShow: 3,
           slidesToScroll: 2,
           responsive: [
         	{
         	  breakpoint: 1024,
         	  settings: {
         		slidesToShow: 3,
         		slidesToScroll: 3,
         		infinite: true,
         		dots: false
         	  }
         	},
         	{
         	  breakpoint: 600,
         	  settings: {
         		slidesToShow: 2,
         		slidesToScroll: 2
         	  }
         	},
         	{
         	  breakpoint: 480,
         	  settings: {
         		slidesToShow: 1,
         		slidesToScroll: 1
         	  }
         	}
           ]
         });
         $('.banner-slider').slick({
         	 dots:true,
         	 arrows: false,
         	 infinite: true,
         	 speed: 2500,
                 autoplay: false,
         	 autoplaySpeed: 2500,
         	 fade:true,
         	 pauseOnHover: false
         });
         });	
         
         
         (function ($) {
         'use strict';
         // Preloader
         $(window).on('load', function () {
           $('#preloader')
             .delay(2000)
             .fadeOut('slow', function () {
               $(this).remove();
             });
         });
         })(window.jQuery);
         
         $(document).ready(function(){
         $('.left-menu-lis li a[href^="#"]').on('click',function (e) {
            e.preventDefault();
            var target = this.hash;
            var $target = $(target);
            $('html, body').stop().animate({
                'scrollTop': $target.offset().top
            }, 900, 'swing', function () {
                // window.location.hash = target;
            });
         });
         });
         
         $(window).scroll(function() {
           if ($(this).scrollTop() > 100) {
             $('.back-to-top').fadeIn('slow');
           } else {
             $('.back-to-top').fadeOut('slow');
           }
         });
         
         $('.back-to-top').click(function() {
           $('html, body').animate({
             scrollTop: 0
           }, 1500, 'easeInOutExpo');
           return false;
         });
