document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  const text = `Новое сообщение с сайта:%0AИмя: ${name}%0AEmail: ${email}%0AСообщение: ${message}`;

  const token = "ВАШ_ТОКЕН_БОТА";
  const chat_id = "5925170010";

  const url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${text}`;

  fetch(url)
  .then(response => {
    document.getElementById("status").innerText = "Сообщение отправлено!";
  })
  .catch(error => {
    document.getElementById("status").innerText = "Ошибка отправки";
  });
});

  const url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${text}`;

  fetch(url)
  .then(response => {
    document.getElementById("status").innerText = "Сообщение отправлено!";
  })
  .catch(error => {
    document.getElementById("status").innerText = "Ошибка отправки";
  });
});
