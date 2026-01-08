import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_desc", jobDesc);

    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>ResumeRoast.ai</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br /><br />

      <textarea
        rows="6"
        cols="60"
        placeholder="Paste job description..."
        value={jobDesc}
        onChange={(e) => setJobDesc(e.target.value)}
      />

      <br /><br />

      <button onClick={analyze}>Analyze</button>

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>ATS Score: {result.ats_score}%</h2>
          <h3>Matched Keywords</h3>
          <pre>{JSON.stringify(result.matched_keywords, null, 2)}</pre>
          <h3>Missing Keywords</h3>
          <pre>{JSON.stringify(result.missing_keywords, null, 2)}</pre>
          <h3>AI Analysis</h3>
          <pre>{result.ai_analysis}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
