async function add_work(){
    let work = document.getElementById('work').value;
    let note_id = document.getElementById('list-id').value;
    if (!work) return;
    const res = await fetch('/works', {
        method: 'POST',
        headers: {'Content-type':'application/json'},
        body: JSON.stringify({id: note_id , name: work})
    })
    window.location.reload();
}


async function list_work() {
    let note_id = document.getElementById('list-id').value;

    try {
        const res = await fetch(`/list-works/${note_id}`, {
            method: 'GET',
            headers: {'Content-type':'application/json'}
        })   
    
        if (res.status !==  200) return ;

        const data = await res.json();
        
        // Show list work
        await list_items(data);
    }
    catch(e){
        return e;
    }

}

