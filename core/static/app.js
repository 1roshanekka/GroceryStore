function appearanceDark() {
    document.getElementById("view").href="/static/darkStyle.css"
    
    // document.getElementById("logo").src="/static/assets/transformerDark.png"

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

    // document.getElementById("logo").src="/static/assets/transformerLight.png"

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


var testElement = document.createElement('div');


testElement.style.fontFamily = 'Young Serif, sans-serif'; 


testElement.textContent = 'Testing Font Loading';


testElement.style.position = 'absolute';
testElement.style.left = '-9999px';
testElement.style.top = '-9999px';


document.body.appendChild(testElement);


var computedFontFamily = window.getComputedStyle(testElement).fontFamily;


var fontLoaded = computedFontFamily.includes('Young Serif');


document.body.removeChild(testElement);


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

function updateID(userID) {

    window.location.href = `/update/${userID}`;
  }
function deleteID(userID) {
    window.location.href = `/delete/${userID}`;
}

// function register() {
//     confirm("You have been registered")

//     if(flag){
//         window.location.href = `/deleteCategory/${categoryId}`;
//       }
//       else{
//         console.log('cancelled')

//       }
//   }



// var reg = document.getElementById('register');
// reg.addEventListener('click', function(event) {
//     event.preventDefault(); 
//     alert('Registration successful!')
// });