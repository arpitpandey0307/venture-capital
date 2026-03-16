import React, { useState } from 'react';

const deals = [
  { name: 'Nexus AI', category: 'LLM Infrastructure', score: 92, growth: '+240%', round: 'Seed', val: '$15M', status: 'High Signal', init: 'N', grad: 'from-primary/80 to-blue-600' },
  { name: 'Quantix', category: 'DeFi Options', score: 88, growth: '+110%', round: 'Series A', val: '$40M', status: null, init: 'Q', grad: 'from-secondary/80 to-purple-800' },
  { name: 'AeroMotive', category: 'Aerospace', score: 84, growth: '+300%', round: 'Pre-Seed', val: '$8M', status: 'Diligence', init: 'A', grad: 'from-emerald-400 to-teal-700' },
  { name: 'BioSync', category: 'Health Tech', score: 79, growth: '+65%', round: 'Seed', val: '$12M', status: null, init: 'B', grad: 'from-rose-500 to-pink-700' },
  { name: 'Vera Node', category: 'Web3 Infra', score: 75, growth: '+180%', round: 'Seed', val: '$10M', status: 'Tracking', init: 'V', grad: 'from-amber-500 to-orange-700' },
];

export default function EmergingTech() {
  const [activeTab, setActiveTab] = useState('hot');

  return (
    <>
      <header className="flex justify-between items-start mb-6">
        <div>
          <h2 className="text-4xl font-black tracking-tighter text-white mb-2 neon-text-primary">Deal Flow Matrix</h2>
          <p className="text-text-muted font-medium">Track emerging technologies and active signals.</p>
        </div>
        <div className="flex gap-4">
          <button className="glass-panel px-5 py-2.5 rounded-xl text-sm text-slate-300 hover:text-white transition-colors font-bold flex items-center gap-2">
            <span className="material-symbols-outlined text-[18px]">filter_list</span> Filter
          </button>
          <button className="bg-primary hover:bg-primary/90 shadow-[0_0_15px_rgba(0,229,255,0.4)] text-bg-dark px-6 py-2.5 rounded-xl text-sm transition-all font-black flex items-center gap-2">
            <span className="material-symbols-outlined text-[18px]">add</span> Add Deal
          </button>
        </div>
      </header>

      {/* Tabs */}
      <div className="border-b border-surface-border mt-8 mb-6">
        <nav className="flex gap-8">
          {['hot', 'diligence', 'tracking'].map((tab) => (
            <button key={tab} onClick={() => setActiveTab(tab)}
              className={`pb-4 text-sm font-bold border-b-2 transition-all capitalize ${
                activeTab === tab ? 'border-primary text-primary neon-text-primary' : 'border-transparent text-slate-400 hover:text-white hover:border-surface-border'
              }`}>
              {tab === 'hot' ? 'Hot Deals' : tab === 'diligence' ? 'In Diligence' : 'Tracking'}
            </button>
          ))}
        </nav>
      </div>

      {/* Table Area */}
      <div className="glass-panel rounded-[1.5rem] overflow-hidden">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-surface/50 border-b border-surface-border">
              {['Project', 'Conviction', 'Growth', 'Round', 'Action'].map((th, i) => (
                <th key={th} className={`px-6 py-5 text-xs font-bold text-text-muted uppercase tracking-wider ${i === 4 ? 'text-right' : ''}`}>{th}</th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-surface-border/50">
            {deals.map((d, i) => (
              <tr key={i} className="hover:bg-white/5 transition-colors group">
                <td className="px-6 py-5 whitespace-nowrap">
                  <div className="flex items-center gap-5">
                    <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${d.grad} flex items-center justify-center text-white font-black text-lg shadow-[0_0_10px_rgba(255,255,255,0.1)] group-hover:scale-105 transition-transform border border-white/10`}>{d.init}</div>
                    <div className="flex flex-col">
                      <div className="flex items-center gap-3">
                        <span className="text-base font-bold text-slate-200 group-hover:text-white transition-colors">{d.name}</span>
                        {d.status && <span className={`px-2.5 py-1 rounded-md text-[10px] font-black tracking-widest uppercase border ${
                          d.status === 'High Signal' ? 'bg-primary/10 text-primary border-primary/30 shadow-[0_0_5px_rgba(0,229,255,0.2)]' : 
                          d.status === 'Diligence' ? 'bg-secondary/10 text-secondary border-secondary/30' : 
                          'bg-surface text-slate-400 border-surface-border'
                        }`}>{d.status}</span>}
                      </div>
                      <span className="text-sm font-medium text-slate-500 mt-1">{d.category}</span>
                    </div>
                  </div>
                </td>
                <td className="px-6 py-5 whitespace-nowrap">
                  <div className="flex items-center gap-4">
                    <span className="text-base font-black text-white w-6">{d.score}</span>
                    <div className="w-24 h-1.5 bg-surface border border-surface-border rounded-full overflow-hidden">
                      <div className="h-full bg-primary rounded-full transition-all duration-500 shadow-[0_0_8px_#00E5FF]" style={{ width: `${d.score}%` }} />
                    </div>
                  </div>
                </td>
                <td className="px-6 py-5 whitespace-nowrap">
                  <span className="inline-flex items-center gap-1.5 text-primary border border-primary/20 bg-primary/10 px-3 py-1.5 rounded-lg text-sm font-bold shadow-sm">
                    <span className="material-symbols-outlined text-[16px]">trending_up</span>{d.growth}
                  </span>
                </td>
                <td className="px-6 py-5 whitespace-nowrap">
                  <div className="text-base font-bold text-slate-200">{d.round}</div>
                  <div className="text-xs font-medium text-slate-500 mt-1">{d.val}</div>
                </td>
                <td className="px-6 py-5 whitespace-nowrap text-right">
                  <button className="p-2 rounded-xl text-slate-400 hover:text-primary hover:bg-primary/10 transition-colors border border-transparent hover:border-primary/20">
                    <span className="material-symbols-outlined text-[22px]">arrow_forward</span>
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}
