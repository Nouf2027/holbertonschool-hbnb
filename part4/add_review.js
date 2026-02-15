const API_REVIEWS_URL = "http://127.0.0.1:5000/api/v1/reviews/";

document.addEventListener("DOMContentLoaded", () => {
  const token = checkAuthentication();
  const placeId = getPlaceIdFromURL();

  if (!placeId) {
    showMsg("Missing place id in URL. Use add_review.html?id=PLACE_ID", false);
    return;
  }

  const form = document.getElementById("review-form");
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const reviewText = document.getElementById("review-text").value.trim();
    const rating = Number(document.getElementById("review-rating").value);

    if (!reviewText) {
      showMsg("Review text is required.", false);
      return;
    }

    if (!Number.isFinite(rating) || rating < 1 || rating > 5) {
      showMsg("Rating must be between 1 and 5.", false);
      return;
    }

    await submitReview(token, placeId, reviewText, rating);
  });
});

function checkAuthentication() {
  const token = getCookie("token");
  if (!token) {
    window.location.href = "index.html";
    return null;
  }
  return token;
}

function getCookie(name) {
  const cookies = document.cookie ? document.cookie.split("; ") : [];
  for (const cookie of cookies) {
    const [key, ...rest] = cookie.split("=");
    if (key === name) return decodeURIComponent(rest.join("="));
  }
  return null;
}

function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get("id");
}

async function submitReview(token, placeId, reviewText, rating) {
  try {
    const payload = {
      user_id: token,
      place_id: placeId,
      text: reviewText,
      rating: rating,
    };

    const res = await fetch(API_REVIEWS_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      let errMsg = `Failed to submit review (HTTP ${res.status}).`;
      try {
        const data = await res.json();
        if (data && data.message) errMsg = data.message;
      } catch (_) {}
      showMsg(errMsg, false);
      return;
    }

    showMsg("Review submitted successfully!", true);
    document.getElementById("review-form").reset();
  } catch (e) {
    console.error(e);
    showMsg("Network error while submitting review.", false);
  }
}

function showMsg(text, ok) {
  const msg = document.getElementById("msg");
  msg.style.display = "block";
  msg.textContent = text;
  msg.style.color = ok ? "green" : "red";
}
