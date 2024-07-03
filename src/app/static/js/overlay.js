const overlayElement = document.querySelector(".overlay");
const modalElement = document.querySelector(".modal");
const menuElement = document.querySelector(".menu");

overlayElement.addEventListener("click", overlayHandler)

function overlayHandler(event) {
    // if (modalElement.style.display === "block") {
    //     modalElement.style.display = "none";
    //     overlayElement.style.display = "none";
    // }
    
    if ( menuElement.style.display === "block") {
        menuElement.style.display = "none";
        overlayElement.style.display = "none";
    }
}