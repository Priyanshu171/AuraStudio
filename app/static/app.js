async function generate() {
    const title = document.getElementById("title").value;
    const tone = document.getElementById("tone").value;
    const format = document.getElementById("format").value;
    const include_images = document.getElementById("images").checked;

    const outputDiv = document.getElementById("output");
    outputDiv.innerHTML = "Generating...";

    const payload = {
        title,
        tone,
        format,
        include_images
    };

    try {
        const res = await fetch("http://localhost:8000/api/generate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(payload)
        });

        const data = await res.json();

        let imagesText = "";

        if (data.images && Array.isArray(data.images)) {
            imagesText = data.images.length > 0
                ? data.images.join("\n")
                : "No images generated.";
        } else {
            imagesText = "Images field missing in response.";
        }

        outputDiv.innerHTML =
            `✔ Content saved at:\n${data.text_path}\n\n` +
            `✔ Images:\n${imagesText}`;

    }
    catch (err) {
        outputDiv.innerHTML = "❌ Error: " + err.message;
    }
}
