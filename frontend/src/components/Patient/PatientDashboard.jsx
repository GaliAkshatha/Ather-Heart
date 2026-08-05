import React, { useState } from "react"
import UploadCard from "./UploadCard"
import FormFallback from "./FormFallback"
import InputForm from "./InputForm"
import ResultCard from "./ResultCard"
import API from "../../api"
import chopper from "../../assets/chopper.png"

export default function PatientDashboard() {
  const [mode, setMode] = useState(null) // upload OR form
  const [extracted, setExtracted] = useState(null)
  const [missingFields, setMissingFields] = useState([])
  const [prediction, setPrediction] = useState(null)
  const [error, setError] = useState(null)

  const resetAll = () => {
    setExtracted(null)
    setMissingFields([])
    setPrediction(null)
    setError(null)
  }

  const handleExtract = (ex, missing) => {
    setExtracted(ex)
    setMissingFields(missing)
  }

  const handleFinalSubmit = async (data) => {
    setError(null)
    try {
      const res = await API.post("/predict/patient", data)
      setPrediction(res.data)
    } catch (err) {
      setError(
        err.response?.data?.error || "Could not get a prediction. Please check your entries and try again."
      )
    }
  }

  return (
    <div className="pt-28 max-w-5xl mx-auto px-6 min-h-screen">

      {/* Page Title */}
      <h1 className="text-3xl font-semibold mb-6">Patient Dashboard</h1>

      {/* Mode Buttons */}
      {!mode && (
        <div className="flex gap-6">
          <button 
            onClick={() => { resetAll(); setMode("upload") }}
            className="px-5 py-3 rounded bg-black text-white hover:bg-gray-800"
          >
            Upload Report
          </button>

          <button 
            onClick={() => { resetAll(); setMode("form") }}
            className="px-5 py-3 rounded bg-black text-white hover:bg-gray-800"
          >
            Fill Form Manually
          </button>
        </div>
      )}

      {/* Chopper Helper */}
      {mode && (
        <div className="mt-6 flex items-center gap-4">
          <img 
            src={chopper} 
            alt="Chopper" 
            className="w-24 h-24 rounded-full border shadow"
          />
          <p className="text-gray-700 text-lg">
            Hi! I'm Chopper! I'll help you check your heart health.  
            {mode === "upload" ? "Upload your report to get started!" : "Fill the form to continue!"}
          </p>
        </div>
      )}

      {error && (
        <p className="mt-4 text-red-600">{error}</p>
      )}

      {/* ========== UPLOAD MODE ========== */}
      {mode === "upload" && (
        <>
          {!extracted && <UploadCard onExtract={handleExtract} />}

          {extracted && missingFields.length > 0 && (
            <FormFallback
              extracted={extracted}
              missing={missingFields}
              onSubmit={handleFinalSubmit}
            />
          )}

          {prediction && <ResultCard prediction={prediction} />}
        </>
      )}

      {/* ========== FORM MODE ========== */}
      {mode === "form" && (
        <>
          {!prediction && (
            <InputForm onSubmit={handleFinalSubmit} />
          )}

          {prediction && <ResultCard prediction={prediction} />}
        </>
      )}

    </div>
  )
}
