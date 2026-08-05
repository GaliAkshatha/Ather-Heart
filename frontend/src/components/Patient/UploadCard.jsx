import React, { useState } from "react"
import API from "../../api"

export default function UploadCard({ onExtract }) {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleUpload = async (e) => {
    const file = e.target.files[0]
    if (!file) return

    setLoading(true)
    setError(null)

    const formData = new FormData()
    formData.append("file", file)

    try {
      const res = await API.post("/ocr/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" }
      })
      onExtract(res.data.extracted, res.data.missing_fields)
    } catch (err) {
      setError(
        err.response?.data?.error || "Could not process that image. Please try again."
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mt-6 p-6 bg-white rounded-xl shadow border w-full">
      <h2 className="text-xl font-semibold mb-4">Upload Lab Report</h2>

      <input 
        type="file" 
        accept="image/*"
        onChange={handleUpload}
        className="mt-3"
      />

      {loading && <p className="mt-4 text-gray-600">Extracting data…</p>}
      {error && <p className="mt-4 text-red-600">{error}</p>}
    </div>
  )
}
