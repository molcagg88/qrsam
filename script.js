const fsapi_url = "localhost";
const urlParams = new URLSearchParams(window.location.search);
const restaurant_id = urlParams.get("restaurant_id");
let currentLanguage = "en"; // default language

async function getMenuData() {
  if (document.getElementById("loader")) {
    document.getElementById("loader").style.display = "block";
  }
  try {
    response = await fetch(`http://${fsapi_url}:5000/menuData/`, {
      method: "POST",
      body: JSON.stringify({
        restaurant_id: restaurant_id,
      }),
      headers: { "Content-Type": "application/json" },
    });
    data = await response.json();
    console.log(data);

    localStorage.setItem("menuData", JSON.stringify(data));
  } catch (err) {
    console.log(err);
    alert(err);
  } finally {
    if (document.getElementById("loader")) {
      document.getElementById("loader").style.display = "none";
    }
  }
}
getMenuData();
menuItems = JSON.parse(localStorage.getItem("menuData"));
async function createMenuItems() {
  const menuGrid = document.querySelector(".menu-grid");

  menuGrid.innerHTML = "";

  Object.entries(menuItems).forEach(([key, item]) => {
    const menuItem = document.createElement("div");
    menuItem.className = "menu-item";
    menuItem.setAttribute("data-category", item.category);
    menuItem.onclick = () => openModal(item);

    menuItem.innerHTML = `
                  <img src="${item.image}" loading='lazy' alt="${item.name}" />
                  <div class="menu-item-content">
                    <div class="menu-item-title">${item.name}</div>
                    <p class="menu-item-ingredients">
                        ${item.ingredients?.[currentLanguage]}
                    </p>
                    <div class="menu-item-price">${item.price}</div>
                  </div>
                `;

    menuGrid.appendChild(menuItem);
  });
}

function openModal(item) {
  const modal = document.getElementById("menuModal");

  document.getElementById("modalImage").src = item.image;
  document.getElementById("modalTitle").textContent = item.name;
  document.getElementById("modalDescription").textContent =
    item.ingredients?.[currentLanguage];

  document.getElementById("modalPrice").textContent = item.price;
  modal.style.display = "flex";
  document.body.classList.add("no-scroll");

  // Small delay before adding the active class for animation
  setTimeout(() => {
    modal.classList.add("active");
    // After modal is shown, set focus to the modal for accessibility
    trapFocus(modal);
  }, 5);
}

function closeModal() {
  const modal = document.getElementById("menuModal");
  modal.classList.remove("active");
  document.body.classList.remove("no-scroll");
  removeTrapFocus();
  setTimeout(() => {
    modal.style.display = "none";
  }, 200);
}

let focusTrapListener = null;

function trapFocus(element) {
  const focusableSelectors = [
    "a[href]",
    "area[href]",
    'input:not([disabled]):not([type="hidden"])',
    "select:not([disabled])",
    "textarea:not([disabled])",
    "button:not([disabled])",
    "iframe",
    "object",
    "embed",
    "[contenteditable]",
    '[tabindex]:not([tabindex="-1"])',
  ];
  const focusableElements = Array.from(
    element.querySelectorAll(focusableSelectors.join(","))
  );

  if (focusableElements.length === 0) {
    element.setAttribute("tabindex", "-1");
    element.focus();
    return;
  }

  // Focus first element or modal itself
  focusableElements[0].focus();

  focusTrapListener = function (e) {
    if (e.key === "Tab") {
      const focusedIndex = focusableElements.indexOf(document.activeElement);
      if (e.shiftKey) {
        // Shift + Tab
        if (focusedIndex === 0) {
          e.preventDefault();
          focusableElements[focusableElements.length - 1].focus();
        }
      } else {
        // Tab only
        if (focusedIndex === focusableElements.length - 1) {
          e.preventDefault();
          focusableElements[0].focus();
        }
      }
    }
  };

  element.addEventListener("keydown", focusTrapListener);
}

function removeTrapFocus() {
  const modal = document.getElementById("menuModal");
  if (focusTrapListener) {
    modal.removeEventListener("keydown", focusTrapListener);
    focusTrapListener = null;
  }
}

// Close modal when clicking outside
window.onclick = function (event) {
  const modal = document.getElementById("menuModal");
  if (event.target == modal) {
    closeModal();
  }
};

// Initialize menu items
createMenuItems();

const translations = {
  en: {
    brand: "YOUR CAFE",
    menu: "Menu",
    snacks: "Snacks",
    drinks: "Drinks",
  },
  am: {
    brand: "የእርስዎ ካፌ",
    menu: "ምን አለ",
    snacks: "ቁርስ",
    drinks: "መጠጦች",
  },
  om: {
    brand: "KAFE KEESSAN",
    menu: "Meeniyuu",
    snacks: "Cunca'u",
    drinks: "Dhugaatii",
  },
  ti: {
    brand: "ካፌኩም",
    menu: "ምን አለ",
    snacks: "ምግባን ናይ ቀሊል ምስናዕ",
    drinks: "መስተ",
  },
};

async function setLanguage(lang) {
  currentLanguage = lang;
  document.querySelectorAll("[data-key]").forEach((el) => {
    const key = el.getAttribute("data-key");
    el.textContent = translations[lang][key] || el.textContent;
  });

  document
    .querySelectorAll(".lang-selector button")
    .forEach((btn) => btn.classList.remove("active"));

  document
    .querySelector(`.lang-selector button[onclick*="${lang}"]`)
    .classList.add("active");

  createMenuItems();

  const modal = document.getElementById("menuModal");
  if (modal && modal.style.display === "flex") {
    const currentTitle = document.getElementById("modalTitle").textContent;
    const currentItem = menuItems.find((item) => item.name === currentTitle);
    if (currentItem) openModal(currentItem);
  }
}

// Filter functionality
document.querySelectorAll(".filter-nav a").forEach((filter) => {
  filter.addEventListener("click", (e) => {
    e.preventDefault();
    const filterValue = filter.getAttribute("data-filter");

    document
      .querySelectorAll(".filter-nav a")
      .forEach((btn) => btn.classList.remove("active"));
    filter.classList.add("active");

    document.querySelectorAll(".menu-item").forEach((item) => {
      if (
        filterValue === "all" ||
        item.getAttribute("data-category") === filterValue
      ) {
        item.style.display = "flex";
      } else {
        item.style.display = "none";
      }
    });
  });
});
