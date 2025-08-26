

document.getElementById("submit").addEventListener('click' , () => {

    notice = document.getElementById('success-message')
    notice.style.display = 'block';

    setTimeout(()=> {
        notice.style.display = 'none';
    },3000);
}
)


async function add_work(){
    let work = document.getElementById('work').value;
    let note_id = document.getElementById('list-id').value;
    if (!work) return;
    const res = await fetch('/works', {
        method: 'POST',
        headers: {'Content-type':'application/json'},
        body: JSON.stringify({id: note_id , name: work})
    })
    console.log(res.status , res.ok)
}