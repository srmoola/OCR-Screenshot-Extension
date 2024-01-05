function requestTextData() {
  const response = fetch("http://127.0.0.1:5000/get-text", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text_data: "" }),
  });
  response
    .then((response) => response.json())
    .then((data) => {
      console.log("Response from server:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

requestTextData();
