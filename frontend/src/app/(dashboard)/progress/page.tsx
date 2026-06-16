"use client";

import React from "react";
import { TrendingUp, BarChart3, Target } from "lucide-react";

export default function ProgressPage() {
  return (
    <div className="flex flex-col gap-10">
      <div>
        <h1 className="text-3xl font-extrabold tracking-tight mb-2">Progress & Analytics</h1>
        <p className="text-zinc-400">Track your mock performance over time across target domains.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="glass-card p-6 flex flex-col gap-4">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-zinc-500">Skill Velocity</span>
            <TrendingUp className="w-5 h-5 text-violet-500" />
          </div>
          <div className="text-4xl font-black text-violet-400">4.5 <span className="text-xs font-normal text-zinc-500">pts/wk</span></div>
          <p className="text-xs text-zinc-500">Speed of improvement across mock attempts.</p>
        </div>

        <div className="glass-card p-6 flex flex-col gap-4">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-zinc-500">Current Readiness</span>
            <Target className="w-5 h-5 text-cyan-500" />
          </div>
          <div className="text-4xl font-black text-cyan-400">88%</div>
          <p className="text-xs text-zinc-500">Estimated capability score compared to FAANG entry standards.</p>
        </div>

        <div className="glass-card p-6 flex flex-col gap-4">
          <div className="flex justify-between items-center">
            <span className="text-sm font-semibold text-zinc-500">Filler Words Trend</span>
            <BarChart3 className="w-5 h-5 text-emerald-500" />
          </div>
          <div className="text-4xl font-black text-emerald-400">-18%</div>
          <p className="text-xs text-zinc-500">Reduction in filler phrase counts.</p>
        </div>
      </div>

      <div className="glass-card p-8">
        <h3 className="text-xl font-bold mb-6">Historical Readiness Timeline</h3>
        <div className="h-[250px] w-full flex items-end gap-6 border-b border-zinc-800 pb-4">
          <div className="flex-1 flex flex-col items-center gap-2">
            <div className="w-full bg-violet-600/30 border border-violet-500/30 rounded-t-lg h-[60%]" />
            <span className="text-xs text-zinc-500">Session 1</span>
          </div>
          <div className="flex-1 flex flex-col items-center gap-2">
            <div className="w-full bg-violet-600/50 border border-violet-500/50 rounded-t-lg h-[75%]" />
            <span className="text-xs text-zinc-500">Session 2</span>
          </div>
          <div className="flex-1 flex flex-col items-center gap-2">
            <div className="w-full bg-violet-600 border border-violet-500 rounded-t-lg h-[88%]" />
            <span className="text-xs text-zinc-500">Session 3</span>
          </div>
        </div>
      </div>
    </div>
  );
}
