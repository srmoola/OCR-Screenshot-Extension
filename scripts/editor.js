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
    aspectRatio: 16 / 9,
    movable: false,
    background: false,
    zoomable: false,
  });

  const button = document.getElementById("crop");

  button.addEventListener("click", async () => {
    const croppedImage = cropper.getCroppedCanvas().toDataURL("image/png");
    const textData = await requestTextData(croppedImage);
    console.log(textData);
  });
}, 500);
