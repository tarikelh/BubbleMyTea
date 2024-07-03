import { displayCart, displayCartTotal, handleCartTotal } from "../cart.js";

export const displayAddModal = (drink) => (`
    <figure>
        <img src="${ drink.photo }" alt="${ drink.name } picture" />
        <figcaption>
            <div class="description">${ drink.description }</div>
        </figcaption>
    </figure>

    <div class="option">
        <h4>Suppléments</h4>
        <ul class="toppinglist"></ul>

        <div class="sugar">
            <label>Sucre</label>
            <select id="sugarselect" class="sugarquantity">
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </select>
        </div>
    </div>
    <div class="price">${ drink.price }.00 €</div>

    <footer>
        <button id="submitbutton" type="submit">Ajouter</button>
    <footer
`);

export function addHandler(drink) {
    const submitButtonHandler = () => {
        return async (event) => {
            event.preventDefault();

            const orderElement = document.querySelector("#order");
            const overlayElement = document.querySelector(".overlay");
            const modalElement = document.querySelector(".modal");
            const cartlistElement = document.querySelector("#cart .cartlist");
            
            const toppingsList = [];
            const toppingCheckboxElements = document.querySelectorAll("input[type='checkbox']");
            toppingCheckboxElements.forEach(element => (element.checked) && toppingsList.push(element.value));

            const sugarSelectElement = document.querySelector("#sugarselect");
            const quantitySugar = sugarSelectElement.value;

            const _drink = {
                id: drink.id,
                toppings: toppingsList,
                sugar: quantitySugar
            }

            const drinks = JSON.parse(orderElement.dataset["drinks"].replaceAll("'", '"'));
            const toppings = JSON.parse(orderElement.dataset["toppings"].replaceAll("'", '"'));
            const cart = JSON.parse(localStorage.getItem('bubbletea') || '[]');

            cart.push(_drink);

            localStorage.setItem('bubbletea', JSON.stringify(cart));

            cartlistElement.innerHTML = cart.map(item => {
                const _drink = drinks.find(drink => drink.id === parseInt(item.id));
                return displayCart({ ...item, ..._drink }, toppings);
            }).join('');

            const newCart = cart.map(item => {
                const _drink = drinks.find(drink => drink.id === parseInt(item.id));
                if (_drink) {
                    return { ...item, price: _drink.price }
                }
            });
            const total = handleCartTotal(newCart, toppings);
            displayCartTotal(total);

            if ( modalElement.style.display === "block") {
                modalElement.style.display = "none";
                overlayElement.style.display = "none";
            }
        };
    };

    const submitButtonELement = document.querySelector("#submitbutton");
    const submitHandler = submitButtonHandler();
    submitButtonELement.addEventListener("click", submitHandler);
}
