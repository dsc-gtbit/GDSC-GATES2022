const LoaderEverytime = () => {
    document.getElementById("page-1-inner").classList.remove("none");
    document.body.style.setProperty('--scroll', "scroll");
    setTimeout(() => {
        document.getElementById("background-animation").classList.remove("none");
    }, 500);
}
const DesktopLoaderFun = () => {
    document.getElementById("loader-overlay").classList.remove("none");
    document.getElementById("base-overlay").classList.add("none");
    setTimeout(() => {
        document.getElementById("loader-text").innerText = "2022";
    }, 1750);
    setTimeout(() => {
        document.getElementById("loader-overlay").classList.add("none");
        LoaderEverytime();
    }, 4000);
}

const MobileLoaderFun = () => {
    document.getElementById("m-loader-overlay").classList.remove("none");
    document.getElementById("base-overlay").classList.add("none");
    setTimeout(() => {
        document.getElementById("m-loader-overlay").classList.add("none");
        LoaderEverytime();
    }, 4000);
}

window.onload = () => {
    if (window.innerWidth >= 993){
        DesktopLoaderFun();
    }
    else{
        MobileLoaderFun();
    }
}