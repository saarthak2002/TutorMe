 if (document.readyState !== 'loading') {
    handleButtonPress();
    handleCardButtonPress();
} else {
    document.addEventListener('DOMContentLoaded', function () {
        handleButtonPress();
        handleCardButtonPress();
    });
}

function handleButtonPress() {
    const buttons = document.querySelectorAll('.request-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            const data = this.getAttribute('request-data');
            const url = new URL(window.location.href);
            url.searchParams.set('data', encodeURIComponent(data));
            console.log(data);
            console.log(url.toString());
            const xhr = new XMLHttpRequest();
            xhr.open('GET', url.toString());
            xhr.onload = function() {
                const response = xhr.responseText;
                window.location.href = url.toString();
            };
            xhr.send();
            
        });
    });
}

function handleCardButtonPress() {
    const buttons = document.querySelectorAll('.tutor-card-request-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            var csrftoken = Cookies.get('csrftoken');
            console.log(csrftoken);
            const from = this.getAttribute('from_user');
            const to = this.getAttribute('to_tutor');
            const course = this.getAttribute('course');
            const url = new URL(window.location.href);

            // '/my-view/?data=' + encodeURIComponent(data))
            url.searchParams.set('from', encodeURIComponent(from));
            this.disabled = true;
            this.innerHTML = "Request Sent";

            console.log(url.toString());
            console.log(from);
            console.log(to);
            console.log(course);

            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            const formData = new FormData();
            // xhr.onload = function() {
            //     const response = xhr.responseText;
            //     window.location.href = url.toString();
            // };
            formData.append('from', from);
            formData.append('to', to);
            formData.append('course', course);
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);

        });
    });
}