function faceRecognition() {
  const id = document.getElementById("employeeId").value;
  const action = document.querySelector('input[name="entryExit"]:checked').value;
  alert(`Face Recognition triggered for ID: ${id} (${action})`);
}

function fingerprintScan() {
  const id = document.getElementById("employeeId").value;
  const action = document.querySelector('input[name="entryExit"]:checked').value;
  alert(`Fingerprint Scan triggered for ID: ${id} (${action})`);
}
