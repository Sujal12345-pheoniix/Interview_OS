"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { Laptop, Briefcase, Award, GraduationCap, ArrowRight, Upload } from "lucide-react";

export default function NewInterview() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [selectedType, setSelectedType] = useState("");
  const [role, setRole] = useState("");
  const [difficulty, setDifficulty] = useState("medium");

  const handleStart = () => {
    // Navigate straight to mock session ID for sandbox demo
    router.push("/interview/mock-session-id");
  };

  return (
    <div className="max-w-3xl mx-auto flex flex-col gap-8">
      {/* Title */}
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight mb-2">Configure Mock Session</h1>
        <p className="text-zinc-400">Step {step} of 3: {step === 1 ? "Select Domain" : step === 2 ? "Provide Target Role & Resume" : "Review settings"}</p>
      </div>

      {/* Step 1: Select Type */}
      {step === 1 && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <button
            onClick={() => { setSelectedType("se"); setStep(2); }}
            className="glass-card p-8 flex flex-col items-start gap-4 text-left hover:border-violet-500/50"
          >
            <div className="w-12 h-12 rounded-xl bg-violet-500/10 flex items-center justify-center text-violet-500">
              <Laptop className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-bold">Software Engineering</h3>
            <p className="text-zinc-500 text-sm">Backend, Frontend, Full Stack, DSA, System Design, DevOps, AI & Machine Learning.</p>
          </button>

          <button
            onClick={() => { setSelectedType("non-tech"); setStep(2); }}
            className="glass-card p-8 flex flex-col items-start gap-4 text-left hover:border-cyan-500/50"
          >
            <div className="w-12 h-12 rounded-xl bg-cyan-500/10 flex items-center justify-center text-cyan-500">
              <Briefcase className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-bold">Non-Technical Roles</h3>
            <p className="text-zinc-500 text-sm">Product Manager, Marketing, Sales, Operations, Finance, Recruiting.</p>
          </button>
        </div>
      )}

      {/* Step 2: Details */}
      {step === 2 && (
        <div className="glass-card p-8 flex flex-col gap-6">
          <div className="flex flex-col gap-2">
            <label className="text-sm font-semibold">Target Job Role</label>
            <input
              type="text"
              placeholder="e.g. Senior Backend Engineer"
              value={role}
              onChange={(e) => setRole(e.target.value)}
              className="px-4 py-3 rounded-xl border border-zinc-800 bg-zinc-950 text-white outline-none focus:border-violet-500 transition-colors"
            />
          </div>

          <div className="flex flex-col gap-2">
            <label className="text-sm font-semibold">Difficulty Level</label>
            <select
              value={difficulty}
              onChange={(e) => setDifficulty(e.target.value)}
              className="px-4 py-3 rounded-xl border border-zinc-800 bg-zinc-950 text-white outline-none focus:border-violet-500 transition-colors"
            >
              <option value="easy">Easy</option>
              <option value="medium">Medium</option>
              <option value="hard">Hard</option>
              <option value="faang">FAANG Level</option>
            </select>
          </div>

          <div className="flex flex-col gap-2">
            <label className="text-sm font-semibold">Resume upload (Optional)</label>
            <div className="border border-dashed border-zinc-800 rounded-xl p-8 flex flex-col items-center justify-center gap-2 bg-zinc-950/20">
              <Upload className="w-8 h-8 text-zinc-600" />
              <div className="text-sm text-zinc-400 font-semibold">Drag & drop files here</div>
              <div className="text-xs text-zinc-600">Supports PDF, DOCX up to 5MB</div>
            </div>
          </div>

          <div className="flex justify-between mt-4">
            <button onClick={() => setStep(1)} className="px-6 py-3 rounded-lg border border-zinc-800 text-sm font-semibold">
              Back
            </button>
            <button onClick={() => setStep(3)} className="px-6 py-3 rounded-lg bg-violet-600 hover:bg-violet-500 text-sm font-semibold text-white flex items-center gap-2">
              Next <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}

      {/* Step 3: Review */}
      {step === 3 && (
        <div className="glass-card p-8 flex flex-col gap-6">
          <h2 className="text-xl font-bold">Verify Session Details</h2>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <div className="text-zinc-500">Domain</div>
              <div className="font-semibold">{selectedType.toUpperCase()}</div>
            </div>
            <div>
              <div className="text-zinc-500">Target Role</div>
              <div className="font-semibold">{role || "Not Specified"}</div>
            </div>
            <div>
              <div className="text-zinc-500">Difficulty</div>
              <div className="font-semibold">{difficulty.toUpperCase()}</div>
            </div>
          </div>

          <div className="flex justify-between mt-4">
            <button onClick={() => setStep(2)} className="px-6 py-3 rounded-lg border border-zinc-800 text-sm font-semibold">
              Back
            </button>
            <button onClick={handleStart} className="px-8 py-4 rounded-xl bg-gradient-to-r from-violet-600 to-purple-700 hover:from-violet-500 hover:to-purple-600 text-base font-bold text-white shadow-lg shadow-violet-500/25">
              Launch Live Interview
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
