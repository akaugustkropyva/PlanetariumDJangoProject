document.addEventListener('DOMContentLoaded', function() {
    updateButton = document.getElementsByClassName('update-cart');

    for(let i = 0; i < updateButton.length; i ++) {
        updateButton[i].addEventListener('click', function(){
            let eventId = this.dataset.event;
            let eventDate = this.dataset.event_date;

           console.log("eventDate")
           console.log(eventDate)

            let action = this.dataset.action;
            console.log('eventId:', eventId, 'eventDate:', eventDate, 'action:', action)

            console.log('USER:', user)
            if(user === 'AnonymousUser'){
                addCookieItem(eventId, eventDate, action)
            } else {
                updateUserOrder(eventId, eventDate, action)
            }

        })

    }
});

function addCookieItem(eventId, eventDate, action){
    console.log("User is not authenticating")


    if (action === 'add') {
        if (cart[eventId] === undefined) {
            cart[eventId] = {};
        }

        if (cart[eventId][eventDate] === undefined) {
            cart[eventId][eventDate] = {'quantity': 1};
        } else {
            cart[eventId][eventDate]['quantity'] += 1;
        }
    }


    if (action === 'remove') {
        cart[eventId][eventDate]['quantity'] -= 1

        if(cart[eventId][eventDate]['quantity'] <=0) {
            console.log('Remove item')
            delete cart[eventId][eventDate]
        }
    }

    if (action === 'delete-item'){
        console.log('Remove item')
        delete cart[eventId][eventDate]

    }

    if (action === 'delete-all'){
        cart = {}
    }
    console.log("Cart:", cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(eventId, eventDate, action) {
    console.log('User is logged in, sending data..')

    let url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'eventId': eventId,
            'eventDate': eventDate,
            'action': action,
        })
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}