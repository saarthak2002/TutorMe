 if (document.readyState !== 'loading') {
    handleButtonPress();
    handleCardButtonPress();
    handleCardRemovePress();
    handleRequestAccept();
    handleRequestReject();
    handleTutorAddPress();
    handleTutorRemovePress();
} else {
    document.addEventListener('DOMContentLoaded', function () {
        handleButtonPress();
        handleCardButtonPress();
        handleCardRemovePress();
        handleRequestAccept();
        handleRequestReject();
        handleTutorAddPress();
        handleTutorRemovePress();
    });
}

function handleButtonPress() {
    const buttons = document.querySelectorAll('.request-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            const data = this.getAttribute('request-data');
            const url = new URL(window.location.href);
            url.searchParams.set('data', encodeURIComponent(data));
            
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
            const from = this.getAttribute('from_user');
            const to = this.getAttribute('to_tutor');
            const course = this.getAttribute('course');
            const url = new URL(window.location.href);


            url.searchParams.set('from', encodeURIComponent(from));
            this.disabled = true;
            this.innerHTML = "Request Sent";

            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            const formData = new FormData();
            formData.append('from', from);
            formData.append('to', to);
            formData.append('course', course);
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);

        });
    });
}

function handleCardRemovePress() {
    const buttons = document.querySelectorAll('.request-card-remove-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            
            var csrftoken = Cookies.get('csrftoken');
            const from = this.getAttribute('from_user');
            const to = this.getAttribute('to_tutor');
            const course = this.getAttribute('course');
            const url = new URL(window.location.href);


            url.searchParams.set('from', encodeURIComponent(from));
            this.disabled = true;
            this.innerHTML = "Removed";

            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            const formData = new FormData();
            formData.append('from', from);
            formData.append('to', to);
            formData.append('course', course);
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);

        });
    });
}

function handleRequestAccept() {
    const buttons = document.querySelectorAll('.request-card-accept-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            
            var csrftoken = Cookies.get('csrftoken');
            const from = this.getAttribute('student');
            const to = this.getAttribute('tutor');
            const course = this.getAttribute('course');
            const type = this.getAttribute('request_type');
            const url = new URL(window.location.href);

            url.searchParams.set('from', encodeURIComponent(from));
            this.disabled = true;
            this.innerHTML = "Accepted";
            
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            const formData = new FormData();
            formData.append('from', from);
            formData.append('to', to);
            formData.append('course', course);
            formData.append('request_type', type)
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);

        });
    });
}

function handleRequestReject() {
    const buttons = document.querySelectorAll('.request-card-reject-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            
            var csrftoken = Cookies.get('csrftoken');
            const from = this.getAttribute('student');
            const to = this.getAttribute('tutor');
            const course = this.getAttribute('course');
            const type = this.getAttribute('request_type');
            const url = new URL(window.location.href);

            url.searchParams.set('from', encodeURIComponent(from));
            this.disabled = true;
            this.innerHTML = "Rejected";
            
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            const formData = new FormData();
            formData.append('from', from);
            formData.append('to', to);
            formData.append('course', course);
            formData.append('request_type', type)
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);

        });
    });
}

function handleTutorAddPress() {
    const buttons = document.querySelectorAll('.tutor-add-class-request-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            console.log("add button pressed");
            var csrftoken = Cookies.get('csrftoken');
            const course = this.getAttribute('course');
            const url = new URL(window.location.href);

            this.disabled = true;
            this.innerHTML = "Added";

            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());

            const formData = new FormData();
            formData.append('course', course);
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);

        });
    });
}

function handleTutorRemovePress() {
    const buttons = document.querySelectorAll('.tutor-class-card-remove-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            
            var csrftoken = Cookies.get('csrftoken');
            const course = this.getAttribute('course');
            const url = new URL(window.location.href);

            this.disabled = true;
            this.innerHTML = "Removed";

            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            
            const formData = new FormData();
            formData.append('course', course);
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);

        });
    });
}
