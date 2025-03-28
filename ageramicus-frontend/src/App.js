import './App.css';

function App() {
  // This function will run when user uploads an image
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    // This will call our backend API (once it's ready)
    const response = await fetch("http://127.0.0.1:8000/analyze-image", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    alert("AI says: " + result.prediction);
  };

  return (
    <div className="App" style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1 style={{ color: 'green', fontSize: '2rem' }}>🌱 AgerAmicus</h1>
      <p>Upload a crop image to detect plant disease using AI.</p>

      <input type="file" onChange={handleUpload} style={{ marginTop: '20px' }} />
    </div>
  );
}

export default App;
