const API_PLACES_URL = 'http://127.0.0.1:5000/api/v1/places/';
const API_REVIEWS_URL = 'http://127.0.0.1:5000/api/v1/reviews/';

document.addEventListener('DOMContentLoaded', () => {
  const placeId = getPlaceIdFromURL();
  if (!placeId) {
    document.getElementById('place-details').textContent = 'Missing place id in URL.';
    return;
  }

  loadPlace(placeId);
  loadReviews(placeId);

  const form = document.getElementById('review-form');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const token = getCookie('token');
      if (!token) {
        alert('You must be logged in to submit a review.');
        window.location.href = 'login.html';
        return;
      }

      const text = document.getElementById('review-text').value.trim();
      if (!text) {
        alert('Review text is required.');
        return;
      }

      try {
        const res = await fetch(API_REVIEWS_URL, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({ place_id: placeId, text })
        });

        if (!res.ok) {
          const data = await res.json().catch(() => ({}));
          alert(data.error || `Failed to submit review (HTTP ${res.status})`);
          return;
        }

        document.getElementById('review-form').reset();
        await loadReviews(placeId);
        alert('Review submitted');
      } catch (err) {
        console.error(err);
        alert('Network error while submitting review');
      }
    });
  }
});

function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('id');
}

async function loadPlace(id) {
  try {
    const res = await fetch(API_PLACES_URL + id);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const place = await res.json();
    const el = document.getElementById('place-details');
    el.innerHTML = `
      <h2>${escapeHtml(place.title || '')}</h2>
      <p>${escapeHtml(place.description || '')}</p>
      <p><strong>Price:</strong> ${place.price ?? ''}</p>
      <p><strong>Latitude:</strong> ${place.latitude ?? ''}</p>
      <p><strong>Longitude:</strong> ${place.longitude ?? ''}</p>
    `;
  } catch (err) {
    console.error('Load place failed', err);
    document.getElementById('place-details').textContent = 'Failed to load place details.';
  }
}

async function loadReviews(placeId) {
  try {
    const res = await fetch(API_REVIEWS_URL + `?place_id=${encodeURIComponent(placeId)}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const reviews = await res.json();
    const list = document.getElementById('reviews-list');
    list.innerHTML = '';

    if (!reviews || reviews.length === 0) {
      list.textContent = 'No reviews yet.';
      return;
    }

    reviews.forEach(r => {
      const node = document.createElement('div');
      node.className = 'review';
      node.innerHTML = `
        <p><strong>User:</strong> ${escapeHtml(r.user_id || '')}</p>
        <p>${escapeHtml(r.text || '')}</p>
      `;
      list.appendChild(node);
    });
  } catch (err) {
    console.error('Load reviews failed', err);
    const list = document.getElementById('reviews-list');
    if (list) list.textContent = 'Failed to load reviews.';
  }
}

function getCookie(name) {
  const cookies = document.cookie ? document.cookie.split('; ') : [];
  for (const cookie of cookies) {
    const [key, ...rest] = cookie.split('=');
    if (key === name) return decodeURIComponent(rest.join('='));
  }
  return null;
}

function escapeHtml(str) {
  return String(str)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}
