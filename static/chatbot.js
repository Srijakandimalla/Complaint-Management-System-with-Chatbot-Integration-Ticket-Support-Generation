function sendMessage(){

let msg = document.getElementById("message").value

if(msg.trim() === ""){
return
}

fetch("/chatbot",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({message:msg})

})

.then(res=>res.json())

.then(data=>{

let chat=document.getElementById("chatbox")

chat.innerHTML += "<div><b>👤 You:</b> "+msg+"</div>"

chat.innerHTML += "<div><b>🤖 Bot:</b> "+data.reply+"</div>"

chat.scrollTop = chat.scrollHeight

})

document.getElementById("message").value=""

}