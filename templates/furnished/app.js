function appearanceDark() {
    document.getElementById("view").href="darkStyle.css"
    document.getElementById("store").src="/static/assets/DownloadOnAppStoreLight.svg"
    document.getElementById("profileIcon").src="/static/assets/profileIconDark.png"
    document.getElementById("cart").src="/static/assets/cartDark.png"

    // if one of the sequencing commands fail then subsequent will not work
    
    
}

function appearanceLight() {
    document.getElementById("view").href="lightStyle.css"
    document.getElementById("store").src="/static/assets/DownloadOnAppStoreDark.svg"
    document.getElementById("profileIcon").src="/static/assets/profileIcon.png"
    document.getElementById("cart").src="/static/assets/cart.png"
    
}

function storeImageDark() {
    document.getEmementById("store").src=""
}

function storeImageLight() {
    document.getElementById("store").src=""
}