 if (document.readyState !== 'loading') {
    console.log('document is already ready, just execute code here');
    handleButtonPress();
} else {
    document.addEventListener('DOMContentLoaded', function () {
        console.log('document was not ready, place code here');
        handleButtonPress();
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
                // Update the DOM as needed
                window.location.href = url.toString();
              };
            xhr.send();
            
        });
    });
}