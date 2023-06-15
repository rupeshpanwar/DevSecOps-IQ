function toggleAnswer(sectionId) {
    const section = document.getElementById(sectionId);
    section.classList.toggle('active');
    const content = section.nextElementSibling;
    if (content.style.display === 'block') {
      content.style.display = 'none';
    } else {
      content.style.display = 'block';
    }
  }
  