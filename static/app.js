function appearanceDark() {
    document.getElementById("view").href="/static/darkStyle.css"
    // document.getElementById("view").href="{{ url_for ('static', filename='darkStyle.css') }}"
    
    // this templating is only done in jinja within HTML File

    document.getElementById("store").src="/static/assets/DownloadOnAppStoreLight.svg"
    // document.getElementById("store").src="{{ url_for ('static', filename='assets/DownloadOnAppStoreLight.svg') }}"

    document.getElementById("profileIcon").src="/static/assets/profileIconDark.png"
    // document.getElementById("profileIcon").src="{{ url_for ('static', filename='assets/profileIconDark.png') }}"

    document.getElementById("cart").src="/static/assets/cartDark.png"
    // document.getElementById("cart").src="{{ url_for ('static', filename='assets/cartDark.png') }}"

    var passedParams = '{{ param }}'

    // if one of the sequencing commands fail then subsequent will not work
    
    
}

function appearanceLight() {
    document.getElementById("view").href="/static/lightStyle.css"
    // document.getElementById("view").href="{{ url_for ('static', filename='lightStyle.css') }}"

    document.getElementById("store").src="/static/assets/DownloadOnAppStoreDark.svg"
    // document.getElementById("store").src="{{ url_for ('static', filename='assets/DownloadOnAppStoreDark.svg') }}"

    document.getElementById("profileIcon").src="/static/assets/profileIcon.png"
    // document.getElementById("profileIcon").src="{{ url_for ('static', filename='assets/profileIcon.png') }}"

    document.getElementById("cart").src="/static/assets/cart.png"
    // document.getElementById("cart").src="{{ url_for ('static', filename='assets/cart.png') }}"
    
}

function storeImageDark() {
    document.getEmementById("store").src=""
}

function storeImageLight() {
    document.getElementById("store").src=""
}

function rotateAnimation() {
    document.getElementById("rotate")
}

// Create an element to test the font
var testElement = document.createElement('div');

// Set the font family to the one you want to check
testElement.style.fontFamily = 'Young Serif, sans-serif'; // Replace 'Young Serif' with the actual font name

// Set some text content to see if the font affects it
testElement.textContent = 'Testing Font Loading';

// Set the position to off-screen
testElement.style.position = 'absolute';
testElement.style.left = '-9999px';
testElement.style.top = '-9999px';

// Append the element to the document body
document.body.appendChild(testElement);

// Check if the computed font family matches the one you set
var computedFontFamily = window.getComputedStyle(testElement).fontFamily;

// Check if the computed font family contains the font name you set
var fontLoaded = computedFontFamily.includes('Young Serif');

// Clean up: Remove the test element from the document
document.body.removeChild(testElement);

// Now 'fontLoaded' will be true if the font is loaded, and false otherwise
if (fontLoaded) {
    console.log('Font is loaded!');
} else {
    console.log('Font is not loaded!');
}


document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        var fadeInText = document.getElementById('fadeInText');
        fadeInText.classList.remove('hidden');
    }, 2000); 
})

