// the ui form for tertiary applicant -- appears when tertiary is selected from education level field
function displayTertiaryApplication() {
  const tertiaryForm = document.querySelector('.tertiary');
  const secondaryForm = document.querySelector('.secondary');

  const eduLevel = document.querySelector('#education-level').value;

  if (eduLevel === 'Tertiary') {
    secondaryForm.style.display = 'none';
    tertiaryForm.style.display = 'block';
  }
  else if (eduLevel === 'Secondary') {
    tertiaryForm.style.display = 'none';
    secondaryForm.style.display = 'block';
  }
  else {
    tertiaryForm.style.display = 'none';
    secondaryForm.style.display = 'none';
  }
}

displayTertiaryApplication()