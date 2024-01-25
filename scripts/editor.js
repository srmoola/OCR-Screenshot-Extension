const requestTextData = async (imageLink) => {
  try {
    const response = await fetch("http://127.0.0.1:5000/get-text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text_data: imageLink }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();

    return data;
  } catch (error) {
    console.error("Error:", error);
  }
};

setTimeout(function () {
  const image = document.getElementById("target");

  const cropper = new Cropper(image, {
    aspectRatio: 21 / 5,
    movable: false,
    background: false,
    zoomable: false,
  });

  const button = document.getElementById("crop");
  const dialog = document.querySelector("dialog");
  const closeButton = document.querySelector("dialog button");
  const textDisplay = document.getElementById("ocr-text");
  const copyButton = document.getElementById("copy");
  const searchButton = document.getElementById("search");

  button.addEventListener("click", async () => {
    const croppedImage = cropper.getCroppedCanvas().toDataURL("image/png");
    const textData = await requestTextData(croppedImage);
    textDisplay.innerText = textData.result;
    copyButton.innerText = "Copy to Clipboard";
    dialog.showModal();
  });

  closeButton.addEventListener("click", () => {
    dialog.close();
  });

  copyButton.addEventListener("click", () => {
    navigator.clipboard.writeText(textDisplay.innerText);
    copyButton.innerText = "Copied!";
  });

  searchButton.addEventListener("click", () => {
    window.location.replace(
      "https://www.google.com/search?q=" + textDisplay.innerText
    );
  });
}, 500);
