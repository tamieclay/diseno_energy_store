const revealBtn = document.querySelector('.shop');
const hiddenContent = document.querySelector('#product-1','pro-container','.prod');

function revealContent(){
    if(hiddenContent.classList.contains('#product-1','pro-container','.prod')
    ) {
        hiddenContent.classList.remove('#product-1','pro-container','.prod')
    }else{
        hiddenContent.classList.add('#product-1','pro-container','.prod')
    } 
}

revealBtn.addEventListener('click' , revealContent);