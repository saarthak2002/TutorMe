if (document.readyState !== 'loading') {
    handleSearchButtonPress();
    handleMyRequestsButtonPress();
    handleProfileButtonPress();
} else {
    document.addEventListener('DOMContentLoaded', function () {
        handleSearchButtonPress();
        handleMyRequestsButtonPress();
        handleProfileButtonPress();
    });
}

function setDefaults() {
    localStorage.setItem('student-nav-search', 'inactive');
    localStorage.setItem('student-nav-requests', 'inactive');
    localStorage.setItem('student-nav-profile', 'inactive');
}

function handleSearchButtonPress() {
    const searchButton = document.getElementById('student-nav-search');
    searchButton.addEventListener('click', function() {
        localStorage.setItem('student-nav-search', 'active');
        localStorage.setItem('student-nav-requests', 'inactive');
        localStorage.setItem('student-nav-profile', 'inactive');
    });
}

function handleMyRequestsButtonPress() {
    const requestsButton = document.getElementById('student-nav-requests');
    requestsButton.addEventListener('click', function() {
        localStorage.setItem('student-nav-search', 'inactive');
        localStorage.setItem('student-nav-requests', 'active');
        localStorage.setItem('student-nav-profile', 'inactive');
    });
}

function handleProfileButtonPress() {
    const profileButton = document.getElementById('student-nav-profile');
    profileButton.addEventListener('click', function() {
        localStorage.setItem('student-nav-search', 'inactive');
        localStorage.setItem('student-nav-requests', 'inactive');
        localStorage.setItem('student-nav-profile', 'active');
    });
}
