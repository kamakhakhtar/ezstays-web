window.onload=function(){setTimeout(function(){var s=$(".listing-slider-one");$.ajax({url:"/ajax/get-hostels/",method:"GET",dataType:"json",success:function(e){var a="";e.hostels.forEach(function(s){a+=`
                        <div class="item">
                            <div class="listing-card-one style-three border-30 mb-50">
                                <div class="img-gallery p-15">
                                    <div class="position-relative border-20 overflow-hidden">
                                        <div class="tag text-dark fw-500 border-20 ${s.hostelType.toLowerCase()}">FOR ${s.hostelType}</div>
                                        ${s.image_url?`<img src="${s.image_url}" alt="${s.name}">`:""}
                                        <a href="#" data-bs-toggle="modal" data-bs-target="#callback" class="btn-four inverse rounded-circle position-absolute"><i class="bi bi-telephone-inbound-fill"></i></a>
                                    </div>
                                </div>
                                <div class="property-info pe-4 ps-4">
                                    <a href="/house/${s.slug}/" class="title tran3s">${s.name}</a>
                                    <div class="address">${s.address}</div>
                                    <div class="pl-footer top-border d-flex align-items-center justify-content-between">
                                        
                                    <a href="#" class="btn-ten rounded-0 btn-ten-black" data-bs-toggle="modal" data-bs-target="#schedule"><span>Schedule a visit</span></a>
                                    </div>
                                </div>
                            </div>
                        </div>`}),s.html(a),s.hasClass("slick-initialized")&&s.slick("unslick"),s.slick({dots:!1,arrows:!0,prevArrow:$(".prev_b"),nextArrow:$(".next_b"),lazyLoad:"ondemand",centerPadding:"0px",slidesToShow:4,slidesToScroll:1,autoplay:!0,autoplaySpeed:1e3,responsive:[{breakpoint:1400,settings:{slidesToShow:3}},{breakpoint:992,settings:{slidesToShow:2}},{breakpoint:768,settings:{slidesToShow:1}}]})},error:function(s){console.log("Error fetching and parsing data",s)}});var e=$(".feedback-slider-two");$.ajax({url:"/ajax/get-testimonials/",method:"GET",dataType:"json",success:function(s){var a="";s.testimonials.forEach(function(s){a+=`
                        <div class="item">
                            <div class="feedback-block-four">
                                <div class="d-flex align-items-center">
                                    <img src="${s.image_url}" alt="${s.student_name}" class="rounded-circle avatar">
                                    <div class="ps-3">
                                        <h6 class="fs-20 m0">${s.student_name}</h6>
                                        <span class="fs-16">${s.student_addr}</span>
                                    </div>
                                </div>
                                <blockquote>"${s.review}"</blockquote>
                                <!-- Remaining structure -->
                            </div>
                        </div>`}),e.html(a),e.hasClass("slick-initialized")&&e.slick("unslick"),e.slick({dots:!1,arrows:!0,prevArrow:$(".prev_c"),nextArrow:$(".next_c"),lazyLoad:"ondemand",centerPadding:"0px",slidesToShow:3,slidesToScroll:1,centerMode:!0,autoplay:!0,autoplaySpeed:3e3,responsive:[{breakpoint:1200,settings:{slidesToShow:2}},{breakpoint:768,settings:{slidesToShow:1}}]}),$("img.lazy-load").each(function(){$(this).attr("src",$(this).data("src"))})},error:function(s){console.log("Error fetching and parsing testimonials",s)}})},100)};