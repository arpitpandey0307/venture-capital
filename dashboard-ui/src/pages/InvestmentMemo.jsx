import React from 'react';

const metrics = [
  { metric: 'Customer Acquisition Cost (CAC)', nexus: '$1,250', avg: '$4,500' },
  { metric: 'LTV:CAC Ratio', nexus: '8.5x', avg: '3.2x' },
  { metric: 'Net Dollar Retention (NDR)', nexus: '142%', avg: '115%' },
  { metric: 'Gross Margin', nexus: '88%', avg: '72%' },
  { metric: 'Sales Cycle Length', nexus: '45 Days', avg: '120 Days' },
];

export default function InvestmentMemo() {
  return (
    <>
      <header className="flex justify-between items-start mb-8">
        <h2 className="text-4xl font-black tracking-tighter text-white neon-text-primary">Investment Committee Memo</h2>
        <button className="glass-panel text-white px-5 py-2.5 rounded-xl text-sm font-bold hover:bg-white/5 transition-colors flex items-center gap-2 border border-surface-border">
          <span className="material-symbols-outlined text-[20px]">download</span> Export PDF
        </button>
      </header>

      <div className="glass-panel rounded-[2rem] p-8 md:p-14 max-w-4xl mx-auto shadow-2xl">
        {/* Document Header */}
        <div className="flex items-center gap-6 pb-8 border-b border-surface-border mb-10">
          <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-primary/80 to-blue-700 flex items-center justify-center text-white font-black text-2xl shadow-[0_0_15px_rgba(0,229,255,0.3)] border border-primary/20">N</div>
          <div>
            <h1 className="text-3xl font-black text-white tracking-tight">Nexus AI <span className="text-slate-500 font-medium">— Series A</span></h1>
            <div className="flex items-center gap-4 text-sm font-medium text-slate-400 mt-3">
              <span className="flex items-center gap-1.5 bg-surface border border-surface-border px-3 py-1.5 rounded-lg"><span className="material-symbols-outlined text-[16px] text-primary">calendar_today</span> Mar 15, 2026</span>
              <span className="flex items-center gap-1.5 bg-surface border border-surface-border px-3 py-1.5 rounded-lg"><span className="material-symbols-outlined text-[16px] text-secondary">person</span> Alex Mercer</span>
            </div>
          </div>
          <span className="ml-auto px-4 py-2 rounded-lg text-xs font-black uppercase tracking-widest text-amber-400 border border-amber-400/30 bg-amber-400/10 shadow-[0_0_10px_rgba(251,191,36,0.1)]">Draft Status</span>
        </div>

        {/* Content */}
        <div className="space-y-12">
          <section>
            <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-3">
              <div className="bg-primary/10 border border-primary/30 p-2 rounded-xl text-primary flex shadow-[0_0_10px_rgba(0,229,255,0.1)]"><span className="material-symbols-outlined text-[20px]">shield</span></div> 
              Market Defensibility
            </h3>
            <p className="text-base leading-relaxed text-slate-300 font-medium">
              Nexus Project operates in a highly fragmented market with significant barriers to entry established by their proprietary data ingestion pipeline. Unlike legacy competitors relying on manual API integrations, Nexus has engineered a zero-touch abstraction layer that autonomously maps disparate financial schemas.
            </p>
          </section>

          <section>
            <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-3">
              <div className="bg-secondary/10 border border-secondary/30 p-2 rounded-xl text-secondary flex shadow-[0_0_10px_rgba(180,0,255,0.1)]"><span className="material-symbols-outlined text-[20px]">trending_up</span></div> 
              Opportunity & Traction
            </h3>
            <p className="text-base leading-relaxed text-slate-300 font-medium mb-8">
              The TAM for automated reconciliation infrastructure is estimated at $12B, growing at 24% CAGR. Nexus secured 14 enterprise logos in the last two quarters. Their land-and-expand motion yields 150% contract expansion within 12 months.
            </p>
            <div className="glass-panel border-l-[4px] border-l-primary rounded-r-2xl p-6 relative overflow-hidden">
              <div className="absolute inset-0 bg-primary/5 pointer-events-none"></div>
              <h4 className="text-base font-bold text-white mb-2 relative z-10">Algorithm Thesis</h4>
              <p className="text-sm text-slate-400 leading-relaxed font-medium relative z-10">
                Core conviction rests on Nexus's proprietary ML models achieving 99.9% accuracy in anomaly detection vs. 94% industry standard. This technical moat fundamentally shifts unit economics for clients.
              </p>
            </div>
          </section>

          <section>
            <h3 className="text-xl font-bold text-white mb-5 flex items-center gap-3">
              <div className="bg-emerald-500/10 border border-emerald-500/30 p-2 rounded-xl text-emerald-400 flex shadow-[0_0_10px_rgba(16,185,129,0.1)]"><span className="material-symbols-outlined text-[20px]">analytics</span></div> 
              Quantitative Due Diligence
            </h3>
            <div className="border border-surface-border rounded-2xl overflow-hidden bg-surface/30">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b border-surface-border bg-surface/50">
                    <th className="px-6 py-5 text-xs font-bold text-slate-400 uppercase tracking-wider">Metric</th>
                    <th className="px-6 py-5 text-xs font-bold text-primary uppercase tracking-wider">Nexus Performance</th>
                    <th className="px-6 py-5 text-xs font-bold text-slate-500 uppercase tracking-wider">Industry Average</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-surface-border/50">
                  {metrics.map((r, i) => (
                    <tr key={i} className="hover:bg-white/5 transition-colors">
                      <td className="px-6 py-5 text-slate-200 font-bold text-sm">{r.metric}</td>
                      <td className="px-6 py-5 text-primary font-black text-lg neon-text-primary">{r.nexus}</td>
                      <td className="px-6 py-5 text-slate-500 font-medium text-sm">{r.avg}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        </div>
      </div>
    </>
  );
}
