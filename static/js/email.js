//email

const btn = document.getElementById('sendMessageButton');

document.getElementById('contactForm')
  .addEventListener('submit', function(event) {
    event.preventDefault();

    btn.value = 'Sending...';

    const serviceID = 'default_service';
    const templateID = 'contact_form';

    emailjs.sendForm(serviceID, templateID, this)
      .then(() => {
        btn.value = 'Send Email';
        alert('Sent!');
        this.reset();  // Clear the form after successful submission
      }, (err) => {
        btn.value = 'Send Email';
        alert(JSON.stringify(err));
      });
  });