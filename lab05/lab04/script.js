document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Ngăn reload trang

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const errorMsg = document.getElementById("error");

  if (username === "" || password === "") {
    errorMsg.textContent = "Please enter username and password!";
  } else if (password.length < 6) {
    errorMsg.textContent = "Password must be at least 6 characters!";
  } else {
    errorMsg.textContent = "";
    alert("Login successful!"); 
  }
});
