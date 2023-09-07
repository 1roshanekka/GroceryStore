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