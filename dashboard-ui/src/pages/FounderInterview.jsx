import React from 'react';

const conversation = [
  { role: 'analyst', name: 'Alex Mercer', label: 'Venture Alpha', text: 'Can you walk me through why you chose to build the underlying architecture in Rust rather than following the standard Python/LangChain approach?' },
  { role: 'founder', name: 'Sarah Chen', label: 'Nexus AI CEO', text: "When we scaled our own internal agents, Python's GIL and memory overhead completely bottlenecked parallel agent execution. Rust gives us C++ level control but with memory safety protocols that allow open-source contributors to commit scaling modules without breaking the core runtime." },
  { role: 'analyst', name: 'Alex Mercer', label: 'Venture Alpha', text: "Your GitHub metrics are incredible for a 3-week-old project. What is the commercialization strategy once the framework becomes the default open-source standard?" },
  { role: 'founder', name: 'Sarah Chen', label: 'Nexus AI CEO', text: "We view the open-source CLI and local runtime as a loss leader to capture developer mindshare. Our enterprise offering provides SOC2-compliant managed agent memory, identity/authorization access controls, and fleet monitoring dashboards. Companies will pay for the enterprise governance layer." },
];

export default function FounderInterview() {
  return (
    <>
      <header className="mb-10 text-center flex flex-col items-center">
        <h2 className="text-4xl font-black tracking-tighter text-white mb-3 neon-text-primary">Simulated Diligence Interview</h2>
        <p className="text-slate-400 font-medium">LLM-powered interview generated from extracted documentation and commits.</p>
        
        <div className="inline-flex items-center gap-3 glass-panel border border-primary/30 shadow-[0_0_15px_rgba(0,229,255,0.1)] px-5 py-2 mt-6 rounded-full text-sm font-bold text-white">
          <span className="relative flex h-3 w-3">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
            <span className="relative inline-flex rounded-full h-3 w-3 bg-primary"></span>
          </span>
          Session Active • Nexus AI Founders
        </div>
      </header>

      <div className="flex flex-col gap-6 max-w-3xl mx-auto glass-panel p-8 md:p-10 rounded-[2rem]">
        {conversation.map((msg, i) => (
          <div key={i} className={`flex gap-5 ${msg.role === 'founder' ? 'flex-row-reverse' : ''}`}>
             <div className={`w-12 h-12 rounded-xl border flex items-center justify-center text-sm font-black shrink-0 shadow-lg ${
              msg.role === 'analyst' ? 'bg-surface border-surface-border text-slate-400' : 'bg-gradient-to-br from-primary/80 to-blue-600 border-primary/30 text-white shadow-[0_0_15px_rgba(0,229,255,0.2)]'
            }`}>
              {msg.role === 'analyst' ? 'AM' : 'SC'}
            </div>
            
            <div className={`flex justify-col w-full max-w-[80%] ${msg.role === 'founder' ? 'items-end' : 'items-start'}`}>
              <div className={`mb-2 flex items-baseline gap-2 px-1 ${msg.role === 'founder' ? 'flex-row-reverse' : ''}`}>
                <span className="text-sm font-bold text-white">{msg.name}</span>
                <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500">{msg.label}</span>
              </div>
              <div className={`px-6 py-4 text-[15px] font-medium leading-relaxed border backdrop-blur-md ${
                msg.role === 'founder' 
                  ? 'bg-primary/10 border-primary/30 text-white rounded-[1.5rem] rounded-tr-md shadow-[0_4px_20px_rgba(0,229,255,0.05)]' 
                  : 'bg-surface border-surface-border text-slate-300 rounded-[1.5rem] rounded-tl-md'
              }`}>
                {msg.text}
              </div>
            </div>
          </div>
        ))}
        
        {/* Input area */}
        <div className="mt-8 bg-panel-dark border border-surface-border rounded-2xl p-2 pl-5 flex items-center gap-4 shadow-inner focus-within:border-primary/50 transition-all">
          <span className="material-symbols-outlined text-slate-500 text-[24px]">terminal</span>
          <input 
            className="flex-1 bg-transparent text-base text-white placeholder-slate-600 font-medium outline-none h-12" 
            placeholder="Type your query into the terminal..." 
            disabled 
          />
          <button className="bg-primary px-6 py-3 rounded-xl text-bg-dark font-black hover:bg-primary/90 transition-colors shadow-[0_0_10px_rgba(0,229,255,0.3)]">
            Execute
          </button>
        </div>
      </div>
    </>
  );
}
