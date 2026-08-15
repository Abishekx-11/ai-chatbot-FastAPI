
let isSending = false

document.getElementById("first_form").addEventListener("submit", async function(event){
    event.preventDefault();

    if(isSending){
        return
    }

    let user = document.getElementById("chatting");
    let chatbox = document.getElementById("chat-box");
    let sendButton = document.querySelector("#first_form button");


    let userMessage = user.value.trim();

    if (userMessage === "") {
        return;
    }

    // Lock immediately
    isSending = true


     // Immediately clear the input
    user.value = "";

    // Prevent multiple submissions while waiting for Gemini
    user.disabled = true;
    sendButton.disabled = true;

    chatbox.innerHTML += `<p><strong>You: </strong> ${userMessage}</p>`;


    try{
        let serverResponse = await fetch("/chat", {
            method: "POST", 
            headers: {"content-type":"application/json"},
            body:JSON.stringify( {"message": userMessage})
        });

        let responseData = await serverResponse.json();
        chatbox.innerHTML += `<p><strong>AI: </strong> ${responseData.message}</p>`;
    }

    catch (error) {

        chatbox.innerHTML += `<p><strong>AI:</strong> Something went wrong.</p>`;

    } finally {

        // release lock from form , that means, we can send anything again
        isSending = false

        // Allow the user to send another message
        user.disabled = false;
        sendButton.disabled = false;



        // after Gemini responds, instead of you having to click the textbox again, the cursor is automatically ready there
        user.focus();   
    }
});