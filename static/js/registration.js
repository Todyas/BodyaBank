// explanation:
// 1. get the values of the two password inputs
// 2. if the values are not equal, show an alert and prevent the form from submitting
// fix:
// use trim() to remove whitespace from the password inputs (e.g. when user copies and pastes a password)

document.querySelector("form").addEventListener("submit", function (event) {
  const password1 = document.getElementById("InputPassword1").value.trim();
  const password2 = document.getElementById("InputPassword2").value.trim();
  if (password1 !== password2) {
    alert("Пароли не совпадают!");
    event.preventDefault();
  }
});
