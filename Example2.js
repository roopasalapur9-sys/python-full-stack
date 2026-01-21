<script>
document.getElementById("myForm").addEventListener("submit", function (e)) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();
  const error = document.getElementById("error");

  error.textContent = "";

  
  if (name === "") {
    error.textContent = "Name is required.";
    return;
  }

  
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    error.textContent = "Enter a valid email address.";
    return;
  }

  
  if (password.length < 6) {
    error.textContent = "Password must be at least 6 characters.";
    return;
  }

  alert("Form submitted successfully!");
});
</script>