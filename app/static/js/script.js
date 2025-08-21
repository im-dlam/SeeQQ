

document.getElementById("submit").onclick = () => {

    notice = document.getElementById('success-message')
    notice.style.display = 'block';

    setTimeout(()=> {
        notice.style.display = 'none';
    },3000);
}
