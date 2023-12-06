function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar 
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })

    .then(function(resp) {
        return resp.json();
    })

    .then(function(data) {
        document.querySelector('#price').innerHTML = 'Цена напитка: ${data.result} рублей';
        document.querySelector('#pay').style.display = '';
    })
};

function pay() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const card = document.querySelector('[name=card]').checked;
    const cvv = document.querySelector('[name=cvv]').checked;

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar,
            card: card,
            cvv: cvv,
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })

    .then(function(resp) {
        return resp.json();
    })

    .then(function(data) {
        document.querySelector('#price').innerHTML = 'Цена напитка: ${data.result} рублей';
        document.querySelector('#pay').style.display = '';
    })
}