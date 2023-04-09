 if (document.readyState !== 'loading') {
    handleButtonPress();
    handleCardButtonPress();
    handleCardRemovePress();
    handleRequestAccept();
    handleRequestReject();
    handleTutorAddPress();
    handleTutorRemovePress();
    handleTutorEditProfileButton();
    handleStudentEditProfileButton();
} else {
    document.addEventListener('DOMContentLoaded', function () {
        handleButtonPress();
        handleCardButtonPress();
        handleCardRemovePress();
        handleRequestAccept();
        handleRequestReject();
        handleTutorAddPress();
        handleTutorRemovePress();
        handleTutorEditProfileButton();
        handleStudentEditProfileButton();
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


            const buttonRect = button.getBoundingClientRect();
            const buttonTop = buttonRect.top;
            const buttonLeft = buttonRect.left;

            const popup = document.createElement('div')
            popup.classList.add('time-request-popup', 'p-3', 'bg-white', 'rounded', 'border', 'border-dark')
            popup.innerHTML = `
            <h2 class="mb-4">Select a time</h2>
            <div class="form-group">
                <label for="date">Date:</label>
                <input type="date" id="date" name="date" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="start-time">Start Time:</label>
                <input type="time" id="start-time" name="start-time" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="end-time">End Time:</label>
                <input type="time" id="end-time" name="end-time" class="form-control" required>
            </div>
            <div class = "buttons">
                <button id="submit" class="btn btn-primary">Submit</button>
                <button id="cancel" class="btn btn-danger">Cancel</button>
            </div>
            `;

            const { top, left, height } = button.getBoundingClientRect();
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const popupTop = top + scrollTop + height;
            popup.style.position = 'absolute';
            popup.style.top = popupTop + 'px';
            popup.style.left = left + 'px';
            

            
            document.body.appendChild(popup)
            const submitButton = popup.querySelector('#submit');
            const cancelButton = popup.querySelector('#cancel');
            submitButton.addEventListener('click', function() {
                const date = popup.querySelector('#date').value;
                const startTime = popup.querySelector('#start-time').value;
                const endTime = popup.querySelector('#end-time').value;
                
                const formData = new FormData();
                formData.append('from', from);
                formData.append('to', to);
                formData.append('course', course);
                formData.append('date', date);
                formData.append('start', startTime);
                formData.append('end', endTime);
                formData.append('csrfmiddlewaretoken', csrftoken);
                
                const xhr = new XMLHttpRequest();
                xhr.open('POST', url.toString());
                xhr.send(formData);
                
                this.disabled = true;
                this.innerHTML = 'Request Sent';
                
                popup.remove();
            });
            cancelButton.addEventListener('click', function(){
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
            const end_time_requested = this.getAttribute('end_time')
            const start_time_requested = this.getAttribute('start_time')
            const date_requested = this.getAttribute('date')
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
            formData.append('start_time_requested', start_time_requested)
            formData.append('end_time_requested', end_time_requested)
            formData.append('date_requested', date_requested)
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
            //when add button is pressed open modal to select available times
            const self = this;
            const modal = document.getElementById('availability_modal');
            const modalInstance = M.Modal.init(modal);
            modalInstance.open();

            const closeModalButtonn = modal.querySelector('.modal-close-button');
            closeModalButtonn.addEventListener('click', function() {
                // Close the modal when the close button is pressed
                modalInstance.close();
            });

            const submitButton = modal.querySelector('.modal-submit-button');
            submitButton.addEventListener('click', function(){
                console.log("added ran");
                const daysOfTheWeek = ['monday', 'tuesday', 'wednesday','thursday', 'friday'];
                const timesOfDay = {
                    'morning':'9:00 AM - 12:00 PM', 
                    'afternoon': '12:00 PM - 5:00 PM', 
                    'evening': '5:00 PM - 9:00 PM', 
                    'night' : '9:00 PM - 12:00 AM'
                }
                const mondayCheckedBoxes = [];
                const tuesdayCheckedBoxes = [];
                const wednesdayCheckedBoxes = []
                const thursdayCheckedBoxes = []
                const fridayCheckedBoxes = []
                for(let i = 0; i < daysOfTheWeek.length; i++){
                    const day = daysOfTheWeek[i] + '-available-times';
                    const arrayToAdd = daysOfTheWeek[i]+'CheckedBoxes';
                    const dayFormGroup = document.querySelector('.'+day);
                    const checkboxes = dayFormGroup.querySelectorAll('input[type="checkbox"]');
                    checkboxes.forEach(function(checkbox) {
                        if (checkbox.checked) {
                            if(daysOfTheWeek[i] == 'monday'){
                                mondayCheckedBoxes.push(timesOfDay[checkbox.value]); 
                            }
                            if(daysOfTheWeek[i] == 'tuesday'){
                                tuesdayCheckedBoxes.push(timesOfDay[checkbox.value]); 
                            }
                            if(daysOfTheWeek[i] == 'wednesday'){
                                wednesdayCheckedBoxes.push(timesOfDay[checkbox.value]); 
                            }
                            if(daysOfTheWeek[i] == 'thursday'){
                                thursdayCheckedBoxes.push(timesOfDay[checkbox.value]); 
                            }
                            if(daysOfTheWeek[i] == 'friday'){
                                fridayCheckedBoxes.push(timesOfDay[checkbox.value]); 
                            }
                        }
                    });
                }
                
                // tutor.available_times = {
                //     'Monday': [
                //         {'start_time': '9:00 AM', 'end_time': '10:00 AM'},
                //         {'start_time': '10:00 AM', 'end_time': '11:00 AM'},
                //     ],
                //     'Tuesday': [
                //         {'start_time': '1:00 PM', 'end_time': '2:00 PM'},
                //     ],
                // }

                var csrftoken = Cookies.get('csrftoken');
                const course = self.getAttribute('course');
                const url = new URL(window.location.href);

                self.disabled = true;
                self.innerHTML = "Added";

                const xhr = new XMLHttpRequest();
                xhr.open('POST', url.toString());

                const formData = new FormData();
                formData.append('course', course);
                formData.append('csrfmiddlewaretoken', csrftoken);
                formData.append('mondayTimes', mondayCheckedBoxes)
                formData.append('tuesdayTimes', tuesdayCheckedBoxes)
                formData.append('wednesdayTimes', wednesdayCheckedBoxes)
                formData.append('thursdayTimes', thursdayCheckedBoxes)
                formData.append('fridayTimes', fridayCheckedBoxes)

                xhr.send(formData);
                modalInstance.close();
            });   

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

function handleTutorEditProfileButton(){
    const buttons = document.querySelectorAll('.tutor-edit-bio-button')
    buttons.forEach(function(button){
        button.addEventListener('click', function(){
            let csrftoken = Cookies.get('csrftoken');
            const bioText = document.getElementById("edit-tutor-bio-textbox").value;
            const xhr = new XMLHttpRequest();
            const url = new URL(window.location.href);

            xhr.open('POST', url.toString());
            
            const formData = new FormData();
            formData.append('bio', bio);
            formData.append('csrfmiddlewaretoken', csrftoken);

            xhr.send(formData);
            
        });
    });

}

function handleStudentEditProfileButton(){
    const buttons = document.querySelectorAll('.student-profile-edit-button')
    buttons.forEach(function(button){
        button.addEventListener('click', function(){
            let csrftoken = Cookies.get('csrftoken');
            const bioText = document.getElementById("edit-student-bio-textbox").value;
            const helpText = document.getElementById("edit-student-help-description-textbox").value;
            const studentYear = document.getElementById("year-in-college").value;
        
            const url = new URL(window.location.href);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            
            const formData = new FormData();
            formData.append('bioText', bioText);
            formData.append('helpText', helpText);
            formData.append('studentYear', studentYear);
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);
        });
    });
}