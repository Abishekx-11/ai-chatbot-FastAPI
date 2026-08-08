
document.getElementById("first_form").addEventListener("submit", async function(event){
    event.preventDefault();

    let userMessage = document.getElementById("chatting").value;

    let serverResponse = await fetch("/chat", {
        method: "POST", 
        headers: {"content-type":"application/json"},
        body:JSON.stringify( {"message": userMessage})
    });

    let responseData = await serverResponse.json();
    document.getElementById("output").innerText = responseData.message;


});