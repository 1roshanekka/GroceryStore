function appearanceDark() {
    document.getElementById("view").href="darkStyle.css"
    document.getElementById("store").src="assets/DownloadOnAppStoreLight.svg"
    document.getElementById("cart").src="assets/cartDark.png"
    document.getElementById("profileIcon").src="assets/profileIconDark.png"
    
}

function appearanceLight() {
    document.getElementById("view").href="lightStyle.css"
    document.getElementById("store").src="assets/DownloadOnAppStoreDark.svg"
    document.getElementById("cart").src="assets/cart.png"
    document.getElementById("profileIcon").src="assets/profileIcon.png"
}

function storeImageDark() {
    document.getEmementById("store").src=""
}

function storeImageLight() {
    document.getElementById("store").src=""
}