function toggleOpenClose(id,toggleId) {
    if(document.getElementById(id).style.display == 'none') {
        document.getElementById(id).style.display = 'block';
        document.getElementById(toggleId).innerText = '△';
    } else {
        document.getElementById(id).style.display = 'none';
        document.getElementById(toggleId).innerText = '▽';
    }
}