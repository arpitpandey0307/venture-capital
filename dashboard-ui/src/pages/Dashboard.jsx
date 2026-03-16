import React from 'react';

const deals = [
  { name: 'Nexus Protocol', cat: 'DeFi', score: '92.4', init: 'N', grad: 'from-indigo-500 to-purple-600', status: 'Evaluating', dotColor: 'bg-primary shadow-[0_0_5px_#00E5FF]' },
  { name: 'Aura Network', cat: 'Infrastructure', score: '88.1', init: 'A', grad: 'from-emerald-500 to-teal-600', status: 'Due Diligence', dotColor: 'bg-secondary shadow-[0_0_5px_#B400FF]' },
  { name: 'Zero Knowledge Labs', cat: 'ZK Tech', score: '85.7', init: 'Z', grad: 'from-orange-500 to-red-600', status: 'Sourcing', dotColor: 'bg-slate-500' },
];

const feed = [
  { title: 'Project Nebula Upgrade', desc: 'High frequency trading signals detected associated with upcoming mainnet launch.', time: '2m ago', tag: 'High Confidence', tagClass: 'text-primary bg-primary/10', dot: 'bg-primary' },
  { title: 'Key Developer Movement', desc: 'Three core contributors from Protocol X have begun contributing to a new stealth repository.', time: '15m ago', tag: 'Medium Confidence', tagClass: 'text-secondary bg-secondary/10', dot: 'bg-secondary' },
  { title: 'Liquidity Migration Alert', desc: 'Significant TVL shift observed from L1 bridging contracts towards emerging L2 networks.', time: '1h ago', tag: 'Observation', tagClass: 'text-slate-300 bg-slate-700/50', dot: 'bg-slate-500' },
  { title: 'Governance Proposal Spike', desc: 'Unusual voter participation rate detected on Cosmos ecosystem key proposals.', time: '3h ago', tag: 'High Confidence', tagClass: 'text-primary bg-primary/10', dot: 'bg-primary' },
];

export default function Dashboard() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-12 gap-6 auto-rows-auto">
      
      {/* Hero Chart (Wide) */}
      <div className="glass-panel rounded-[1.5rem] p-6 lg:col-span-8 flex flex-col gap-4 relative overflow-hidden group">
        <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent pointer-events-none"></div>
        <div className="flex justify-between items-start z-10">
          <div>
            <p className="text-text-muted text-sm font-medium mb-1 uppercase tracking-wider">Platform Conviction</p>
            <div className="flex items-end gap-3">
              <h2 className="text-white text-5xl sm:text-6xl font-black tracking-tighter neon-text-primary">88.4</h2>
              <span className="text-primary text-sm font-bold mb-2 flex items-center">
                <span className="material-symbols-outlined text-[16px] mr-1">arrow_upward</span> 4.2%
              </span>
            </div>
          </div>
          <div className="flex gap-2">
            <span className="px-2.5 py-1 rounded-md bg-primary/10 text-primary text-xs font-bold border border-primary/20 backdrop-blur">Real-time</span>
          </div>
        </div>
        
        <div className="flex-1 min-h-[220px] mt-2 relative z-10">
          <div className="absolute bottom-0 w-full h-full flex items-end">
            <svg className="w-full h-full" preserveAspectRatio="none" viewBox="0 0 100 100">
              <defs>
                <linearGradient id="chartGradient" x1="0" x2="0" y1="0" y2="1">
                  <stop offset="0%" stopColor="#00E5FF" stopOpacity="0.3" />
                  <stop offset="100%" stopColor="#00E5FF" stopOpacity="0.0" />
                </linearGradient>
              </defs>
              <path d="M0,100 L0,60 C10,55 20,70 30,65 C40,60 50,45 60,50 C70,55 80,30 90,35 C95,37 98,20 100,25 L100,100 Z" fill="url(#chartGradient)" />
              <path d="M0,60 C10,55 20,70 30,65 C40,60 50,45 60,50 C70,55 80,30 90,35 C95,37 98,20 100,25" fill="none" stroke="#00E5FF" strokeWidth="2" vectorEffect="non-scaling-stroke" />
              <circle cx="30" cy="65" fill="#00E5FF" r="1.5" />
              <circle cx="60" cy="50" fill="#00E5FF" r="1.5" />
              <circle cx="90" cy="35" fill="#00E5FF" r="1.5" />
              <circle cx="100" cy="25" fill="#fff" filter="drop-shadow(0 0 4px #00E5FF)" r="2" />
            </svg>
          </div>
        </div>
      </div>

      {/* Metric Square 1 */}
      <div className="glass-panel rounded-[1.5rem] p-6 lg:col-span-2 flex flex-col justify-between">
        <div>
          <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center mb-6 border border-primary/20 text-primary shadow-[0_0_15px_rgba(0,229,255,0.1)]">
            <span className="material-symbols-outlined text-[24px]">radar</span>
          </div>
          <p className="text-text-muted text-sm font-medium mb-1">Active Signals</p>
          <h3 className="text-white text-3xl font-black tracking-tight">3,402</h3>
        </div>
        <div className="mt-6 flex items-center justify-between">
          <span className="text-primary text-sm font-bold bg-primary/10 px-2 py-0.5 rounded border border-primary/20">+12%</span>
          <span className="text-slate-500 text-xs font-medium">vs last week</span>
        </div>
      </div>

      {/* Metric Square 2 */}
      <div className="glass-panel rounded-[1.5rem] p-6 lg:col-span-2 flex flex-col justify-between">
        <div>
          <div className="w-12 h-12 rounded-xl bg-secondary/10 flex items-center justify-center mb-6 border border-secondary/20 text-secondary shadow-[0_0_15px_rgba(180,0,255,0.1)]">
            <span className="material-symbols-outlined text-[24px]">speed</span>
          </div>
          <p className="text-text-muted text-sm font-medium mb-1">Weekly Velocity</p>
          <h3 className="text-white text-3xl font-black tracking-tight neon-text-secondary">128.5</h3>
        </div>
        <div className="mt-6 flex items-center justify-between">
          <span className="text-secondary text-sm font-bold bg-secondary/10 px-2 py-0.5 rounded border border-secondary/20">+8.4%</span>
          <span className="text-slate-500 text-xs font-medium">vs last week</span>
        </div>
      </div>

      {/* Top Deals (Medium Rectangular) */}
      <div className="glass-panel rounded-[1.5rem] p-0 lg:col-span-8 flex flex-col overflow-hidden">
        <div className="p-6 border-b border-surface-border flex justify-between items-center bg-white/5">
          <h3 className="text-white text-lg font-bold">Top Deals Radar</h3>
          <button className="text-primary text-sm hover:text-white transition-colors font-medium">View All</button>
        </div>
        <div className="flex-1 px-2 py-2">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="text-text-muted text-[11px] uppercase tracking-wider font-bold">
                <th className="p-4">Project</th>
                <th className="p-4">Category</th>
                <th className="p-4">Conviction</th>
                <th className="p-4">Status</th>
              </tr>
            </thead>
            <tbody className="text-sm">
              {deals.map((d, i) => (
                <tr key={i} className={`hover:bg-white/5 transition-colors group ${i !== deals.length - 1 ? 'border-b border-surface-border/50' : ''}`}>
                  <td className="p-4">
                    <div className="flex items-center gap-4">
                      <div className={`w-10 h-10 rounded-xl bg-gradient-to-br ${d.grad} flex items-center justify-center font-black text-white text-sm shadow-lg`}>
                        {d.init}
                      </div>
                      <span className="text-slate-200 font-bold group-hover:text-white transition-colors">{d.name}</span>
                    </div>
                  </td>
                  <td className="p-4">
                    <span className="px-2.5 py-1.5 rounded-lg bg-surface border border-surface-border text-xs font-bold text-slate-300">{d.cat}</span>
                  </td>
                  <td className="p-4 text-slate-300 font-bold">{d.score}</td>
                  <td className="p-4">
                    <div className="flex items-center gap-2">
                      <span className={`w-2 h-2 rounded-full ${d.dotColor}`}></span>
                      <span className="text-slate-300 text-xs font-bold">{d.status}</span>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Intelligence Feed (Tall Vertical) */}
      <div className="glass-panel rounded-[1.5rem] lg:col-span-4 lg:row-span-2 flex flex-col h-full max-h-[500px] overflow-hidden">
        <div className="p-6 border-b border-surface-border flex items-center gap-3 bg-white/5">
          <span className="material-symbols-outlined text-primary text-[24px] neon-text-primary">bolt</span>
          <h3 className="text-white text-lg font-bold tracking-tight">Intelligence Feed</h3>
        </div>
        <div className="flex-1 overflow-y-auto p-4 custom-scrollbar">
          <div className="flex flex-col gap-2">
            {feed.map((f, i) => (
              <div key={i} className="p-4 hover:bg-white/5 rounded-xl transition-colors cursor-pointer group border border-transparent hover:border-surface-border/50">
                <div className="flex justify-between items-start mb-2">
                  <span className={`text-[10px] font-bold uppercase tracking-widest px-2 py-1 rounded-md border border-white/5 ${f.tagClass}`}>{f.tag}</span>
                  <span className="text-slate-500 text-xs font-medium">{f.time}</span>
                </div>
                <h4 className="text-slate-200 text-sm font-bold mb-2 group-hover:text-white transition-colors">{f.title}</h4>
                <div className="flex items-start gap-3">
                  <span className={`w-1.5 h-1.5 rounded-full mt-1.5 shrink-0 shadow-lg ${f.dot}`}></span>
                  <p className="text-slate-400 text-xs leading-relaxed font-medium">{f.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      
    </div>
  );
}
