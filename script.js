function toggleSection(sectionId) {
    const sections = document.getElementsByClassName('section');
    for (let i = 0; i < sections.length; i++) {
      sections[i].style.display = 'none';
    }
    const section = document.getElementById(sectionId);
    section.style.display = 'block';
  }
  
  function toggleAnswer(elementId) {
    const element = document.getElementById(elementId);
    element.classList.toggle('active');
    const content = element.nextElementSibling;
    if (content.style.display === 'block') {
      content.style.display = 'none';
    } else {
      content.style.display = 'block';
    }
  }
  