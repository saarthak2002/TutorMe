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
    handleTutorAddingAvailableTimes();
    handleTutorApplication();
    handleReviewButtonPress();
    handleChatButtonPress();
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
        handleTutorAddingAvailableTimes();
        handleTutorApplication();
        handleReviewButtonPress();
        handleChatButtonPress();
    });
}

// Student View - "Search" tab
// "Request" button in student search table
function handleButtonPress() {
    const buttons = document.querySelectorAll('.request-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            self = this;
            
            const popup = document.createElement('div');
            const overlay = document.querySelector('#overlay');
            overlay.style.display = 'block';
            popup.classList.add('time-request-popup', 'p-3', 'bg-white', 'rounded', 'border', 'border-dark')
            popup.innerHTML = `
            <div>
            <h2 class="mb-4">Select a time</h2>
            <div class="form-group">
                <label for="date">Date:</label>
                <input type="date" id="date" name="date" class="form-control" required>
            </div>
            <div class="form-group">
                
                <label>Time:</label><br>
                <div style="display:flex;">
                    <div style="padding:10px;">
                    <input type="radio" id = "time-selection" name = "time-selection" value="8AM-9AM" required> 8AM-9AM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="9AM-10AM" required> 9AM-10AM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="10AM-11AM" required> 10AM-11AM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="11AM-12PM" required> 11AM-12PM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="12PM-1PM" required> 12PM-1PM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="1PM-2PM" required> 1PM-2PM
                    <br>
                    <input type="radio"  id = "time-selection" name = "time-selection" value="2PM-3PM" required> 2PM-3PM
                    <br>
                    </div>
                    <div style="padding:10px;">
                    <input type="radio" id = "time-selection" name = "time-selection" value="3PM-4PM" required> 3PM-4PM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="4PM-5PM" required> 4PM-5PM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="5PM-6PM" required> 5PM-6PM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="6PM-7PM" required> 6PM-7PM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="7PM-8PM" required> 7PM-8PM
                    <br>
                    <input type="radio" id = "time-selection" name = "time-selection" value="8PM-9PM" required> 8PM-9PM
                    </div>
                </div>
                
            </div>
            <div class="buttons">
                <button id="submit" class="btn btn-primary">Submit</button>
                <button id="cancel" class="btn btn-danger">Cancel</button>
            </div>
            </div>
            `;
            window.scrollTo(0, 0);
            document.body.appendChild(popup);
            
            const { top, left, height } = button.getBoundingClientRect();
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const popupTop = top + scrollTop + height;
            popup.style.position = 'absolute';
            popup.style.top = "20%";
            popup.style.left = "50%";
            popup.style.zIndex = "2";
            const submitButton = popup.querySelector('#submit');
            const cancelButton = popup.querySelector('#cancel');
            
            submitButton.addEventListener('click', function() {
                const data = self.getAttribute('request-data');
                const selectedTimeBox = popup.querySelector('input[name="time-selection"]:checked');
                const date = popup.querySelector('#date').value;
                const selectedDate = new Date(date)
                const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
                const selectDayOfWeek = daysOfWeek[selectedDate.getUTCDay()];
                if(selectedTimeBox == null){
                    alert("please select a time");
                }
                else if(date == ""){
                    alert("please select a date");
                }
                // else if(selectDayOfWeek == "Saturday" || selectDayOfWeek == "Sunday"){
                //     alert("please select week day");
                // }
                else {
                    selectedTime = selectedTimeBox.value;
                    const url = new URL(window.location.href);
                    url.searchParams.set('data', encodeURIComponent(data));
                    url.searchParams.set('time', encodeURIComponent(selectedTime));
                    url.searchParams.set('date', encodeURIComponent(date));

                    const xhr = new XMLHttpRequest();
                    xhr.open('GET', url.toString());
                    xhr.onload = function() {
                        const response = xhr.responseText;
                        window.location.href = url.toString();
                    };
                    xhr.send();
                    
                    popup.remove();
                    overlay.style.display = 'none';
                }
            });
            cancelButton.addEventListener('click', function(){
                popup.remove();
                overlay.style.display = 'none';
            });
        });
    });
    if (document.querySelector('.found-tutors-in-search-unique')) {
        window.scrollTo(0, document.body.scrollHeight);
    }
    if (document.querySelector('.no-tutor')) {
        window.scrollTo(0, document.body.scrollHeight);
    }
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
            const date = this.getAttribute('date_requested');
            const time = this.getAttribute('time_requested');
            const startTime = time.split("-")[0]; 
            const endTime = time.split("-")[1]; 
            const url = new URL(window.location.href);

            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            const formData = new FormData();
            formData.append('from', from);
            formData.append('to', to);
            formData.append('course', course);
            formData.append('date', date);
            formData.append('start', startTime);
            formData.append('end', endTime);
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);
            this.disabled = true;
            this.innerHTML = 'Request Sent';

        });
    });
}

function handleReviewButtonPress() {
    const buttons = document.querySelectorAll('.request-card-review-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            
            var csrftoken = Cookies.get('csrftoken');
            const to = this.getAttribute('to_tutor');
            const url = "/tutorme/review/?tutor=" + to;
            this.disabled = true;
            this.innerHTML = 'Reviewed';
            window.location.href = url;

        });
    });
}

function handleChatButtonPress() {
    const buttons = document.querySelectorAll('.tutor-card-chat-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            
            var csrftoken = Cookies.get('csrftoken');
            const from = this.getAttribute('from_user');
            const to = this.getAttribute('to_tutor');

            const url = new URL(window.location.href);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            const formData = new FormData();

            formData.append('from', from);
            formData.append('to', to);
            formData.append('csrfmiddlewaretoken', csrftoken);
            formData.append('value', 'new_chat');
            xhr.send(formData);
            this.disabled = true;
            this.innerHTML = 'Processing...';

            setTimeout(function() {
                window.location.href = "/tutorme/chats/";
            }, 2000)
            
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

function handleTutorEditProfileButton(){
    const buttons = document.querySelectorAll('.tutor-edit-bio-button')
    buttons.forEach(function(button){
        button.addEventListener('click', function(){
            let csrftoken = Cookies.get('csrftoken');
            const bioText = document.getElementById("edit-tutor-bio-textbox").value;
            const hourlyRate = document.getElementById("hourly-rate").value;
            const value = parseFloat(hourlyRate);
            if (isNaN(value) && hourlyRate != "" || value < 0 && hourlyRate != ""|| value > 9999.99 && hourlyRate != "") {
              alert('Please enter a number between 0 and 9999.99');
              document.getElementById("hourly-rate").value = 0; 
            }else{
                this.disabled = true;
                this.innerHTML = "Processing...";
                const xhr = new XMLHttpRequest();
                const url = new URL(window.location.href);

                xhr.open('POST', url.toString());
                
                const formData = new FormData();
                formData.append('bio', bioText);
                formData.append('hourlyRate', hourlyRate);
                formData.append('csrfmiddlewaretoken', csrftoken);

                xhr.send(formData);

                setTimeout(function() {
                    window.location.href = "/tutorme/tutor/profiles/";
                }, 2000)
            }
        });
    });

}

function handleStudentEditProfileButton(){
    const buttons = document.querySelectorAll('.student-profile-edit-button')
    buttons.forEach(function(button){
        button.addEventListener('click', function(){
            this.disabled = true;
            this.innerHTML = "Processing...";
            
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

            setTimeout(function() {
                window.location.href = "/tutorme/profile/";
            }, 2000)
        });
    });
}

function handleTutorAddingAvailableTimes(){
    const buttons = document.querySelectorAll('.tutor-select-available-times-button');
    buttons.forEach(function(button){
        button.addEventListener('click', function(){
            
            const daysOfTheWeek = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday'];
            const mondayCheckedBoxes = [];
            const tuesdayCheckedBoxes = [];
            const wednesdayCheckedBoxes = [];
            const thursdayCheckedBoxes = [];
            const fridayCheckedBoxes = [];
            const saturdayCheckedBoxes = [];
            const sundayCheckedBoxes = [];
            for(let i = 0; i < daysOfTheWeek.length; i++){
                const day = daysOfTheWeek[i] + '-available-times';
                const dayFormGroup = document.querySelector('.'+day);
                const checkboxes = dayFormGroup.querySelectorAll('input[type="checkbox"]');
                checkboxes.forEach(function(checkbox) {
                    if (checkbox.checked) {
                        if(daysOfTheWeek[i] == 'monday'){
                            mondayCheckedBoxes.push(checkbox.value); 
                        }
                        if(daysOfTheWeek[i] == 'tuesday'){
                            tuesdayCheckedBoxes.push(checkbox.value); 
                        }
                        if(daysOfTheWeek[i] == 'wednesday'){
                            wednesdayCheckedBoxes.push(checkbox.value); 
                        }
                        if(daysOfTheWeek[i] == 'thursday'){
                            thursdayCheckedBoxes.push(checkbox.value); 
                        }
                        if(daysOfTheWeek[i] == 'friday'){
                            fridayCheckedBoxes.push(checkbox.value); 
                        }
                        if(daysOfTheWeek[i] == 'saturday'){
                            saturdayCheckedBoxes.push(checkbox.value); 
                        }
                        if(daysOfTheWeek[i] == 'sunday'){
                            sundayCheckedBoxes.push(checkbox.value); 
                        }
                    }
                });
            }
            
            var csrftoken = Cookies.get('csrftoken');
            const tutor = this.getAttribute('tutor');
            const url = new URL(window.location.href);
            this.disabled = true;
            this.innerHTML = "Processing...";

            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());

            const formData = new FormData();
            formData.append('csrfmiddlewaretoken', csrftoken);
            formData.append('mondayTimes', mondayCheckedBoxes)
            formData.append('tuesdayTimes', tuesdayCheckedBoxes)
            formData.append('wednesdayTimes', wednesdayCheckedBoxes)
            formData.append('thursdayTimes', thursdayCheckedBoxes)
            formData.append('fridayTimes', fridayCheckedBoxes)
            formData.append('saturdayTimes', saturdayCheckedBoxes)
            formData.append('sundayTimes', sundayCheckedBoxes)
            xhr.send(formData);
            setTimeout(function() {
                location.reload();
            }, 2000);  
        });
    });
}

function handleTutorApplication(){
    const buttons = document.querySelectorAll('.prior-experience-button');
    buttons.forEach(function(button){
        button.addEventListener('click', function(){
            const url = new URL(window.location.href);
            let csrftoken = Cookies.get('csrftoken');
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url.toString());
            const formData = new FormData();
            formData.append('csrfmiddlewaretoken', csrftoken);
            xhr.send(formData);
            this.innerHTML = "Applied";
            setTimeout(function() {
                window.location.href = window.location.origin + '/tutorme/';
            }, 3000); 
        });
    }); 
}
                