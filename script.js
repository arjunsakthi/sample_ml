document.addEventListener("DOMContentLoaded", function () {
  const stressRange = document.getElementById("stress-range");
  const stressNumber = document.getElementById("stress-number");
  const form = document.querySelector("form");
  const athulMindTitle = document.getElementById("athul-mind-title");

  // Synchronize range input and number input
  stressRange.addEventListener("input", function () {
    stressNumber.value = stressRange.value;
  });

  stressNumber.addEventListener("input", function () {
    if (stressNumber.value >= 1 && stressNumber.value <= 1000) {
      stressRange.value = stressNumber.value;
    }
  });

  // Form validation
  form.addEventListener("submit", function (event) {
    if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
    } else {
      // Perform your form submission logic here
    }
    form.classList.add("was-validated");
  });

  // Number input validation
  stressNumber.addEventListener("input", function () {
    const value = parseInt(stressNumber.value, 10);
    if (isNaN(value) || value < 1 || value > 1000) {
      stressNumber.setCustomValidity(
        "Please enter a value between 1 and 1000."
      );
    } else {
      stressNumber.setCustomValidity("");
    }
  });

  // Handle the form submission
  form.addEventListener("submit", async function (event) {
    event.preventDefault();
    if (form.checkValidity()) {
      try {
        const stressLevel = stressNumber.value;
        const API_BASE_URL = "{{RENDER_EXTERNAL_URL}}";
        const response = await fetch("${API_BASE_URL}/api/stress", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({ stressLevel: stressLevel }),
        });

        if (response.ok) {
          const data = await response.json();
          athulMindTitle.textContent = `Athul's Mind: ${data.result}`;
        } else {
          athulMindTitle.textContent = `Error: ${response.statusText}`;
        }
      } catch (error) {
        athulMindTitle.textContent = `Error: ${error.message}`;
      }
    }
  });
});
