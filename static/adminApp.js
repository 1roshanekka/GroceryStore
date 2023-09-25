// function rotate() {
//     var change = document.querySelector(".ss");

//     change.style.transform = "rotate(45deg)";
// }
var rotated = false;
function rotate() {
    var change = document.querySelector(".ss");
    
    change.style.transform = "rotate(45deg)";
    if (rotated) {
        change.style.transform = "rotate(0deg)";
    } else {
        change.style.transform = "rotate(45deg)";
    }

    rotated = !rotated; // Toggle the rotation state
}


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