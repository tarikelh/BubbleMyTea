export const displayCart = (bubbletea, toppings) => {
  const toppingsList = [];

  if (bubbletea.toppings.length > 0) {
    bubbletea.toppings.forEach(toppingId => {
      const matchingTopping = toppings.find(topping => topping.id === parseInt(toppingId));
      if (matchingTopping) toppingsList.push(matchingTopping.name);
    });
  }

  return (`
    <li class="cartitem" data-id="${ bubbletea.id }">
      <h4>${ bubbletea.name }</h4>
      <ul class="toppingslist"></ul>
    </li>
  `)
};

export const displayCartTotal = ({ price }) => {
  const cartTotalElement = document.querySelector("#carttotal");
  cartTotalElement.textContent = "€ " + price
}

export const handleCartTotal = (cart, toppings) => {
  const calculateToppingsPrice = (bubbletea) => {
    let toppingsPrice = 0;
    if (bubbletea.toppings.length > 0) {
      bubbletea.toppings.forEach(toppingId => {
        const matchingTopping = toppings.find(topping => topping.id === parseInt(toppingId));
        if (matchingTopping) toppingsPrice += matchingTopping.price;
      });
    }

    return toppingsPrice;
  };

  const totalPrice = cart.reduce((total, bubbletea) => {
    let bubbleTeaPrice = bubbletea.price;
    const toppingsPrice = calculateToppingsPrice(bubbletea);
    bubbleTeaPrice += toppingsPrice;

    return total + bubbleTeaPrice;
  }, 0);

  return { price: totalPrice };
};