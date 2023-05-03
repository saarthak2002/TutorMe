# Tutor Me Project

## What is Tutor Me?
Tutor Me is a web application that matches students with tutors on a college campus. The app uses the university's courses API to get all the courses. Then, tutors and students can sign up with Google accounts and schedule sessions. The app also has additional features like chat, reviews, ratings, and profiles.
##### Technology
Tutor Me is based on the MVC architecture and uses a PostgreSQL Database in the backend. The app was originally deployed on Heroku. GitHub actions was used for the CI/CD pipeline. The app offers two dashboards for the two user types- students and tutors.

### Landing Page
![Tutor Me landing page](/screenshots/landing.png)

### Student Search
#### A student can search for a class which queries a REST API for classes.
![Tutor Me Search Student](/screenshots/s-search-1.png)
#### On clicking request, a popup is displayed to select a date and time slot for the session.
![Tutor Me Search Student](/screenshots/s-search-2.png)
#### The search results for tutors for that course available at the requested time are shown.
![Tutor Me Search Student](/screenshots/s-search-3.png)
The student can read other students' reviews for that tutor, chat with them, or send a request for a session.

### Tutor Requests Page

The tutor can accept or decline requests. The system even sends an email to the student if their request is accepted.

![Tutor Requests Page](/screenshots/tutor-requests.png)

### Chat Page

Tutors and students can chat with each other on the platform.

![List of Chats](/screenshots/tutor-chats.png)

#### Tutor Chat UI

![Chat UI](/screenshots/chat1.png)

#### Student Chat UI

![Chat UI](/screenshots/chat2.png)

#### View Reviews For Tutor

![Review View UI](/screenshots/student-view-reviews.png)

### Student Requests Page
The student can view and modify their requests, and leave a review for a tutor.
![Student Requests](/screenshots/student-requests.png)

#### Review a tutor
![Review UI](/screenshots/student-leave-review.png)

### Tutor Home Page

Shows the upcoming accepted sessions a tutor has in the next 7 days.

![Tutor Home Page](/screenshots/tutor-home.png)

### Tutor My Classes View

The tutor can view their tutored classes and remove them if needed.

![Tutor Classes Page](/screenshots/tutor-classes.png)

### Tutor Add Classes Page

The tutor can search for courses the college offers and add them to the list of classes they tutor for.

![Tutor Add Classes Page](/screenshots/tutor-add-classes.png)

### Tutor Availability Page

The tutor can select slots they want to tutor for.

![Tutor Time Page](/screenshots/tutor-times.png)

### Tutor Profile Page

The profile displays info about the tutor like profile picture, name, email, username, hourly rate, bio, courses tutored, and reviews. The user can even edit their profile with the edit button.

![Tutor Home Page](/screenshots/tutor-profile.png)

### Student Profile Page

The profile displays info about the student like profile picture, name, email, username, class year, bio, courses requested, and what they need help with. The user can even edit their profile with the edit button.

![Student Profile Page](/screenshots/student-profile.png)
