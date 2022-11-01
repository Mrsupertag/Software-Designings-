const password = document.getElementById('password')
const username = document.getElementById('username')

document.getElementById('form').addEventListener('sumbit", (event) => {
event.preventDefault()
valid = true

const password_value = password.value
const username_value = username.value

if (username_value.length < 5 || password_value.length < 12) {
  alert('The form has not been submitted : \n - A field is not valid.')
  valid = false 

if (valid)
  alert('The form has been completed. \n We will proceed with the sending.')

})
