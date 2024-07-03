import * as api from "../api/index.js"
import { getCookies } from "../utils/cookies.js";

export const displayDeleteModal = `
    Êtes vous sûr de supprimer cette boisson ?

    <button id="cancelbutton">Annuler</button>
    <button id="submitbutton" type="submit">Supprimer</button>
`;

export function deleteHandler(drinkId) {
    const closeModal = () => {
        const overlayElement = document.querySelector(".overlay");
        const modalElement = document.querySelector(".modal");

        if ( modalElement.style.display === "block") {
            modalElement.style.display = "none";
            overlayElement.style.display = "none";
        }
    };

    const cancelButtonHandler = () => {
        return (event) => {
            closeModal()
        };
    };

    const submitButtonHandler = () => {
        return async (event) => {
            const headers = { "X-CSRFToken": getCookies("csrftoken")  };

            await api.del({ url: `/admin/${ drinkId }/`, headers });
            closeModal()
        }
    };

    const cancelButtonElement = document.querySelector("#cancelbutton");
    const cancelHandler = cancelButtonHandler();
    cancelButtonElement.addEventListener("click", cancelHandler);

    const submitButtonELement = document.querySelector("#submitbutton");
    const submitHandler = submitButtonHandler();
    submitButtonELement.addEventListener("click", submitHandler);
}
