// agromart
function showSection(section) {
  document.getElementById('business').style.display = 'none';
  document.getElementById('farmer').style.display = 'none';
  document.getElementById(section).style.display = 'block';
  
  document.getElementById('btn-business').classList.remove('active');
  document.getElementById('btn-farmer').classList.remove('active');
  document.getElementById('btn-' + section).classList.add('active');
}
showSection('business');