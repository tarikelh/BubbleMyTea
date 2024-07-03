const avatarElement = document.querySelector("#header .avatar");
const menuElement = document.querySelector(".menu");
const closeElement = document.querySelector(".menu .close");
const overlayElement = document.querySelector(".overlay");

avatarElement.addEventListener("click", menuHandler);
closeElement.addEventListener("click", menuHandler);

function menuHandler(event) {
    if (menuElement.style.display === "none") {
        menuElement.style.display = "block";
        overlayElement.style.display = "block";
    } else {
        menuElement.style.display = "none";
        overlayElement.style.display = "none";
    }
}
