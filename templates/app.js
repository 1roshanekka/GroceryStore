function appearanceDark() {
    document.getElementById("view").href="darkStyle.css"
    document.getElementById("store").src="assets/DownloadOnAppStoreLight.svg"
    document.getElementById("profileIcon").src="assets/profileIconDark.png"
    document.getElementById("cart").src="assets/cartDark.png"

    // if one of the sequencing commands fail then subsequent will not work
    
    
}

function appearanceLight() {
    document.getElementById("view").href="lightStyle.css"
    document.getElementById("store").src="assets/DownloadOnAppStoreDark.svg"
    document.getElementById("profileIcon").src="assets/profileIcon.png"
    document.getElementById("cart").src="assets/cart.png"
    
}

function storeImageDark() {
    document.getEmementById("store").src=""
}

function storeImageLight() {
    document.getElementById("store").src=""
}