const statusELements = document.querySelectorAll(".status span");

statusELements.forEach(element => {
    if (element.textContent === "En cours") {
        element.style.backgroundColor = "#e69710";
    } else if (element.textContent === "Terminé") {
        element.style.backgroundColor = "#42b992";
    } else {
        element.style.backgroundColor = "#bf5155";
    }
});