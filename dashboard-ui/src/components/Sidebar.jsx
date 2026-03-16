import React from 'react';
import { NavLink } from 'react-router-dom';

const navItems = [
  { label: 'Dashboard', path: '/' },
  { label: 'Deal Flow', path: '/emerging' },
  { label: 'Memos', path: '/memo' },
  { label: 'Interviews', path: '/interview' },
  { label: 'Engine', path: '/engine' },
];

export default function Sidebar() {
  // We're repurposing the "Sidebar" component into a Floating Top Nav Island
  return (
    <div className="fixed top-6 left-1/2 -translate-x-1/2 w-[95%] max-w-5xl z-50">
      <nav className="glass-panel rounded-full px-4 sm:px-6 py-3 flex items-center justify-between shadow-[0_10px_40px_rgba(0,0,0,0.5)]">
        
        {/* Logo */}
        <div className="flex items-center gap-3">
          <span className="material-symbols-outlined text-primary text-2xl" style={{ textShadow: '0 0 8px rgba(0,229,255,0.6)' }}>hexagon</span>
          <h1 className="text-white text-lg font-bold tracking-tight hidden sm:block">Venture Alpha</h1>
        </div>

        {/* Navigation Links */}
        <div className="hidden md:flex items-center gap-8">
          {navItems.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              end={item.path === '/'}
              className={({ isActive }) =>
                `text-sm font-medium transition-colors ${
                  isActive ? 'text-primary neon-text-primary' : 'text-text-muted hover:text-white'
                }`
              }
            >
              {item.label}
            </NavLink>
          ))}
        </div>

        {/* Right Actions */}
        <div className="flex items-center gap-4">
          <button className="text-text-muted hover:text-primary transition-colors flex items-center justify-center">
            <span className="material-symbols-outlined text-[20px]">search</span>
          </button>
          <button className="text-text-muted hover:text-primary transition-colors flex items-center justify-center relative">
            <span className="material-symbols-outlined text-[20px]">notifications</span>
            <span className="absolute -top-1 -right-1 w-2 h-2 bg-secondary rounded-full shadow-[0_0_8px_#B400FF]"></span>
          </button>
          <button className="w-8 h-8 rounded-full bg-surface border border-surface-border flex items-center justify-center text-primary overflow-hidden ml-2 hover:bg-surface-border transition-colors">
            <span className="material-symbols-outlined text-[18px]">person</span>
          </button>
        </div>

      </nav>
    </div>
  );
}
