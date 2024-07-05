$(window).on('load', function() {
    // Function to handle form validation and submission
    function handleFormSubmit(formClass, successMessage) {
        $(formClass).on('submit', function(e) {
            e.preventDefault();

            let isValid = true;
            const nameInput = this.querySelector('input[name="name"]');
            const phoneInput = this.querySelector('input[name="phone"]');

            // Validate name
            if (nameInput.value.trim() === '') {
                nameInput.classList.add('invalid');
                isValid = false;
            } else {
                nameInput.value = nameInput.value.replace(/^(.)|\s+(.)/g, c => c.toUpperCase());
                nameInput.classList.remove('invalid');
            }

            // Validate phone
            if (phoneInput.value.trim() === '' || phoneInput.value.length != 10) {
                phoneInput.classList.add('invalid');
                isValid = false;
            } else {
                phoneInput.classList.remove('invalid');
            }

            if (!isValid) return;

            var $btn = $(this);
            $btn.prop('disabled', true).html('<div class="progress-bar"></div>');
            $('.progress-bar').css('animation', 'loading 2s linear forwards');

            var formattedMessage = `${formClass === '.call-back-form' ? 'Call Back' : 'Schedule a Visit'}\nName: ${nameInput.value}\nPhone: ${phoneInput.value}`;
            var encodedMessage = encodeURIComponent(formattedMessage);
            var url = `/send-email/${encodedMessage}`;

            // AJAX request
            setTimeout(function() {
                $.ajax({
                    url: url,
                    type: 'GET',
                    success: function() {
                        $('.modal').modal('hide');
                        $btn.html(formClass === '.call-back-form' ? 'Request a callback' : 'Schedule a visit').prop('disabled', false);
                        $('#thankyou .thankyou-title').text(successMessage);
                        $('#thankyou').modal('show');
                    },
                    error: function(xhr, status, error) {
                        $btn.html('Failed - Try Again').prop('disabled', false);
                        alert(`Error: ${error}`);
                    }
                });
            }, 500); // Reduced simulated network delay
        });
    }

    // Handle callback and schedule form submissions
    handleFormSubmit('.call-back-form', 'Callback request sent successfully!');
    handleFormSubmit('.schedule-form', 'Visit Scheduled Successfully!');

    // Lazy loading images with fade-in effect
    $('img.lazy-load').each(function() {
        var img = $(this);
        img.hide().attr('src', img.attr('data-src')).removeAttr('data-src').on('load', function() {
            img.fadeIn();
        });
    });

    // Function to load SEO footer URLs
    function loadSEOFooter() {
        $.ajax({
            url: '/ajax/seofooter-urls/',
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                var seoFooter = $('#seo-footer').empty();
                data.footer_urls.forEach(function(urlData) {
                    seoFooter.append(`<a href="/${urlData.slug}">${urlData.title}<span> | </span></a>`);
                });
            },
            error: function() {
                console.log('Error loading SEO footer URLs');
            }
        });
    }

    // Function to load cities data
    // function loadCities() {
    //     $.ajax({
    //         url: '/ajax/get-cities/',
    //         type: 'GET',
    //         dataType: 'json',
    //         success: function(data) {
    //             var select = $('.nice-select.location').empty();
    //             data.cities.forEach(function(city) {
    //                 select.append(new Option(city.city, city.pk));
    //             });
    //             select.niceSelect('update');
    //         },
    //         error: function() {
    //             console.error('Failed to load cities');
    //         }
    //     });
    // }

    // Load SEO footer URLs and cities data
    loadSEOFooter();
    loadCities();
});
