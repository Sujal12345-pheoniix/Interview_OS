"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Brain, LayoutDashboard, PlusCircle, History, BarChart3, Settings } from "lucide-react";

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();

  const menuItems = [
    { label: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
    { label: "New Session", href: "/interview/new", icon: PlusCircle },
    { label: "History", href: "/interview/history", icon: History },
    { label: "Progress", href: "/progress", icon: BarChart3 },
  ];

  return (
    <div className="min-h-screen bg-[#09090b] text-white flex flex-col md:flex-row">
      {/* Sidebar Navigation */}
      <aside className="w-full md:w-64 border-r border-zinc-800 bg-[#0f0f12] flex flex-col p-6 shrink-0 gap-6">
        <div className="flex items-center gap-2 mb-4">
          <img src="/favicon.png" alt="Brain Logo" className="w-8 h-8 object-contain" />
          <span className="text-xl font-bold tracking-tight">InterviewOS</span>
        </div>

        <nav className="flex flex-col gap-2 flex-grow">
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href;
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all ${
                  isActive
                    ? "bg-violet-600 text-white shadow-lg shadow-violet-500/20"
                    : "text-zinc-400 hover:text-white hover:bg-zinc-800/40"
                }`}
              >
                <Icon className="w-5 h-5" />
                {item.label}
              </Link>
            );
          })}
        </nav>

        <div className="pt-6 border-t border-zinc-800 flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-violet-600/20 border border-violet-500/30 flex items-center justify-center font-bold text-violet-400">
            C
          </div>
          <div>
            <div className="text-sm font-bold">Candidate</div>
            <div className="text-xs text-zinc-500">Free Tier</div>
          </div>
        </div>
      </aside>

      {/* Workspace Area */}
      <main className="flex-1 p-6 md:p-12 overflow-y-auto max-w-7xl mx-auto w-full">
        {children}
      </main>
    </div>
  );
}
