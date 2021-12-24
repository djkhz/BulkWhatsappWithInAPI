let aTags = document.querySelectorAll('span[data-href]');

function onClick(e){
    let target = e.target;
    window.location.replace(target.getAttribute('data-href'));
}

for(let i = 0; i < aTags.length; i++){
    let aTag = aTags[i];
    aTag.addEventListener("click", onClick)
}