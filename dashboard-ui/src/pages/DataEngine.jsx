import React from 'react';

const streams = [
  { name: 'GitHub Firehose v4', status: 'Syncing', ok: true },
  { name: 'Reddit Sentiment NLP', status: 'Syncing', ok: true },
  { name: 'Twitter/X KOL Graph', status: 'Rate Limited', ok: false },
  { name: 'HackerNews Real-Time', status: 'Syncing', ok: true },
];

const stats = [
  { icon: 'speed', label: 'API Calls / Min', value: '4,502', status: 'Stable', color: 'text-primary bg-primary/10 border-primary/20 shadow-[0_0_15px_rgba(0,229,255,0.1)]' },
  { icon: 'timer', label: 'Latency', value: '42ms', status: '-12ms ↓', color: 'text-secondary bg-secondary/10 border-secondary/20 shadow-[0_0_15px_rgba(180,0,255,0.1)]' },
  { icon: 'model_training', label: 'Models Active', value: '5', status: 'BERT, RoBERTa', color: 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20 shadow-[0_0_15px_rgba(16,185,129,0.1)]' },
];

export default function DataEngine() {
  return (
    <>
      <header className="mb-8">
        <h2 className="text-4xl font-black tracking-tighter text-white mb-2 neon-text-primary">Signal Pipeline</h2>
        <p className="text-slate-400 font-medium">Real-time health of data ingestion and inference models.</p>
      </header>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {stats.map((s, i) => (
          <div key={i} className="glass-panel rounded-[1.5rem] p-8 flex flex-col gap-5 items-center text-center">
             <div className={`p-4 rounded-xl border ${s.color}`}>
              <span className="material-symbols-outlined text-[32px]">{s.icon}</span>
            </div>
            <div>
              <p className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">{s.label}</p>
              <p className="text-5xl font-black text-white tracking-tight mb-2">{s.value}</p>
              <p className="text-sm font-bold text-slate-400">{s.status}</p>
            </div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6">
        {/* Streams */}
        <div className="glass-panel rounded-[1.5rem] overflow-hidden">
          <div className="px-8 py-6 border-b border-surface-border bg-surface/30">
            <h3 className="text-lg font-bold text-white">Active Ingestion Streams</h3>
          </div>
          <div className="divide-y divide-surface-border/50 p-2">
            {streams.map((s, i) => (
              <div key={i} className="flex items-center justify-between p-6 hover:bg-white/5 rounded-xl transition-colors">
                <div className="flex items-center gap-4">
                  <div className={`w-3 h-3 rounded-full ${s.ok ? 'bg-primary shadow-[0_0_8px_#00E5FF]' : 'bg-red-500 shadow-[0_0_8px_#EF4444] animate-pulse'}`} />
                  <span className="text-base font-bold text-slate-200">{s.name}</span>
                </div>
                <span className={`px-3 py-1.5 border rounded-lg text-[10px] font-black uppercase tracking-widest ${
                  s.ok ? 'bg-primary/10 text-primary border-primary/30' : 'bg-red-500/10 text-red-500 border-red-500/30'
                }`}>{s.status}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Architecture */}
        <div className="glass-panel rounded-[1.5rem] flex flex-col overflow-hidden">
          <div className="px-8 py-6 border-b border-surface-border bg-surface/30">
            <h3 className="text-lg font-bold text-white">System Architecture</h3>
          </div>
          <div className="flex-1 flex items-center justify-center p-10 bg-panel-dark/50 m-2 rounded-2xl border border-dashed border-surface-border relative overflow-hidden">
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(0,229,255,0.05)_0,transparent_100%)]"></div>
            <div className="flex flex-col gap-8 text-sm font-mono items-center relative z-10">
              <div className="flex items-center gap-6">
                <span className="px-5 py-3 glass-panel border border-surface-border rounded-xl text-slate-300 font-bold">Sources</span>
                <span className="material-symbols-outlined text-primary/50">arrow_forward</span>
                <span className="px-5 py-3 glass-panel border border-surface-border rounded-xl text-slate-300 font-bold">Kafka Queue</span>
              </div>
              <span className="material-symbols-outlined text-primary/50 text-[24px]">arrow_downward</span>
              <div className="flex items-center gap-6">
                <span className="px-5 py-3 glass-panel border border-surface-border rounded-xl text-slate-300 font-bold">Features</span>
                <span className="material-symbols-outlined text-primary/50">arrow_forward</span>
                <span className="px-6 py-4 bg-primary/20 border border-primary/50 text-primary rounded-xl font-black shadow-[0_0_20px_rgba(0,229,255,0.2)] relative backdrop-blur-sm">
                  <span className="absolute -top-1.5 -right-1.5 flex h-4 w-4">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-4 w-4 bg-primary border-2 border-bg-dark"></span>
                  </span>
                  Inference
                </span>
                <span className="material-symbols-outlined text-primary/50">arrow_forward</span>
                <span className="px-5 py-3 glass-panel border border-surface-border rounded-xl text-slate-300 font-bold">Dashboard</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
