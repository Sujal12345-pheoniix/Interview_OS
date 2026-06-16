"use client";

import React from "react";
import Link from "next/link";
import { CheckCircle2, AlertTriangle, ArrowRight, BookOpen, Clock, Heart, Award } from "lucide-react";

export default function ReportPage() {
  return (
    <div className="max-w-5xl mx-auto flex flex-col gap-10">
      {/* Top Banner Recommendation */}
      <div className="glass-card p-8 bg-gradient-to-r from-emerald-950/20 via-zinc-900/50 to-transparent flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-3">
            🟢 Strong Hire
          </div>
          <h1 className="text-3xl font-extrabold tracking-tight mb-2">Technical Interview Analysis</h1>
          <p className="text-zinc-400">Software Engineering (Backend) • June 16, 2026</p>
        </div>
        <div className="flex flex-col items-center gap-1">
          <div className="text-sm text-zinc-500 font-bold">OVERALL SCORE</div>
          <div className="text-5xl font-black text-emerald-400">88<span className="text-lg font-normal text-zinc-500">/100</span></div>
        </div>
      </div>

      {/* Metric Breakdown Radar Columns */}
      <div className="grid grid-cols-1 md:grid-cols-5 gap-6">
        <div className="glass-card p-6 flex flex-col items-center text-center gap-2">
          <div className="text-zinc-500 text-xs font-bold uppercase">Communication</div>
          <div className="text-3xl font-bold text-violet-400">92%</div>
          <div className="text-xs text-zinc-500 mt-2">Clear STAR delivery</div>
        </div>
        <div className="glass-card p-6 flex flex-col items-center text-center gap-2">
          <div className="text-zinc-500 text-xs font-bold uppercase">Technical Depth</div>
          <div className="text-3xl font-bold text-cyan-400">85%</div>
          <div className="text-xs text-zinc-500 mt-2">Solid code patterns</div>
        </div>
        <div className="glass-card p-6 flex flex-col items-center text-center gap-2">
          <div className="text-zinc-500 text-xs font-bold uppercase">Problem Solving</div>
          <div className="text-3xl font-bold text-emerald-400">90%</div>
          <div className="text-xs text-zinc-500 mt-2">Correct complexity</div>
        </div>
        <div className="glass-card p-6 flex flex-col items-center text-center gap-2">
          <div className="text-zinc-500 text-xs font-bold uppercase">Confidence</div>
          <div className="text-3xl font-bold text-amber-400">80%</div>
          <div className="text-xs text-zinc-500 mt-2">Slight pacing rush</div>
        </div>
        <div className="glass-card p-6 flex flex-col items-center text-center gap-2">
          <div className="text-zinc-500 text-xs font-bold uppercase">Leadership</div>
          <div className="text-3xl font-bold text-blue-400">85%</div>
          <div className="text-xs text-zinc-500 mt-2">Clear scope ownership</div>
        </div>
      </div>

      {/* Strengths / Weaknesses Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="glass-card p-8">
          <h3 className="text-xl font-bold flex items-center gap-2 text-emerald-400 mb-6">
            <CheckCircle2 className="w-5 h-5" /> Key Strengths
          </h3>
          <ul className="flex flex-col gap-4 text-sm text-zinc-300">
            <li className="flex gap-2">
              <span className="text-emerald-500">✓</span> Provided clean, well-reasoned explanations for database concurrency issues.
            </li>
            <li className="flex gap-2">
              <span className="text-emerald-500">✓</span> Strong use of the STAR method to structure backend architecture examples.
            </li>
          </ul>
        </div>

        <div className="glass-card p-8">
          <h3 className="text-xl font-bold flex items-center gap-2 text-rose-400 mb-6">
            <AlertTriangle className="w-5 h-5" /> Areas to Improve
          </h3>
          <ul className="flex flex-col gap-4 text-sm text-zinc-300">
            <li className="flex gap-2">
              <span className="text-rose-500">✗</span> Frequency of filler words increased under follow-up questioning.
            </li>
            <li className="flex gap-2">
              <span className="text-rose-500">✗</span> Speed of explanation was slightly fast, exceeding 140 wpm temporarily.
            </li>
          </ul>
        </div>
      </div>

      {/* 90-Day Improvement Plan Schedule */}
      <div className="glass-card p-8">
        <h3 className="text-xl font-bold flex items-center gap-2 mb-6">
          <BookOpen className="w-5 h-5 text-violet-500" /> Customized 90-Day Learning Plan
        </h3>
        <div className="border-l-2 border-zinc-800 ml-4 pl-6 flex flex-col gap-8">
          <div className="relative">
            <div className="absolute -left-[31px] top-1.5 w-4 h-4 rounded-full bg-violet-600 border-4 border-zinc-950" />
            <div className="text-xs text-zinc-500 font-bold">WEEK 1-2</div>
            <div className="font-bold text-sm mt-1">Refining Pace and Pauses</div>
            <p className="text-zinc-400 text-xs mt-1">Practice deliberate pause pacing to eliminate filler words.</p>
          </div>
          <div className="relative">
            <div className="absolute -left-[31px] top-1.5 w-4 h-4 rounded-full bg-zinc-700 border-4 border-zinc-950" />
            <div className="text-xs text-zinc-500 font-bold">WEEK 3-4</div>
            <div className="font-bold text-sm mt-1">System Design Paradigms</div>
            <p className="text-zinc-400 text-xs mt-1">Study database partitioning algorithms and horizontal scaling rules.</p>
          </div>
        </div>
      </div>

      {/* Exit CTAs */}
      <div className="flex gap-4">
        <Link href="/dashboard" className="px-6 py-3 rounded-lg border border-zinc-800 hover:bg-zinc-900 text-sm font-semibold">
          Back to Dashboard
        </Link>
        <Link href="/interview/new" className="px-6 py-3 rounded-lg bg-violet-600 hover:bg-violet-500 text-sm font-semibold text-white flex items-center gap-2">
          Start Next Session <ArrowRight className="w-4 h-4" />
        </Link>
      </div>
    </div>
  );
}
