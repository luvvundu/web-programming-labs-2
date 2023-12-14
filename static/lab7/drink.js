function getPrice() {
    const milk = document.querySelector ('[name = milk]').checked;
    const sugar = document. querySelector ('[name = sugar]').checked;
    const drink = document.querySelector ('[name = drink]:checked') .value; 
            
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
        .then (function (data) {
            document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб`;
            document. querySelector('#pay').style.display = '';
            })
}

function pay(){
    const milk = document.querySelector('[name = milk]').checked;
    const sugar = document. querySelector('[name = sugar]').checked;
    const drink = document.querySelector('[name = drink]:checked') .value; 
    const card_num = document.querySelector('[name = card]').value;
    const cvv = document.querySelector('[name = cvv]').value;
            
    const obj = {
            "method": "pay",
            "params": {
                drink: drink, 
                milk: milk, 
                sugar: sugar,
                card_num: card_num,
                cvv: cvv
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
        .then (function (data) {
            if(data.result != null){
                document.getElementById('pay_result').innerHTML = data.result
            }
            else if(data.error != null){
                document.getElementById('pay_result').innerHTML = data.error 
            }
        })
}

function refund(){
    const milk = document.querySelector('[name = milk]').checked;
    const sugar = document. querySelector('[name = sugar]').checked;
    const drink = document.querySelector('[name = drink]:checked') .value; 
    const card_num = document.querySelector('[name = card]').value;
    const cvv = document.querySelector('[name = cvv]').value;
     
    const first_obj = {
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
        body: JSON.stringify(first_obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function (data) {
        const obj = {
            "method": "refund",
            "params": {
                card_num: card_num,
                cost: data.result
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
        .then (function (data) {
            if(data.result != null){
                document.getElementById('pay_result').innerHTML = data.result
            }
            else if(data.error != null){
                document.getElementById('pay_result').innerHTML = data.error 
            }
        })  
    })

}