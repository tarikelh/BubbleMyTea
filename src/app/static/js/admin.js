import { displayCreateModal, createHandler } from "./modal/create.js";
import { displayModifyModal, modifyHandler } from "./modal/modify.js";
import { displayDeleteModal, deleteHandler } from "./modal/delete.js";

const modalElement = document.querySelector(".modal");
const closeModalElement = document.querySelector(".modal .close");
const titleModalElement = document.querySelector(".modal .title");
const containerModalElement = document.querySelector(".modal .container");
const actionElements = document.querySelectorAll(".action");
const overlayElement = document.querySelector(".overlay");

actionElements.forEach(element => {
    const drinkId = element.dataset["id"];
    const handler = actionHandler(element, drinkId);
    element.addEventListener("click", handler);
});

closeModalElement.addEventListener("click", modalHandler);

function modalHandler(event) {
    if (modalElement.style.display === "block") {
        modalElement.style.display = "none";
        overlayElement.style.display = "none";
    }
}

function actionHandler(element, drinkId) {
    return event => {
        if (element.textContent === "Ajouter une boisson") {
            titleModalElement.textContent = "Créer une Boisson";
            containerModalElement.innerHTML = displayCreateModal;
            createHandler()
        } else if (element.textContent === "Modifier") {
            titleModalElement.textContent = "Modifier une Boisson";
            containerModalElement.innerHTML = displayModifyModal;
            modifyHandler(drinkId)
        } else if (element.textContent === "Supprimer") {
            titleModalElement.textContent = "Supprimer une Boisson";
            containerModalElement.innerHTML = displayDeleteModal;
            deleteHandler(drinkId)
        }

        if (modalElement.style.display === "none") {
            modalElement.style.display = "block";
            overlayElement.style.display = "block";
        }
    }
}
