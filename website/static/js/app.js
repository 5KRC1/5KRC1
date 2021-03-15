let card = document.querySelectorAll('.character');

card.forEach((e) => {
    e.addEventListener('click', () => {
        if(e.classList.value != 'character'){
            e.classList.toggle('active');
            e.classList.add('character');
        }
        else{
            removeActiveClasses();
            e.classList.toggle('active');
            e.classList.remove('character')
        }
    });
})

function removeActiveClasses(){
    card.forEach(e => {
        e.classList.remove('active');
        e.classList.add('character');
    })
}

