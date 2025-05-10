async function ask() {
  const question = document.getElementById("question").value;
  const responseDiv = document.getElementById("response");
  responseDiv.innerHTML = "Sto pensando...";
  const res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });
  const data = await res.json();
  if (data.error) {
    responseDiv.innerHTML = `<p><strong>Errore:</strong> ${data.error}</p>`;
  } else {
    responseDiv.innerHTML = `<p><strong>Risposta:</strong> ${data.answer}</p><p><strong>SQL:</strong> ${data.sql || "-"}</p>${data.table || ""}`;
  }
}