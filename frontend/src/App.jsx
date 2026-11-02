import { useState } from 'react'

export default function App() {
  const [file, setFile] = useState(null)
  const [results, setResults] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handlePredict = async () => {
    if (!file) {
      setError('Please choose a CSV file first')
      return
    }
    setLoading(true)
    setError('')
    setResults([])

    const formData = new FormData()
    formData.append('file', file)

    try {
      const res = await fetch('/predict', { method: 'POST', body: formData })
      const data = await res.json()
      if (!res.ok) setError(data.error || 'Something went wrong')
      else setResults(data)
    } catch (e) {
      setError('Could not reach the server')
    }
    setLoading(false)
  }

  return (
    <div style={{ maxWidth: 700, margin: '40px auto', fontFamily: 'sans-serif', padding: 16 }}>
      <h1>Gene Expression Cancer Prediction</h1>
      <p>Upload a gene expression CSV and the model will predict the cancer type.</p>
      <p><a href="/sample.csv" download>Download a sample file to try</a></p>

      <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handlePredict} disabled={loading} style={{ marginLeft: 10 }}>
        {loading ? 'Predicting...' : 'Predict'}
      </button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {results.length > 0 && (
        <table border="1" cellPadding="8" style={{ marginTop: 20, borderCollapse: 'collapse', width: '100%' }}>
          <thead>
            <tr><th>Sample</th><th>Prediction</th><th>Confidence</th></tr>
          </thead>
          <tbody>
            {results.map((r) => (
              <tr key={r.sample}>
                <td>{r.sample}</td>
                <td>{r.prediction}</td>
                <td>{(r.confidence * 100).toFixed(1)}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      <p style={{ marginTop: 30, fontSize: 12, color: 'gray' }}>
        For educational purposes only. Not a medical diagnosis.
      </p>
    </div>
  )
}