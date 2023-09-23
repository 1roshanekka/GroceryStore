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