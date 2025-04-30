import React, { useState } from "react";
import { PlayIcon, StopIcon, ClockIcon, Cog6ToothIcon, ChartBarIcon } from "@heroicons/react/24/solid";

function App() {
  const [status, setStatus] = useState("Idle");
  const [delay, setDelay] = useState(0);

  const handleStart = async () => {
    setStatus("Starting...");
    try {
      const res = await fetch("http://127.0.0.1:8000/start");
      if (res.ok) setStatus("Detection Running");
      else setStatus("Failed to Start");
    } catch (err) {
      setStatus("Error Starting Detection");
    }
  };

  const handleStop = async () => {
    setStatus("Stopping...");
    try {
      const res = await fetch("http://127.0.0.1:8000/stop");
      if (res.ok) setStatus("Detection Stopped");
      else setStatus("Failed to Stop");
    } catch (err) {
      setStatus("Error Stopping Detection");
    }
  };

  const handleSetDelay = async () => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/set-delay?value=${delay}`, {
        method: "POST"
      });
      if (res.ok) setStatus(`Delay set to ${delay}s`);
      else setStatus("Failed to set delay");
    } catch (err) {
      setStatus("Error setting delay");
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-blue-100 text-gray-800">
      {/* Navbar */}
      <nav className="bg-white shadow-md px-6 py-4 flex justify-between items-center">
        <h1 className="text-xl font-bold text-blue-700">Smart Glasses</h1>
        <div className="flex gap-6">
          <button className="text-gray-600 hover:text-blue-600 flex items-center gap-1">
            <Cog6ToothIcon className="h-5 w-5" /> Settings
          </button>
          <button className="text-gray-600 hover:text-blue-600 flex items-center gap-1">
            <ChartBarIcon className="h-5 w-5" /> Stats
          </button>
        </div>
      </nav>

      <main className="p-6 flex flex-col justify-center items-center">
        <div className="bg-white shadow-2xl rounded-3xl p-10 max-w-lg w-full border border-blue-200">
          <h1 className="text-4xl font-black text-center text-blue-700 mb-6">
            Dashboard
          </h1>
          <p className="text-center text-base text-gray-600 mb-8">
            Status: <span className="font-semibold text-blue-900">{status}</span>
          </p>

          <div className="flex flex-col gap-5">
            <button
              className="flex items-center justify-center gap-3 bg-green-500 text-white font-bold py-3 px-6 rounded-2xl shadow-lg hover:bg-green-600 transition-all"
              onClick={handleStart}
            >
              <PlayIcon className="h-6 w-6" /> Start Detection
            </button>

            <button
              className="flex items-center justify-center gap-3 bg-red-500 text-white font-bold py-3 px-6 rounded-2xl shadow-lg hover:bg-red-600 transition-all"
              onClick={handleStop}
            >
              <StopIcon className="h-6 w-6" /> Stop Detection
            </button>

            <div className="flex gap-3 items-center">
              <input
                type="number"
                value={delay}
                onChange={(e) => setDelay(e.target.value)}
                className="flex-1 px-4 py-2 border border-gray-300 rounded-xl shadow focus:ring-2 focus:ring-blue-400 focus:outline-none"
                placeholder="Set Delay (seconds)"
              />
              <button
                className="flex items-center gap-2 bg-blue-500 text-white font-bold py-2 px-5 rounded-2xl shadow-lg hover:bg-blue-600 transition-all"
                onClick={handleSetDelay}
              >
                <ClockIcon className="h-5 w-5" /> Set
              </button>
            </div>
          </div>
        </div>

        {/* Stats Panel */}
        <div className="mt-10 w-full max-w-4xl grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white p-6 rounded-2xl shadow text-center">
            <h2 className="text-lg font-bold text-gray-700">Objects Detected</h2>
            <p className="text-3xl font-extrabold text-blue-600 mt-2">--</p>
          </div>
          <div className="bg-white p-6 rounded-2xl shadow text-center">
            <h2 className="text-lg font-bold text-gray-700">Current Delay</h2>
            <p className="text-3xl font-extrabold text-blue-600 mt-2">{delay}s</p>
          </div>
          <div className="bg-white p-6 rounded-2xl shadow text-center">
            <h2 className="text-lg font-bold text-gray-700">System Status</h2>
            <p className="text-3xl font-extrabold text-blue-600 mt-2">{status}</p>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
