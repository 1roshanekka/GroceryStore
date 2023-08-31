function appearanceDark() {
    document.getElementById("view").href="darkStyle.css"
    document.getElementById("store").src="assets/DownloadOnAppStoreLight.svg"
}

function appearanceLight() {
    document.getElementById("view").href="lightStyle.css"
    document.getElementById("store").src="assets/DownloadOnAppStoreDark.svg"
}

function storeImageDark() {
    document.getEmementById("store").src=""
}

function storeImageLight() {
    document.getElementById("store").src=""
}