import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Venture Alpha | VC Analytics",
    page_icon="🔭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
def inject_custom_css():
    st.markdown("""
    <style>
        /* Hide Streamlit default components */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Global Typography & Colors */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #E2E8F0;
        }
        
        /* App Background */
        .stApp {
            background-color: #0B0F19;
        }

        /* Metric Cards */
        div[data-testid="stMetric"] {
            background-color: #111827;
            border: 1px solid #1F2937;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
            transition: all 0.3s ease;
        }
        div[data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            border-color: #3B82F6;
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.15);
        }
        
        /* Headers */
        h1 {
            font-weight: 700 !important;
            letter-spacing: -0.04em !important;
            color: #F8FAFC !important;
            margin-bottom: 0.5rem !important;
        }
        h2 {
            font-weight: 600 !important;
            letter-spacing: -0.03em !important;
            color: #F1F5F9 !important;
        }
        h3 {
            font-weight: 600 !important;
            color: #E2E8F0 !important;
            font-size: 1.1rem !important;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* Badges */
        .badge {
            display: inline-block;
            padding: 0.25em 0.75em;
            font-size: 0.75rem;
            font-weight: 600;
            border-radius: 9999px;
            margin-right: 0.5rem;
            background-color: rgba(59, 130, 246, 0.1);
            color: #60A5FA;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        .badge.green { background-color: rgba(16, 185, 129, 0.1); color: #34D399; border-color: rgba(16, 185, 129, 0.2); }
        .badge.purple { background-color: rgba(168, 85, 247, 0.1); color: #C084FC; border-color: rgba(168, 85, 247, 0.2); }
        .badge.orange { background-color: rgba(249, 115, 22, 0.1); color: #FB923C; border-color: rgba(249, 115, 22, 0.2); }

        /* Customizing tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
            background-color: transparent;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: transparent !important;
            padding-bottom: 12px;
            padding-top: 12px;
            color: #94A3B8;
        }
        .stTabs [aria-selected="true"] {
            color: #3B82F6 !important;
            border-bottom: 2px solid #3B82F6 !important;
        }
        
        /* Buttons */
        div.stButton > button {
            background-color: #1E293B;
            color: #F8FAFC;
            border: 1px solid #334155;
            border-radius: 8px;
            font-weight: 500;
            padding: 0.5rem 1rem;
            transition: all 0.2s ease;
        }
        div.stButton > button:hover {
            background-color: #3B82F6;
            border-color: #3B82F6;
            color: white;
            transform: translateY(-1px);
        }

        /* Expanders */
        .streamlit-expanderHeader {
            background-color: #111827 !important;
            border-color: #1F2937 !important;
            border-radius: 8px !important;
        }
        .streamlit-expanderContent {
            border-color: #1F2937 !important;
            background-color: #0F172A !important;
        }
        
        hr {
            border-color: #1F2937 !important;
            margin: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# --- SIDEBAR & NAVIGATION ---
with st.sidebar:
    st.markdown("""
        <div style='text-align: left; padding: 20px 0 30px 0;'>
            <h2 style='margin:0; font-weight: 800; color: #F8FAFC; display:flex; align-items:center; letter-spacing: -0.5px;'>
                <span style='color: #3B82F6; margin-right:10px; font-size: 1.5rem;'>▲</span> Venture Alpha
            </h2>
            <p style='margin:5px 0 0 32px; font-size: 0.75rem; color: #64748B; font-weight: 600; letter-spacing: 1px;'>SCOUT PLATFORM v3.0</p>
        </div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["Dashboard Overview", "Emerging Technologies", "Investment Memo", "Founder Interview", "Data Engine"],
        icons=["pie-chart", "rocket", "file-text", "mic", "database"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "transparent",
                "border": "none"
            },
            "icon": {
                "color": "#94A3B8", 
                "font-size": "1.1rem"
            }, 
            "nav-link": {
                "font-size": "0.95rem", 
                "font-weight": "500",
                "color": "#94A3B8",
                "text-align": "left", 
                "margin": "4px 0", 
                "padding": "12px 16px",
                "border-radius": "8px",
                "transition": "all 0.2s ease"
            },
            "nav-link-selected": {
                "background-color": "#2563EB", 
                "color": "#F8FAFC",
                "font-weight": "600",
                "box-shadow": "0 4px 6px -1px rgba(37, 99, 235, 0.2)"
            }
        }
    )
    
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    
    # User Profile Mockup
    st.markdown("""
        <div style='display:flex; align-items:center; background-color:#111827; padding:16px; border-radius:12px; border:1px solid #1F2937; margin-bottom: 20px; transition: all 0.3s ease; cursor: pointer;' onmouseover='this.style.borderColor="#3B82F6"; this.style.transform="translateY(-2px)";' onmouseout='this.style.borderColor="#1F2937"; this.style.transform="none";'>
            <div style='width:36px; height:36px; border-radius:8px; background: linear-gradient(135deg, #3B82F6, #1D4ED8); color:white; display:flex; align-items:center; justify-content:center; font-weight:700; font-size: 0.9rem; margin-right:12px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);'>GP</div>
            <div>
                <div style='font-size:0.9rem; font-weight:600; color:#F1F5F9; line-height: 1.2;'>General Partner</div>
                <div style='font-size:0.75rem; color:#64748B; margin-top: 2px;'>Fund IV • Analyst Area</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='display: flex; align-items: center; justify-content: center; padding: 10px; background-color: rgba(16, 185, 129, 0.05); border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.1);'>
            <div style='width: 8px; height: 8px; background-color: #10B981; border-radius: 50%; margin-right: 8px; box-shadow: 0 0 8px #10B981;'></div>
            <span style='font-size: 0.75rem; color: #10B981; font-weight: 600; letter-spacing: 0.5px;'>LIVE DATA SYNCING</span>
        </div>
    """, unsafe_allow_html=True)

# Clean selection string
route = selected

# --- MAIN ROUTING ---
if route == "Dashboard Overview":
    
    # Header Area
    col_txt, col_btn = st.columns([4, 1])
    with col_txt:
        st.markdown("<h1>Platform Intelligence</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #94A3B8; font-size: 1.1rem; margin-top:-10px;'>Real-time signal aggregation across developer ecosystems and open-source networks.</p>", unsafe_allow_html=True)
    with col_btn:
        st.write("")
        st.button("⚙️ Generate PDF Report", use_container_width=True)

    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    # Key Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Signals Analyzed (30d)", "1.24M", "+12.4% MoM")
    m2.metric("Projects Scanned", "34,280", "+5.2% MoM")
    m3.metric("Breakout Tech Detected", "24", "4 New This Week")
    m4.metric("Platform Avg Conviction", "78.4", "+4.2 MoM")

    # Layout for Charts
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.markdown("### Top Sectors Signal Velocity")
        st.markdown("<div style='background-color: #111827; padding: 20px; border-radius: 12px; border: 1px solid #1F2937;'>", unsafe_allow_html=True)
        if PLOTLY_AVAILABLE:
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            df_chart = pd.DataFrame({
                "Month": months,
                "AI Agents": [120, 150, 200, 310, 480, 750, 1100, 1500, 2100, 3200, 4800, 7500],
                "ZK Proofs": [80, 95, 120, 180, 220, 350, 500, 700, 1200, 1800, 2500, 3800],
                "Bio-Compute": [200, 250, 300, 320, 350, 380, 400, 420, 430, 450, 460, 480]
            })
            fig = px.area(df_chart, x="Month", y=["AI Agents", "ZK Proofs", "Bio-Compute"], 
                          color_discrete_sequence=["#3B82F6", "#8B5CF6", "#10B981"],
                          template="plotly_dark")
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=0, r=0, t=10, b=0),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title=""),
                xaxis=dict(showgrid=False, color="#94A3B8"),
                yaxis=dict(showgrid=True, gridcolor="#1F2937", color="#94A3B8")
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.bar_chart(pd.DataFrame({"AI Agents": [120, 310, 750, 1500, 3200, 7500]}, index=["Jan", "Apr", "Jun", "Aug", "Oct", "Dec"]))
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c2:
        st.markdown("### Momentum Heatmap")
        st.markdown("<div style='background-color: #111827; padding: 20px; border-radius: 12px; border: 1px solid #1F2937; height: 100%;'>", unsafe_allow_html=True)
        
        # Recent activity feed simulation
        st.markdown("""
            <div style='margin-bottom:15px; padding-bottom:15px; border-bottom:1px solid #1F2937;'>
                <span class='badge'>AI</span> <span class='badge purple'>Frameworks</span><br>
                <div style='margin-top:8px; font-weight:600;'>AutoGPT cross-repo surge</div>
                <div style='color:#64748B; font-size:0.8rem;'>+4,500 mentions in last 24h</div>
            </div>
            
            <div style='margin-bottom:15px; padding-bottom:15px; border-bottom:1px solid #1F2937;'>
                <span class='badge green'>Web3</span> <span class='badge orange'>DePIN</span><br>
                <div style='margin-top:8px; font-weight:600;'>Decentralized GPU Net Growth</div>
                <div style='color:#64748B; font-size:0.8rem;'>Reddit sentiment highly positive</div>
            </div>
            
            <div style='margin-bottom:15px; padding-bottom:15px;'>
                <span class='badge'>DevTools</span> <span class='badge'>WASM</span><br>
                <div style='margin-top:8px; font-weight:600;'>Rust compiled runtimes</div>
                <div style='color:#64748B; font-size:0.8rem;'>Major fork activity detected</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.button("View Live Feed", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif route == "Emerging Technologies":
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Deal Flow & Pipeline")
        st.markdown("High-conviction OSS projects exhibiting massive breakout potential.")
    with col2:
        st.write("")
        st.selectbox("Filter Layer", ["All Stages", "Early Signal", "High Conviction", "Due Diligence"], label_visibility="collapsed")
    
    st.write("---")

    tech_tabs = st.tabs(["🔥 Hot Deals", "🔍 Deep Diligence", "📉 Fading Signals"])
    
    with tech_tabs[0]:
        techs = [
            {"name": "Agentic Protocol", "category": "AI Infrastructure", "score": 93, "growth": "+450%", "val_est": "Seed / $15M", "status": "Hot"},
            {"name": "ZK-Rollup VM", "category": "Web3 Scaling", "score": 88, "growth": "+210%", "val_est": "Series A / $80M", "status": "Stable"},
            {"name": "WASM Cloud Edge", "category": "Cloud Infrastructure", "score": 84, "growth": "+125%", "val_est": "Seed / $20M", "status": "Rising"}
        ]

        # Datatable layout mockup
        st.markdown("""
        <div style="display:grid; grid-template-columns: 3fr 2fr 1.5fr 1.5fr 1fr; padding: 10px 15px; color:#94A3B8; font-size:0.8rem; font-weight:600; text-transform:uppercase; border-bottom:1px solid #1F2937; margin-bottom:10px;">
            <div>Project entity</div>
            <div>Conviction Score</div>
            <div>GitHub Growth</div>
            <div>Est. Round</div>
            <div>Action</div>
        </div>
        """, unsafe_allow_html=True)

        for i, tech in enumerate(techs):
            with st.container():
                cols = st.columns([3, 2, 1.5, 1.5, 1.3])
                
                with cols[0]:
                    st.markdown(f"**{tech['name']}** <span class='badge' style='margin-left:5px;'>{tech['status']}</span><br><span style='font-size:0.8rem; color:#94A3B8;'>{tech['category']}</span>", unsafe_allow_html=True)
                
                with cols[1]:
                    st.progress(tech['score']/100)
                    st.markdown(f"<div style='font-size:0.8rem; text-align:right; margin-top:-5px;'>{tech['score']} / 100</div>", unsafe_allow_html=True)
                
                with cols[2]:
                    color = "#10B981" if "+" in tech['growth'] else "#EF4444"
                    st.markdown(f"<div style='color:{color}; font-weight:600; padding-top:5px;'>{tech['growth']}</div>", unsafe_allow_html=True)
                    
                with cols[3]:
                    st.markdown(f"<div style='padding-top:5px;'>{tech['val_est']}</div>", unsafe_allow_html=True)
                    
                with cols[4]:
                    st.button("Analyze", key=f"btn_{i}", use_container_width=True)
                    
                st.markdown("<hr style='margin: 10px 0;'/>", unsafe_allow_html=True)
                
        # Expanded detail view dynamically placed
        with st.expander("Deep Dive: Agentic Protocol (Target 1)", expanded=True):
            st.markdown("### Technical Nuance & Developer Capture")
            
            c_left, c_right = st.columns([2, 1])
            with c_left:
                st.write("This protocol solves the fundamental multi-agent state management problem. By utilizing a custom vector-distributed database specifically built for agent memory sharing, they have achieved a 10x latency reduction compared to standard RAG implementations.")
                st.markdown("**Core Tech Stack:** `Rust`, `gRPC`, `Torch`, `RocksDB`")
                
                if PLOTLY_AVAILABLE:
                    df = pd.DataFrame({"Week": ["W1","W2","W3","W4","W5"], "Forks": [10, 25, 60, 150, 420], "Stars": [100, 300, 1200, 4000, 11000]})
                    fig2 = px.bar(df, x="Week", y=["Forks", "Stars"], barmode="group", template="plotly_dark", color_discrete_sequence=["#F59E0B", "#FCD34D"])
                    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=250, margin=dict(t=10, b=0, l=0, r=0))
                    st.plotly_chart(fig2, use_container_width=True)

            with c_right:
                st.markdown("<div style='background-color:#1E293B; padding:20px; border-radius:8px;'>", unsafe_allow_html=True)
                st.markdown("#### System Signals")
                st.metric("HackerNews Rank", "#1", "Maintained 14 hours")
                st.metric("KOL Mentions", "12", "E.g. Karpathy, Ng")
                st.metric("Enterprise Adoption", "3 pilots", "Fortune 500 tech")
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.link_button("View GitHub Repo ↗", "https://github.com", type="primary", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

elif route == "Investment Memo":
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Investment Committee Memo")
        st.markdown("**Subject:** Project 'Nexus' (AI Agent OS) | **Target Yield:** 15x")
    with col2:
        st.write("")
        st.button("Export to Word", use_container_width=True)
        
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #111827; padding: 40px; border-radius: 12px; border: 1px solid #1F2937; max-width: 900px; margin: 0 auto; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);'>
        <div style='display:flex; justify-content:space-between; margin-bottom: 20px;'>
            <div style='font-size:0.9rem; color:#94A3B8;'><span class='badge'>DRAFT</span> Date: March 15, 2026</div>
            <div style='font-size:0.9rem; color:#94A3B8;'>Author: Automated Core Algorithm v3</div>
        </div>
        
        <h2 style='color:#3B82F6 !important; border-bottom: 1px solid #1F2937; padding-bottom:10px;'>1. Market Defensibility & Problem</h2>
        <p style='color:#E2E8F0; line-height: 1.7;'>The market for LLM deployment is shifting rapidly from raw model endpoints to localized autonomous agents. However, developers lack the equivalent of an operating system to manage file I/O, parallel API tool execution, and episodic memory persistence. Project Nexus provides an elegant, compiler-level approach to agent execution.</p>
        
        <h2 style='color:#3B82F6 !important; border-bottom: 1px solid #1F2937; padding-bottom:10px; margin-top:30px;'>2. Opportunity & Traction</h2>
        <p style='color:#E2E8F0; line-height: 1.7;'>Unlike competitors who offer hosted Python frameworks, Nexus is written natively in Rust as a runtime layer. Based on our signal analysis over 14 days, the project went from zero to 15,000 GitHub stars, indicating product-market-fit among backend engineers.</p>
        
        <div style='background-color:#0F172A; padding:20px; border-radius:8px; border-left:4px solid #10B981; margin: 20px 0;'>
            <strong>Algorithm Thesis:</strong> High conviction due to anomalous repository cloning behaviors (indicating active enterprise code base integration rather than just casual starring).
        </div>
        
        <h2 style='color:#3B82F6 !important; border-bottom: 1px solid #1F2937; padding-bottom:10px; margin-top:30px;'>3. Quantitative Signal Diligence</h2>
        <table style='width:100%; border-collapse: collapse; margin-top:10px; color:#E2E8F0;'>
            <tr style='border-bottom: 1px solid #334155; text-align:left;'>
                <th style='padding:10px 0;'>Metric</th>
                <th style='padding:10px 0;'>Nexus Project</th>
                <th style='padding:10px 0;'>Industry Avg</th>
            </tr>
            <tr style='border-bottom: 1px solid #1E293B;'>
                <td style='padding:10px 0;'>Weekly Issues Closed</td>
                <td style='color:#10B981; font-weight:bold;'>245</td>
                <td>45</td>
            </tr>
            <tr style='border-bottom: 1px solid #1E293B;'>
                <td style='padding:10px 0;'>Unique Contributors</td>
                <td style='color:#10B981; font-weight:bold;'>85</td>
                <td>12</td>
            </tr>
            <tr>
                <td style='padding:10px 0;'>Reddit Sentiment</td>
                <td style='color:#10B981; font-weight:bold;'>94% Pos</td>
                <td>65% Pos</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

elif route == "Founder Interview":
    st.title("Virtual Diligence Room")
    st.markdown("Simulated LLM-powered preliminary founding team interview based on extracted documentation and code commit messages.")
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='display:flex; justify-content:center; align-items:center; margin-bottom:40px;'>
            <div style='background-color:#1E293B; padding:10px 20px; border-radius:20px; font-size:0.8rem; color:#94A3B8; border:1px solid #334155;'>
                🔴 Session connected • Recording Active • Protocol Nexus
            </div>
        </div>
    """, unsafe_allow_html=True)

    # VC Question
    with st.chat_message("user", avatar="👔"):
        st.markdown("**Analyst GP:** Can you walk me through why you chose to build the underlying architecture in Rust rather than following the standard Python/LangChain approach?")
        
    # Founder Answer
    with st.chat_message("assistant", avatar="⚡"):
        st.markdown("**Nexus Founder:** Absolutely. When we scaled our own internal agents, we noticed that Python's GIL and memory overhead completely bottlenecked parallel agent execution. If you have 5,000 agents traversing the web and hitting rate limits, you need rigorous thread control and minimal latency. Rust gives us C++ level control but with memory safety protocols that allow open-source contributors to commit scaling modules without breaking the core runtime.")
        
    # VC Question
    with st.chat_message("user", avatar="👔"):
        st.markdown("**Analyst GP:** That makes sense. Your GitHub metrics are incredible for a 3-week-old project. What is the commercialization strategy once the framework becomes the default open-source standard?")
        
    # Founder Answer
    with st.chat_message("assistant", avatar="⚡"):
        st.markdown("**Nexus Founder:** We view the open-source CLI and local runtime as a loss leader to capture developer mindshare. Our enterprise offering, built on top of this, provides SOC2-compliant managed agent memory, identity/authorization access controls for agents hitting private APIs, and fleet monitoring dashboards. Companies will pay for the enterprise governance layer.")

elif route == "Data Engine":
    st.title("Signal Processing Pipeline")
    st.markdown("Live view of data ingestion models and algorithm health.")
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("API Calls / Min", "4,502", "Stable", delta_color="normal")
    col2.metric("Latency", "42ms", "-12ms", delta_color="inverse")
    col3.metric("Models Active", "5", "BERT, RoBERTa, Llama-3")
    
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("### Active Ingestion Streams")
        st.markdown("""
        <div style='background-color:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937;'>
            <div style='display:flex; justify-content:space-between; margin-bottom:15px; align-items:center;'>
                <div style='display:flex; align-items:center;'><span style='color:#3B82F6; font-size:1.5rem; margin-right:10px;'>🐙</span> GitHub Firehose v4</div>
                <span class='badge green'>Syncing</span>
            </div>
            <div style='display:flex; justify-content:space-between; margin-bottom:15px; align-items:center;'>
                <div style='display:flex; align-items:center;'><span style='color:#F59E0B; font-size:1.5rem; margin-right:10px;'>👾</span> Reddit Sentiment NLP</div>
                <span class='badge green'>Syncing</span>
            </div>
            <div style='display:flex; justify-content:space-between; margin-bottom:15px; align-items:center;'>
                <div style='display:flex; align-items:center;'><span style='color:#38BDF8; font-size:1.5rem; margin-right:10px;'>🐦</span> Twitter/X KOL Graph</div>
                <span class='badge orange'>Rate Limited</span>
            </div>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div style='display:flex; align-items:center;'><span style='color:#EF4444; font-size:1.5rem; margin-right:10px;'>📰</span> HackerNews Real-Time</div>
                <span class='badge green'>Syncing</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("### System Architecture")
        st.markdown("""
        <div style='background-color:#111827; padding:20px; border-radius:12px; border:1px solid #1F2937; height:240px; display:flex; justify-content:center; align-items:center; color:#64748B; font-family:monospace; font-size:0.85rem; line-height: 1.8;'>
            <div style="text-align: center;">
            [ Data Sources ] &rarr; [ Kafka Queue ] &rarr; [ Spark Streaming ]<br><br>
            [ Spark Streaming ] &rarr; [ Feature Store ] &rarr; [ Inference ]<br><br>
            [ Model Inference ] &rarr; [ Postgres DB ] &rarr; [ Dashboard ]
            </div>
        </div>
        """, unsafe_allow_html=True)
