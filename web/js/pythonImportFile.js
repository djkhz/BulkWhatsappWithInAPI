const importBtn = document.querySelector('.import');
const h4 = document.querySelector('#h4');
const show_numbers = document.querySelector('.show_numbers');
const tagTextArea = document.querySelector('#MessageText');
const send = document.querySelector('.send');
const SendingMessage = document.querySelector('.sending');
const showResult = document.querySelector('.show_result');
const sendLog = document.querySelector('.send_log');
const snedMsgBtn = document.querySelector('.sendingBtn');
const finshed = document.querySelector('.Finshed');
const finMsgBtn = document.querySelector('.finMsgBtn');

function select(){
    eel.selectFolder();
    console.log("clicked")
  }
  
importBtn.addEventListener('click', select);
  
function addText(text){
  h4.innerHTML = 'Whatsapp Numbers (' + text + ')';
}
eel.expose(addText);

function addNumbers(Numbers){
  show_numbers.innerHTML += Numbers +"<br>";

}
eel.expose(addNumbers);

function Message(){
  valueTextArea = tagTextArea.value;
  eel.Get_Message(valueTextArea);
  SendingMessage.style.display = "block";
}

send.addEventListener('click', Message);

function Result(text){
  showResult.innerHTML += text + "<br>";
}

eel.expose(Result);

function Log(number){
  sendLog.innerHTML = 'Send Log (' + number + ')';
}

eel.expose(Log);

function MsgBtn(){
  SendingMessage.style.display = "none";
}

snedMsgBtn.addEventListener('click', MsgBtn);

function finshMsg(){
  finshed.style.display = "block";
}

eel.expose(finshMsg);

function FinBtn(){
  finshed.style.display = "none";
}

finMsgBtn.addEventListener('click', FinBtn);