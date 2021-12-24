const importBtn = document.querySelector('.import');
const h4 = document.querySelector('#h4');
const show_numbers = document.querySelector('.show_numbers');

function select(){
    eel.selectFolder();
    console.log("clicked")
  }
  
  importBtn.addEventListener('click', select);
  
function addText(text){
  h4.innerHTML = 'Whatsapp Numbers: (' + text + ')';
}
eel.expose(addText);

function addNumbers(Numbers){
  show_numbers.innerHTML += '+' + Numbers +"<br>";

}
eel.expose(addNumbers);