

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
        new_child.textContent = w.name;
        document.getElementById('list-works').appendChild(new_child)
    })
}