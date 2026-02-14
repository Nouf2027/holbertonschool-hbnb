const API_URL = "http://127.0.0.1:5000/api/v1/places/";

document.addEventListener("DOMContentLoaded", () => {
  loadPriceFilterOptions();
  setupPriceFilterListener();
  checkAuthentication();
});

function getCookie(name) {
  const cookies = document.cookie ? document.cookie.split("; ") : [];
  for (const cookie of cookies) {
    const [key, ...rest] = cookie.split("=");
    if (key === name) return decodeURIComponent(rest.join("="));
  }
  return null;
}

function checkAuthentication() {
  const token = getCookie("token");
  const loginLink = document.getElementById("login-link");

  if (!token) {
    loginLink.style.display = "block";
    clearPlaces();
    return;
  }

  loginLink.style.display = "none";
  fetchPlaces(token);
}

async function fetchPlaces(token) {
  try {
    const res = await fetch(API_URL, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const places = await res.json();
    displayPlaces(places);
    applyPriceFilter();
  } catch (err) {
    console.error("Fetch places failed:", err);
    clearPlaces();
  }
}

function displayPlaces(places) {
  const list = document.getElementById("places-list");
  list.innerHTML = "";

  places.forEach((place) => {
    const price = Number(place.price_per_night) || 0;

    const card = document.createElement("div");
    card.classList.add("place");
    card.dataset.price = String(price);

    card.innerHTML = `
      <h2>
        <a href="place.html?id=${place.id}">
          ${escapeHtml(place.name || "Unnamed place")}
        </a>
      </h2>
      <p>${escapeHtml(place.description || "")}</p>
      <p><strong>Price per night:</strong> ${price}</p>
      <p><strong>Latitude:</strong> ${place.latitude ?? ""}</p>
      <p><strong>Longitude:</strong> ${place.longitude ?? ""}</p>
      <p><strong>Owner:</strong> ${escapeHtml(place.owner_id || "")}</p>
    `;

    list.appendChild(card);
  });
}

function loadPriceFilterOptions() {
  const sel = document.getElementById("price-filter");
  sel.innerHTML = "";

  ["10", "50", "100", "All"].forEach((v) => {
    const opt = document.createElement("option");
    opt.value = v;
    opt.textContent = v;
    sel.appendChild(opt);
  });

  sel.value = "All";
}

function setupPriceFilterListener() {
  document.getElementById("price-filter").addEventListener("change", () => {
    applyPriceFilter();
  });
}

function applyPriceFilter() {
  const value = document.getElementById("price-filter").value;
  const cards = document.querySelectorAll("#places-list .place");

  cards.forEach((card) => {
    const price = Number(card.dataset.price || "0");

    if (value === "All") {
      card.style.display = "block";
      return;
    }

    const max = Number(value);
    card.style.display = price <= max ? "block" : "none";
  });
}

function clearPlaces() {
  const list = document.getElementById("places-list");
  if (list) list.innerHTML = "";
}

function escapeHtml(str) {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
