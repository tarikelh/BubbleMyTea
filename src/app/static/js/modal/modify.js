import * as api from "../api/index.js"
import { getCookies } from "../utils/cookies.js";

export const displayModifyModal = `
    <div class="formdata">
        <label>Nom</label>
        <input id="productname" name="name" />
    </div>
    <div class="formdata">
        <label>Photo</label>
        <input id="picture" name="photo" type="text" />
    </div>
    <div class="formdata">
        <label>Description</label>
        <textarea id="description" name="description"></textarea>
    </div>
    <div class="formdata">
        <label>Prix</label>
        <input id="price" name="price" />
    </div>

    <button id="cancelbutton">Annuler</button>
    <button id="submitbutton" type="submit">Créer</button>
`;

export function modifyHandler(drinkId) {
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
            closeModal();
        };
    };

    const submitButtonHandler = () => {
        return async (event) => {
            event.preventDefault();

            const productname = document.querySelector("#productname");
            const picture = document.querySelector("#picture");
            const description = document.querySelector("#description");
            const price = document.querySelector("#price");

            const data = {
                "csrfmiddlewaretoken": getCookies("csrftoken"),
                "name": productname.value,
                "photo": picture.value,
                "description": description.value,
                "price": price.value
            }

            const headers = { "X-CSRFToken": getCookies("csrftoken"), "Content-Type": "application/json" };

            await api.put({ url: `/admin/${ drinkId }/`, data: JSON.stringify(data), headers });

            // closeModal();
        };
    };

    const cancelButtonElement = document.querySelector("#cancelbutton");
    const cancelHandler = cancelButtonHandler();
    cancelButtonElement.addEventListener("click", cancelHandler);

    const submitButtonELement = document.querySelector("#submitbutton");
    const submitHandler = submitButtonHandler();
    submitButtonELement.addEventListener("click", submitHandler);
}
