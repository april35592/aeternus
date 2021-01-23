var reply_h3 = document.querySelectorAll(".reply_list h3");
var reply_diraction = document.querySelectorAll(".reply_list span");
var reply_p = document.querySelectorAll(".reply_list p");

for (let i = 0; i < reply_h3.length; i++) {
    reply_h3[i].onclick = function(event) {
        if(reply_p[i].style.display == 'none') {
            reply_p[i].style.display = 'block';
            reply_diraction[i].innerText = '△';
        } else {
            reply_p[i].style.display = 'none';
            reply_diraction[i].innerText = '▽';
        }
    }
}