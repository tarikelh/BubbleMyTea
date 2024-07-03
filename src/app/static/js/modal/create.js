import * as api from "../api/index.js"
import { getCookies } from "../utils/cookies.js";

export const displayCreateModal = `
    <div class="formdata">
        <label>Nom</label>
        <input id="productname" />
    </div>
    <div class="formdata">
        <label>Photo</label>
        <input id="picture" type="file" accept="image/*f" />
    </div>
    <div class="formdata">
        <label>Description</label>
        <textarea id="description"></textarea>
    </div>
    <div class="formdata">
        <label>Prix</label>
        <input id="price" />
    </div>

    <button id="cancelbutton">Annuler</button>
    <button id="submitbutton" type="submit">Créer</button>
`;

export function createHandler() {
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
            event.preventDefault();

            const productname = document.querySelector("#productname");
            const picture = document.querySelector("#picture");
            const description = document.querySelector("#description");
            const price = document.querySelector("#price");

            const formData = new FormData();
            formData.append("csrfmiddlewaretoken", getCookies("csrftoken"));
            formData.append("name", productname.value);
            formData.append("photo", picture.files[0]);
            formData.append("description", description.value);
            formData.append("price", price.value);

            const headers = { "X-CSRFToken": getCookies("csrftoken")  };

            await api.post({ url: "/admin/", data: formData, headers });
            closeModal()
        };
    };

    const cancelButtonElement = document.querySelector("#cancelbutton");
    const cancelHandler = cancelButtonHandler();
    cancelButtonElement.addEventListener("click", cancelHandler);

    const submitButtonELement = document.querySelector("#submitbutton");
    const submitHandler = submitButtonHandler();
    submitButtonELement.addEventListener("click", submitHandler);
}
