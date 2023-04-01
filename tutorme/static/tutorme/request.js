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

// Student View - "Search" tab
// "Request" button in student search table
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

// Student View - "Search" tab
// "Request Help" button in tutor cards from search results
function handleCardButtonPress() {
    const buttons = document.querySelectorAll('.tutor-card-request-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            
            var csrftoken = Cookies.get('csrftoken');
            const from = this.getAttribute('from_user');
            const to = this.getAttribute('to_tutor');
            const course = this.getAttribute('course');
            const url = new URL(window.location.href);

            //get position of button to know where to place popup
            const buttonRect = button.getBoundingClientRect();
            const buttonTop = buttonRect.top;
            const buttonLeft = buttonRect.left;

            //Show popup to ask the student what time they want to request
            const popup = document.createElement('div')
            popup.classList.add('time-request-popup')
            popup.innerHTML=`
                <h2>Request Help</h2>
                <label for="date">Date:</label>
                <input type="date" id="date" name="date" required>
                <br>
                <label for="start-time">Start Time:</label>
                <input type="time" id="start-time" name="start-time" required>
                <br>
                <label for="end-time">End Time:</label>
                <input type="time" id="end-time" name="end-time" required>
                <br>
                <button id="submit">Submit</button>
            `;
            //position the pop up correctly
            popup.style.position = 'absolute';
            popup.style.top = buttonTop + button.offsetHeight + 'px';
            popup.style.left = buttonLeft + 'px';
            
            document.body.appendChild(popup)
            const submitButton = popup.querySelector('#submit');
            submitButton.addEventListener('click', function() {
                const date = popup.querySelector('#date').value;
                const startTime = popup.querySelector('#start-time').value;
                const endTime = popup.querySelector('#end-time').value;
                
                // Create the form data object with the necessary data
                const formData = new FormData();
                formData.append('from', from);
                formData.append('to', to);
                formData.append('course', course);
                formData.append('date', date);
                formData.append('start', startTime);
                formData.append('end', endTime);
                formData.append('csrfmiddlewaretoken', csrftoken);
                
                // Send the POST request to the server
                const xhr = new XMLHttpRequest();
                xhr.open('POST', url.toString());
                xhr.send(formData);
                
                // Update the button to indicate that the request has been sent
                this.disabled = true;
                this.innerHTML = 'Request Sent';
                
                // Hide the popup form
                popup.remove();
            });
            // const xhr = new XMLHttpRequest();
            // xhr.open('POST', url.toString());
            // const formData = new FormData();
            // formData.append('from', from);
            // formData.append('to', to);
            // formData.append('course', course);
            // formData.append('csrfmiddlewaretoken', csrftoken);
            // xhr.send(formData);

        });
    });
}


// Student View - "My Requests" tab
// "Remove" button in student request cards, removes a particular Request a student has made from the database
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

// Tutor View - "My Requests" tab
// "Accept" button in cards in My Requests page in the Tutor View, changes the status of a particular request to "Accepted"
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

// Tutor View - "My Requests" tab
// "Reject" button in cards in My Requests page in the Tutor View, changes the status of a particular request to "Declined"
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

// Tutor View - "Add Classes" tab
// "Add" button in table in Add Classes page in the Tutor View, adds a particular course to the Tutor model- After Search
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

// Tutor View - "My Classes" tab
// "Remove" button in cards in My Classes page in the Tutor View, removes a particular course from the Tutor model
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
