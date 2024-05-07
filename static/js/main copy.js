$(document).ready(function() {
    // Handle the submission of the callback form
    $('.call-back-form').on('submit', function(e) {
        
        let isValid = true;
        const nameInput = this.querySelector('input[name="name"]');
        const phoneInput = this.querySelector('input[name="phone"]');

        // Validate name to ensure it's not empty and capitalizes the first letter
        if (nameInput.value.trim() === '') {
            nameInput.classList.add('invalid');
            isValid = false;
        } else {
            nameInput.value = nameInput.value.replace(/^(.)|\s+(.)/g, c => c.toUpperCase());
            nameInput.classList.remove('invalid');
        }

        // Validate phone to ensure it's 10 digits long
        if (phoneInput.value.trim() === '' || phoneInput.value.length != 10) {
            phoneInput.classList.add('invalid');
            isValid = false;
        } else {
            phoneInput.classList.remove('invalid');
        }

        if (!isValid) {
            e.preventDefault(); // Prevent form submission if validation fails
        }
        
        e.preventDefault();  // Prevent the default form submission

        var $btn = $(this);
        // Disable the button to prevent multiple clicks
        $btn.prop('disabled', true);

        // Add a progress bar element to the button
        $btn.html('<div class="progress-bar"></div>');
        $('.progress-bar').css('animation', 'loading 2s linear forwards');


        var name = $(this).find('input[name="name"]').val();  // Get the name from the input
        var phone = $(this).find('input[name="phone"]').val();  // Get the phone number

        // Construct the message in a simple table format
        var formattedMessage = `Call Back \nName: ${nameInput.value}\nPhone: ${phoneInput.value}`;

        // Encode the message for URL
        var encodedMessage = encodeURIComponent(formattedMessage);

        // Construct the URL to send the data to
        var url = `/send-email/${encodedMessage}`;

        // Make the AJAX request
        setTimeout(function() {
        $.ajax({
            url: url,
            type: 'GET',
            success: function(response) {
                 // Close all Bootstrap modals
                 $('.modal').modal('hide');

                   // On success, reset the button
                $btn.html('Request a callback');
                $btn.prop('disabled', false);

                // Change the title and text of the thank you modal
                $('#thankyou .thankyou-title').text('Callback request sent successfully!');

                // Open the thank you modal
                $('#thankyou').modal('show');
                // Optionally clear the form or handle other success actions
            },
            error: function(xhr, status, error) {
                $btn.html('Failed - Try Again');
                $btn.prop('disabled', false);
                // Handle any errors here
                alert('Error requesting callback: ' + error);
            }
        });
    }, 3500); // simulate network delay
    });

    // Handle the submission of the schedule form
    $('.schedule-form').on('submit', function(e) {
        let isValid = true;
        const nameInput = this.querySelector('input[name="name"]');
        const phoneInput = this.querySelector('input[name="phone"]');

        // Validate name to ensure it's not empty and capitalizes the first letter
        if (nameInput.value.trim() === '') {
            nameInput.classList.add('invalid');
            isValid = false;
        } else {
            nameInput.value = nameInput.value.replace(/^(.)|\s+(.)/g, c => c.toUpperCase());
            nameInput.classList.remove('invalid');
        }

        // Validate phone to ensure it's 10 digits long
        if (phoneInput.value.trim() === '' || phoneInput.value.length != 10) {
            phoneInput.classList.add('invalid');
            isValid = false;
        } else {
            phoneInput.classList.remove('invalid');
        }

        if (!isValid) {
            e.preventDefault(); // Prevent form submission if validation fails
        }
        
        e.preventDefault();  // Prevent the default form submission
        var $btn = $(this);
        // Disable the button to prevent multiple clicks
        $btn.prop('disabled', true);

        // Add a progress bar element to the button
        $btn.html('<div class="progress-bar"></div>');
        $('.progress-bar').css('animation', 'loading 2s linear forwards');

        var name =  $('#sc-name').val();  // Get the name from the input
        var phone =  $('#sc-phone').val();  // Get the phone number
        
    
        // Construct the URL to send the data to
        // Construct the message in a simple table format
        var formattedMessage = `Schedule a Visit \nName: ${nameInput.value}\nPhone: ${phoneInput.value}`;

        // Encode the message for URL
        var encodedMessage = encodeURIComponent(formattedMessage);
        
        // Construct the URL to send the data to
        var url = `/send-email/${encodedMessage}`;
        // Make the AJAX request
        setTimeout(function() {
        $.ajax({
            url: url,
            type: 'GET',
            success: function(response) {
                 // Close all Bootstrap modals
                 $('.modal').modal('hide');

                  // On success, reset the button
                $btn.html('Schedule a visit');
                $btn.prop('disabled', false);

                // Change the title and text of the thank you modal
                $('#thankyou .thankyou-title').text('Visit Scheduled Successfully!');

                // Open the thank you modal
                $('#thankyou').modal('show');
                // Optionally clear the form or handle other success actions
            },
            error: function(xhr, status, error) {
                // Handle error
                $btn.html('Failed - Try Again');
                $btn.prop('disabled', false);
                // Handle any errors here
                alert('Error scheduling visit: ' + error);
            }
        });
    }, 3500); // simulate network delay
    });
});

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        // Lazy loading images with fade-in effect
        $('img.lazy-load').each(function() {
            var img = $(this); // Reference to the current image
            img.hide(); // Initially hide the image
            img.attr('src', img.attr('data-src')).removeAttr('data-src'); // Set src from data-src
            img.on('load', function() {
                img.fadeIn(); // Fade in the image once it's loaded
            });
        });

        // AJAX call to load footer URLs
        $.ajax({
            url: '/ajax/footer-urls/', // Ensure this URL matches your Django URL configuration
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                $('#footer-url-container').html(data.html); // Assuming an element with this ID exists
            },
            error: function() {
                console.log('Error loading footer URLs');
            }
        });

        // AJAX call to fetch city data and populate select element
        $.ajax({
            url: '/ajax/get-cities/', // URL configured in urls.py
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                var select = $('.nice-select.location');
                select.empty(); // Clear any existing options
                data.cities.forEach(function(city) {
                    select.append(new Option(city.city, city.pk)); // Append new options
                });
                select.niceSelect('update'); // Update niceSelect plugin display
            },
            error: function() {
                console.error('Failed to load cities');
            }
        });

    }, 100); // Execute all the above after a 1000ms delay post-DOMContentLoaded
});
