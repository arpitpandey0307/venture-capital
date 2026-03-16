import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar'; // This is now our Floating Top Nav
import Dashboard from './pages/Dashboard';
import EmergingTech from './pages/EmergingTech';
import InvestmentMemo from './pages/InvestmentMemo';
import FounderInterview from './pages/FounderInterview';
import DataEngine from './pages/DataEngine';

export default function App() {
  return (
    <Router>
      <div className="min-h-screen text-text-main font-display antialiased selection:bg-primary/30 selection:text-white">
        {/* Floating Top Nav */}
        <Sidebar />
        
        {/* Main Content Container (with top padding for the floating nav) */}
        <main className="pt-28 pb-12 px-6 max-w-[1400px] mx-auto min-h-screen">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/emerging" element={<EmergingTech />} />
            <Route path="/memo" element={<InvestmentMemo />} />
            <Route path="/interview" element={<FounderInterview />} />
            <Route path="/engine" element={<DataEngine />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}
