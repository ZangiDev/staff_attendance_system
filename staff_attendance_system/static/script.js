let streamStarted = false;

async function startCamera() {
  if (streamStarted) return;

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    const video = document.getElementById('video');
    video.srcObject = stream;
    video.style.display = 'block';
    streamStarted = true;
  } catch (err) {
    console.error('Camera error:', err);
    alert('Could not access the webcam.');
  }
}

function stopCamera() {
  const video = document.getElementById('video');
  const stream = video.srcObject;
  if (stream) {
    stream.getTracks().forEach(track => track.stop());
  }
  video.srcObject = null;
  video.style.display = 'none';
  streamStarted = false;
}

async function faceRecognition() {
  const empId = document.getElementById('employeeId').value.trim();
  const action = document.querySelector('input[name="entryExit"]:checked').value;

  if (!empId) {
    alert('Please enter an Employee ID first.');
    return;
  }

  await startCamera();

  // Wait for 1 second so camera can adjust
  setTimeout(async () => {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imgData = canvas.toDataURL('image/png');

    try {
      const res = await fetch('/face-auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          employee_id: empId,
          entry_exit: action,
          image: imgData
        })
      });

      const data = await res.json();

      // ✅ Stop camera after response
      stopCamera();

      // ✅ Show result
      if (data.success) {
        alert('✅ Face recognition successful!');
      } else {
        alert('❌ Face not recognized.');
      }

    } catch (err) {
      console.error(err);
      stopCamera();
      alert('Something went wrong while processing.');
    }
  }, 1000);
}

function fingerprintScan() {
  const empId = document.getElementById('employeeId').value.trim();
  const action = document.querySelector('input[name="entryExit"]:checked').value;
  alert(`Fingerprint Scan triggered for ID: ${empId} (${action})`);
}
