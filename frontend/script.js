const API_BASE = "https://sgp3fkd9h9.execute-api.ap-south-1.amazonaws.com";

const form = document.getElementById("shorten-form");
const input = document.getElementById("url-input");
const submitBtn = document.getElementById("submit-btn");
const errorMsg = document.getElementById("error-msg");
const result = document.getElementById("result");
const shortLinkEl = document.getElementById("short-link");
const copyBtn = document.getElementById("copy-btn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  errorMsg.hidden = true;
  result.hidden = true;

  const url = input.value.trim();
  if (!url) return;

  submitBtn.disabled = true;
  submitBtn.textContent = "Shortening…";

  try {
    const res = await fetch(`${API_BASE}/links`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url }),
    });

    if (!res.ok) {
      throw new Error("Request failed");
    }

    const data = await res.json();
    const shortLink = `${API_BASE}/links/${data.short_code}`;

    shortLinkEl.textContent = shortLink;
    shortLinkEl.href = shortLink;
    result.hidden = false;
  } catch (err) {
    errorMsg.textContent = "Couldn't shorten that link. Try again.";
    errorMsg.hidden = false;
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Shorten";
  }
});

copyBtn.addEventListener("click", () => {
  navigator.clipboard.writeText(shortLinkEl.textContent);
  copyBtn.textContent = "Copied";
  setTimeout(() => {
    copyBtn.textContent = "Copy";
  }, 2000);
});
