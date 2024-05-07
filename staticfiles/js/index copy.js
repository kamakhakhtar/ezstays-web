window.onload = function() {
    // Timeout to delay execution for 1 second after full page load
    setTimeout(function() {
        var $slider = $(".listing-slider-one");
        
        $.ajax({
            url: '/ajax/get-hostels/',
            method: "GET",
            dataType: "json",
            success: function(response) {
                var items = "";
                response.hostels.forEach(function(hostel) {
                    items += `
                        <div class="item">
                            <div class="listing-card-one style-three border-30 mb-50">
                                <div class="img-gallery p-15">
                                    <div class="position-relative border-20 overflow-hidden">
                                        <div class="tag text-dark fw-500 border-20 ${hostel.hostelType.toLowerCase()}">FOR ${hostel.hostelType}</div>
                                        ${hostel.image_url ? `<img src="${hostel.image_url}" alt="${hostel.name}">` : ""}
                                        <a href="#" data-bs-toggle="modal" data-bs-target="#callback" class="btn-four inverse rounded-circle position-absolute"><i class="bi bi-telephone-inbound-fill"></i></a>
                                    </div>
                                </div>
                                <div class="property-info pe-4 ps-4">
                                    <a href="/house/${hostel.slug}/" class="title tran3s">${hostel.name}</a>
                                    <div class="address">${hostel.address}</div>
                                    <div class="pl-footer top-border d-flex align-items-center justify-content-between">
                                        <strong class="price fw-500 color-dark">&#8377;${hostel.price}/mo*</strong>
                                        <a href="#" data-bs-toggle="modal" data-bs-target="#schedule" class="btn-four rounded-circle"><i class="bi bi-calendar-plus"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>`;
                });
                $slider.html(items);
                if ($slider.hasClass("slick-initialized")) {
                    $slider.slick('unslick');
                }
                $slider.slick({
                    dots: false,
                    arrows: true,
                    prevArrow: $(".prev_b"),
                    nextArrow: $(".next_b"),
                    lazyLoad: "ondemand",
                    centerPadding: "0px",
                    slidesToShow: 4,
                    slidesToScroll: 1,
                    autoplay: true,
                    autoplaySpeed: 1000,
                    responsive: [
                        { breakpoint: 1400, settings: { slidesToShow: 3 }},
                        { breakpoint: 992, settings: { slidesToShow: 2 }},
                        { breakpoint: 768, settings: { slidesToShow: 1 }}
                    ]
                });
            },
            error: function(error) {
                console.log("Error fetching and parsing data", error);
            }
        });

        // Similarly, load the testimonials
        var $testimonialSlider = $(".feedback-slider-two");
        $.ajax({
            url: '/ajax/get-testimonials/',
            method: "GET",
            dataType: "json",
            success: function(response) {
                var items = "";
                response.testimonials.forEach(function(testimonial) {
                    items += `
                        <div class="item">
                            <div class="feedback-block-four">
                                <div class="d-flex align-items-center">
                                    <img src="${testimonial.image_url}" alt="${testimonial.student_name}" class="rounded-circle avatar">
                                    <div class="ps-3">
                                        <h6 class="fs-20 m0">${testimonial.student_name}</h6>
                                        <span class="fs-16">${testimonial.student_addr}</span>
                                    </div>
                                </div>
                                <blockquote>"${testimonial.review}"</blockquote>
                                <!-- Remaining structure -->
                            </div>
                        </div>`;
                });
                $testimonialSlider.html(items);
                if ($testimonialSlider.hasClass("slick-initialized")) {
                    $testimonialSlider.slick('unslick');
                }
                $testimonialSlider.slick({
                    dots: false,
                    arrows: true,
                    prevArrow: $(".prev_c"),
                    nextArrow: $(".next_c"),
                    lazyLoad: "ondemand",
                    centerPadding: "0px",
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    centerMode: true,
                    autoplay: true,
                    autoplaySpeed: 3000,
                    responsive: [
                        { breakpoint: 1200, settings: { slidesToShow: 2 }},
                        { breakpoint: 768, settings: { slidesToShow: 1 }}
                    ]
                });
                $("img.lazy-load").each(function() {
                    $(this).attr('src', $(this).data('src'));
                });
            },
            error: function(error) {
                console.log("Error fetching and parsing testimonials", error);
            }
        });
    }, 100); // Delay execution by 1 second after full page load
};
