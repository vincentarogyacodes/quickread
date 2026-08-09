const button = document.getElementById("quick-read-button");
const status = document.getElementById("status");
const input = document.getElementById("url-input");
const aiSummary = document.getElementById("summarized-text");

button.addEventListener("click", async function () {
    const url = input.value.trim();

    if (url === "") {
        status.textContent = "Please enter a URL";
        return;
    }

    if (!url.startsWith("http://") && !url.startsWith("https://")) {
        status.textContent = "Please enter a valid URL";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();
        aiSummary.textContent = data.message;

    } catch (error) {
        console.log("catch block ran");
        console.log(error);
        status.textContent = "Could not connect to the backend";
    }
});