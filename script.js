console.log("JavaScript is successfully connected!");
alert("Hello! This is your browser talking.");
const btn = document.getElementById('colorBtn');

btn.addEventListener('click', function() {
    document.body.style.backgroundColor = 'yellow';
})