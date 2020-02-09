// the ui form for tertiary applicant -- appears when tertiary is selected from education level field
function displayTertiaryApplication() {
  const tertiaryForm = document.querySelector('.tertiary');
  const eduLevel = document.querySelector('#education-level').value;

  if (eduLevel === 'Tertiary') {
    tertiaryForm.style.display = 'block';
  } else {
    tertiaryForm.style.display = 'none';
  }
}

displayTertiaryApplication()