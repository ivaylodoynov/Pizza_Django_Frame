let updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i <updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function (){
        let pizzaId = this.dataset.pizza
        let action = this.dataset.action
        console.log('pizzaId:', pizzaId, 'Action:', action)

        console.log('USER:', user)
        if (user === 'AnonymousUser'){
            console.log('User is not authenticated')
        }else {
            updateUserOrder(pizzaId, action)
        }
    })
}

function updateUserOrder(pizzaId, action){
    console.log('User is authenticated, sending data...')

    let url = '/store/update_item/'

    fetch(url, {
        method: 'post',
        headers: {
            'Content-Type':'application/json',
            'Accept': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'pizzaId': pizzaId, 'action': action})
    })
    .then((response)=> {
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}