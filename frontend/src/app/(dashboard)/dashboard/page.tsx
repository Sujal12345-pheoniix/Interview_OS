"use client";

import React from "react";
import Link from "next/link";
import { PlusCircle, Trophy, BarChart3, TrendingUp, Mic } from "lucide-react";

export default function DashboardHome() {
  return (
    <div className="flex flex-col gap-10">
      {/* Banner */}
      <div className="glass-card p-8 bg-gradient-to-r from-violet-900/20 via-zinc-900/50 to-transparent flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight mb-2">Welcome Back, Candidate!</h1>
          <p className="text-zinc-400">Ready to boost your interview success rate? Start a new session now.</p>
        </div>
        <Link href="/interview/new" className="px-6 py-3.5 rounded-xl font-bold bg-violet-600 hover:bg-violet-500 shadow-lg shadow-violet-500/20 flex items-center gap-2 transition-all">
          <PlusCircle className="w-5 h-5" /> Start New Interview
        </Link>
      </div>

      {/* Analytics Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="glass-card p-6 flex flex-col gap-3">
          <div className="text-sm font-semibold text-zinc-500">Readiness Score</div>
          <div className="text-3xl font-black text-violet-400">85%</div>
          <div className="text-xs text-emerald-500 flex items-center gap-1">
            <TrendingUp className="w-3.5 h-3.5" /> +2.3% this week
          </div>
        </div>

        <div className="glass-card p-6 flex flex-col gap-3">
          <div className="text-sm font-semibold text-zinc-500">Interviews Conducted</div>
          <div className="text-3xl font-black text-cyan-400">4</div>
          <div className="text-xs text-zinc-500">Targeting FAANG</div>
        </div>

        <div className="glass-card p-6 flex flex-col gap-3">
          <div className="text-sm font-semibold text-zinc-500">Filler Words Avg</div>
          <div className="text-3xl font-black text-emerald-400">2.1 <span className="text-xs font-normal text-zinc-500">/min</span></div>
          <div className="text-xs text-emerald-500 flex items-center gap-1">
            <TrendingUp className="w-3.5 h-3.5" /> Improving trend
          </div>
        </div>

        <div className="glass-card p-6 flex flex-col gap-3">
          <div className="text-sm font-semibold text-zinc-500">Pacing Pace</div>
          <div className="text-3xl font-black text-amber-400">125 <span className="text-xs font-normal text-zinc-500">wpm</span></div>
          <div className="text-xs text-zinc-500">Conversational range</div>
        </div>
      </div>

      {/* Historical List */}
      <div className="glass-card p-8">
        <h2 className="text-xl font-extrabold tracking-tight mb-6">Recent Sessions</h2>
        <div className="flex flex-col gap-4">
          <div className="p-4 border border-zinc-800 rounded-xl bg-zinc-900/20 flex justify-between items-center">
            <div>
              <div className="font-bold flex items-center gap-2">
                FastAPI Backend Design <span className="text-xs px-2 py-0.5 rounded bg-violet-500/10 text-violet-400">FAANG</span>
              </div>
              <div className="text-xs text-zinc-500">Software Engineering (Backend) • June 16, 2026</div>
            </div>
            <Link href="/interview/mock-session-id/report" className="px-4 py-2 rounded-lg border border-zinc-800 bg-zinc-900/50 hover:bg-zinc-800 text-sm font-semibold text-zinc-400 hover:text-white transition-all">
              View Report
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
