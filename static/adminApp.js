// function rotate() {
//     var change = document.querySelector(".ss");

//     change.style.transform = "rotate(45deg)";
// }

document.addEventListener('DOMContentLoaded', function() {
    // Your JavaScript code here
    // Get the modal
  var modal = document.getElementById("mymodal");

  // Get the button that opens the modal
  var btn = document.getElementById("ass");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal 
  btn.onclick = function() {
    modal.style.display = "block";  
    var change = document.querySelector(".ss");
    change.style.transform = "rotate(45deg)";
  }


  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
    var change = document.querySelector(".ss");
    change.style.transform = "rotate(45deg)";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
      var change = document.querySelector(".ss");
      change.style.transform = "rotate(45deg)";
    }
  }
});


// var rotated = false;
// function rotate() {
//     var change = document.querySelector(".ss");
    
//     change.style.transform = "rotate(45deg)";
//     if (rotated) {
//         change.style.transform = "rotate(0deg)";
//     } else {
//         change.style.transform = "rotate(45deg)";
//     }

//     rotated = !rotated; // Toggle the rotation state
// }


function navMenu_js() {
    document.getElementById("dropdown-listID").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.drop-button')) {
      var dropdowns = document.getElementsByClassName("dropdown-list");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

  function appearanceDark() {
    document.getElementById("view").href="/static/adminDark.css"
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
    document.getElementById("view").href="/static/adminLight.css.css"
    // document.getElementById("view").href="{{ url_for ('static', filename='lightStyle.css') }}"

    document.getElementById("store").src="/static/assets/DownloadOnAppStoreDark.svg"
    // document.getElementById("store").src="{{ url_for ('static', filename='assets/DownloadOnAppStoreDark.svg') }}"

    document.getElementById("profileIcon").src="/static/assets/profileIcon.png"
    // document.getElementById("profileIcon").src="{{ url_for ('static', filename='assets/profileIcon.png') }}"

    document.getElementById("cart").src="/static/assets/cart.png"
    // document.getElementById("cart").src="{{ url_for ('static', filename='assets/cart.png') }}"
    
}

