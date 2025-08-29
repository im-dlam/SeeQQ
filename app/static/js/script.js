

document.getElementById("submit").addEventListener('click' , () => {

    notice = document.getElementById('success-message')
    notice.style.display = 'block';

    setTimeout(()=> {
        notice.style.display = 'none';
    },3000);
}
)



async function list_items(list_works = []) {

    const ul = document.getElementById('list-works');
    if(!ul){
        return "not found element";
    }
    list_works.forEach(w => {
        let new_child = document.createElement('li');
        new_child.className = 'works';
        
        let span = document.createElement('span');
        let radio = document.createElement('input');
        radio.type = 'checkbox';
        span.textContent = w.name;
        new_child.appendChild(span);
        new_child.appendChild(radio);
        ul.appendChild(new_child)
    })
}