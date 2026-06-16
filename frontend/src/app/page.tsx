"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { Brain, Mic, Trophy, FileText, Zap, Shield, ChevronRight } from "lucide-react";

export default function Home() {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.1, delayChildren: 0.2 }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: "easeOut" as const } }
  };

  return (
    <div className="min-h-screen bg-[#09090b] text-white overflow-hidden relative selection:bg-violet-500 selection:text-white">
      {/* Background Mesh Orbs */}
      <div className="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] rounded-full bg-violet-600/10 blur-[120px] pointer-events-none" />
      <div className="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] rounded-full bg-cyan-600/10 blur-[120px] pointer-events-none" />

      {/* Header / Nav */}
      <header className="fixed top-0 w-full z-50 glass-header py-4 px-6 md:px-12 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <Brain className="w-8 h-8 text-violet-500 animate-pulse" />
          <span className="text-xl font-bold tracking-tight bg-gradient-to-r from-white to-zinc-400 bg-clip-text text-transparent">InterviewOS</span>
        </div>
        <nav className="hidden md:flex items-center gap-8 text-sm text-zinc-400">
          <a href="#features" className="hover:text-white transition-colors">Features</a>
          <a href="#pricing" className="hover:text-white transition-colors">Pricing</a>
          <a href="#metrics" className="hover:text-white transition-colors">Impact</a>
        </nav>
        <div className="flex items-center gap-4">
          <Link href="/dashboard" className="px-5 py-2 rounded-lg text-sm font-semibold border border-zinc-800 bg-zinc-900/50 hover:bg-zinc-800 transition-all">
            Enter Dashboard
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-6 md:px-12 max-w-7xl mx-auto flex flex-col items-center text-center relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, ease: "easeOut" }}
          className="max-w-4xl"
        >
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-violet-500/30 bg-violet-950/20 text-xs font-semibold text-violet-400 mb-6">
            <Zap className="w-3.5 h-3.5" /> Introducing Next-Gen Mock Interviews
          </div>
          <h1 className="text-display-lg md:text-display-xl lg:text-display-2xl font-extrabold tracking-tight mb-6 leading-tight">
            Land Your Dream Job With{" "}
            <span className="bg-gradient-to-r from-violet-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent">
              InterviewOS
            </span>
          </h1>
          <p className="text-zinc-400 text-lg md:text-xl max-w-2xl mx-auto mb-10">
            Diagnose weaknesses, customize multi-agent learning roadmaps, and simulate voice-based FAANG preparation loops with instant analytical diagnostics.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/dashboard" className="px-8 py-4 rounded-xl text-base font-semibold bg-gradient-to-r from-violet-600 to-purple-700 hover:from-violet-500 hover:to-purple-600 text-white shadow-lg shadow-violet-500/25 flex items-center justify-center gap-2 group transition-all transform hover:-translate-y-0.5">
              Start Free Session <ChevronRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </Link>
          </div>
        </motion.div>
      </section>

      {/* Features Grid */}
      <section id="features" className="py-20 px-6 md:px-12 max-w-7xl mx-auto relative z-10">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Engineered to Perfect Every Aspect</h2>
          <p className="text-zinc-400 max-w-xl mx-auto">Equipped with specialized AI agents focusing on distinct components of your success.</p>
        </div>

        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          className="grid grid-cols-1 md:grid-cols-3 gap-8"
        >
          <motion.div variants={itemVariants} className="glass-card p-8 flex flex-col gap-4">
            <div className="w-12 h-12 rounded-xl bg-violet-500/10 flex items-center justify-center text-violet-500">
              <Mic className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-bold">Real-time Voice AI</h3>
            <p className="text-zinc-400 text-sm">Ultra-low latency mock interviews with Deepgram STT and Cartesia speech response synthesis.</p>
          </motion.div>

          <motion.div variants={itemVariants} className="glass-card p-8 flex flex-col gap-4">
            <div className="w-12 h-12 rounded-xl bg-cyan-500/10 flex items-center justify-center text-cyan-500">
              <FileText className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-bold">Resume & JD Analysis</h3>
            <p className="text-zinc-400 text-sm">Upload context and target job requirements to auto-calibrate custom difficulty curves.</p>
          </motion.div>

          <motion.div variants={itemVariants} className="glass-card p-8 flex flex-col gap-4">
            <div className="w-12 h-12 rounded-xl bg-emerald-500/10 flex items-center justify-center text-emerald-500">
              <Trophy className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-bold">Evaluation Metrics</h3>
            <p className="text-zinc-400 text-sm">STAR method performance charts, filler words counters, pacing tracking, and 90-day learning schedules.</p>
          </motion.div>
        </motion.div>
      </section>

      {/* Footer */}
      <footer className="border-t border-zinc-900 py-12 px-6 md:px-12 text-center text-sm text-zinc-500">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-2">
            <Brain className="w-6 h-6 text-violet-500" />
            <span className="font-bold text-white">InterviewOS</span>
          </div>
          <div>© 2026 InterviewOS. Built for elite preparation workflows.</div>
        </div>
      </footer>
    </div>
  );
}
