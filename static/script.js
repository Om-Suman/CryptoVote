// Countdown Timer
function startCountdown() {
  let countdownElement = document.getElementById("countdown");
  if (!countdownElement) return;

  let timeParts = countdownElement.textContent.split(":");
  let hours = parseInt(timeParts[0]);
  let minutes = parseInt(timeParts[1]);
  let seconds = parseInt(timeParts[2]);

  function updateTimer() {
    if (seconds === 0) {
      if (minutes === 0) {
        if (hours === 0) {
          countdownElement.textContent = "00:00:00";
          return;
        } else {
          hours--;
          minutes = 59;
        }
      } else {
        minutes--;
      }
      seconds = 59;
    } else {
      seconds--;
    }

    countdownElement.textContent = `${String(hours).padStart(2, "0")}:${String(
      minutes
    ).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;

    setTimeout(updateTimer, 1000);
  }

  setTimeout(updateTimer, 1000);
}

// Run functions after page load
document.addEventListener("DOMContentLoaded", () => {
  startCountdown();
});
