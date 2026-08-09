
document.getElementById("first_form").addEventListener("submit", async function(event){
    event.preventDefault();

    let userMessage = document.getElementById("chatting").value;
    let chatbox = document.getElementById("chat-box");
    chatbox.innerHTML += `<p><strong>You: </strong> ${userMessage}</p>`;

    let serverResponse = await fetch("/chat", {
        method: "POST", 
        headers: {"content-type":"application/json"},
        body:JSON.stringify( {"message": userMessage})
    });

    let responseData = await serverResponse.json();
    chatbox.innerHTML += `<p><strong>AI: </strong> ${responseData.message}</p>`;

    document.getElementById("chatting").value = "";

});