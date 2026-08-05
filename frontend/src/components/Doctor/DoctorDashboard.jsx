import React, { useState, useEffect } from "react"
import ShapTable from "./ShapTable"
import PatientList from "./PatientList"
import TrendGraph from "./TrendGraph"
import API from "../../api"

export default function DoctorDashboard() {

  const [selectedPatient, setSelectedPatient] = useState(null)
  const [shapData, setShapData] = useState(null)
  const [error, setError] = useState(null)

  const handleView = async (patient) => {
    setSelectedPatient(patient)
    setError(null)

    try {
      const res = await API.post("/predict/doctor", patient)
      setShapData(res.data)
    } catch (err) {
      setShapData(null)
      setError(
        err.response?.data?.error || "Could not load SHAP data for this patient."
      )
    }
  }

  return (
    <div className="pt-28 px-6 max-w-6xl mx-auto">
      
      <h1 className="text-3xl font-semibold mb-6">Doctor Dashboard</h1>

      {/* Patient Table */}
      <PatientList onView={handleView} />

      {error && <p className="mt-4 text-red-600">{error}</p>}

      {/* SHAP Analysis */}
      {shapData && (
        <div className="mt-10">
          <h2 className="text-2xl font-semibold mb-4">
            SHAP Feature Impact (For Selected Patient)
          </h2>
          <ShapTable data={shapData} />
        </div>
      )}

      {/* Trend Graph */}
      <div className="mt-10">
        <h2 className="text-2xl font-semibold mb-4">Predicted Risk Trend</h2>
        <TrendGraph />
      </div>
    </div>
  )
}
