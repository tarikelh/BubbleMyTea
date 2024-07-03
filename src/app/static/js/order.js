import * as api from "./api/index.js"
import { getCookies } from "./utils/cookies.js";
import { displayAddModal, addHandler } from "./modal/add.js";
import { displayCart, displayCartTotal, handleCartTotal } from "./cart.js";

const orderElement = document.querySelector("#order");
const cartlistElement = document.querySelector("#cart .cartlist");
const modalElement = document.querySelector(".modal");
const closeModalElement = document.querySelector(".modal .close");
const titleModalElement = document.querySelector(".modal .title");
const containerModalElement = document.querySelector(".modal .container");
const cardElements = document.querySelectorAll(".carditem");
const overlayElement = document.querySelector(".overlay");
const submitCartElement = document.querySelector(".submitcart");

const cart = JSON.parse(localStorage.getItem('bubbletea') || '[]');
const drinks = JSON.parse(orderElement.dataset["drinks"].replaceAll("'", '"'));
const toppings = JSON.parse(orderElement.dataset["toppings"].replaceAll("'", '"'));

cart.forEach(item => {
    const _drink = drinks.find(drink => drink.id === parseInt(item.id));
    cartlistElement.innerHTML += displayCart({ ...item, ..._drink }, toppings);
});

const newCart = cart.map(item => {
    const _drink = drinks.find(drink => drink.id === parseInt(item.id));
    if (_drink) {
        return { ...item, price: _drink.price };
    }
});

const total = handleCartTotal(newCart, toppings);
displayCartTotal(total);

cardElements.forEach(element => {
    const drink = element.dataset
    const handler = cardHandler(drink);
    element.addEventListener("click", handler);
});

closeModalElement.addEventListener("click", modalHandler);

const submitCart = handleSubmitCart();
submitCartElement.addEventListener("click", submitCart)

function modalHandler(event) {
    if (modalElement.style.display === "block") {
        modalElement.style.display = "none";
        overlayElement.style.display = "none";
    }
}

function cardHandler(drink) {
    return event => {
        titleModalElement.textContent = drink.name;
        containerModalElement.innerHTML = displayAddModal(drink);

        const toppingsListElements = document.querySelector(".toppinglist");
        toppingsListElements.innerHTML += toppings.map(topping => (`
            <li class="toppingitem">
                <input type="checkbox" id="topping-${ topping.id }" name="topping-${ topping.id }" value="${ topping.id }" />
                <label for="topping-${ topping.id }">${ topping.name + " | € " + topping.price }</label>
            </li>
        `)).join("");

        addHandler(drink);

        if (modalElement.style.display === "none") {
            modalElement.style.display = "block";
            overlayElement.style.display = "block";
        }
    }
}

function handleSubmitCart() {
    return async (event) => {
        event.preventDefault();

        const cart = JSON.parse(localStorage.getItem('bubbletea') || '[]');
        const newCart = cart.map(item => {
            const _drink = drinks.find(drink => drink.id === parseInt(item.id));
            if (_drink) {
                return { ...item, price: _drink.price };
            }
        });

        const total = handleCartTotal(newCart, toppings);


        const data = {
            command_date: "yyyy/mm/dd",
            state: "process",
            user_id: 1,
            total: total.price,
            cart
        }

        const headers = { "X-CSRFToken": getCookies("csrftoken")  };

        await api.post({ url: "/", data: JSON.stringify(data), headers });
        localStorage.clear();
    };
}
