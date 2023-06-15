function toggleSection(sectionId) {
  const sections = document.getElementsByClassName('section');
  for (let i = 0; i < sections.length; i++) {
    const section = sections[i];
    section.style.display = section.id === sectionId ? 'block' : 'none';
  }
}
