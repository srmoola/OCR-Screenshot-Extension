setTimeout(function () {
  const image = document.getElementById("target");

  const cropper = new Cropper(image, {
    aspectRatio: 16 / 9,
    movable: false,
    background: false,
    zoomable: false,
  });

  const button = document.getElementById("crop");

  button.addEventListener("click", () => {
    var croppedimage = cropper.getCroppedCanvas().toDataURL("image/png");
    console.log(croppedimage);
  });
}, 500);
