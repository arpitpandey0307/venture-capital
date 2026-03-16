# Venture Alpha Dashboard Architecture

This document provides a comprehensive overview of the frontend architecture, the technologies used, and the current structure of the Venture Alpha dashboard project.

## 1. Evolution from Streamlit to React
The project originally began as a Python-based **Streamlit** application (`app.py`). While Streamlit is excellent for rapid data prototyping, it lacks the layout flexibility, animation support, and deep styling capabilities required for an ultra-premium, highly customized user interface.

To achieve the desired "cyberpunk bento-box" aesthetic, the frontend was completely rebuilt using a modern JavaScript stack. **The `app.py` file is now considered deprecated for UI purposes**, though its underlying data processing logic could be repurposed later to build a backend API.

## 2. Technology Stack
The new frontend is isolated within the `dashboard-ui/` directory and is built using:
*   **Vite**: A lightning-fast frontend build tool and development server.
*   **React**: A component-based UI library for building modular interfaces.
*   **Tailwind CSS (v4)**: A utility-first CSS framework used for all styling. We utilize Tailwind's new `@theme` configuration within `index.css` to define custom design tokens.
*   **React Router (`react-router-dom`)**: Used for client-side navigation between different dashboard views without reloading the browser.
*   **Google Fonts & Icons**: Using the **"Inter"** font for crisp typography and **"Material Symbols Outlined"** for scalable, modern iconography.

## 3. Directory Structure
The React application follows a clean, component-driven structure:

```text
dashboard-ui/
├── index.html              # Main HTML entry point
├── package.json            # Dependencies and scripts (use `npm run dev`)
├── postcss.config.js       # PostCSS config required for Tailwind v4
└── src/
    ├── main.jsx            # React app initialization
    ├── App.jsx             # Root layout and Router configuration
    ├── index.css           # Global styles, Tailwind imports, and custom utility classes
    ├── components/
    │   └── Sidebar.jsx     # The floating "Island" top navigation bar
    └── pages/
        ├── Dashboard.jsx      # Home: Bento grid with conviction metrics and intelligence feed
        ├── EmergingTech.jsx   # Deal Flow: Filterable matrix of potential investments
        ├── InvestmentMemo.jsx # Memos: Clean, readable analysis documents with glassmorphism
        ├── FounderInterview.jsx # Interviews: LLM-simulated chat interface
        └── DataEngine.jsx     # Engine: Pipeline architecture diagrams and API health stats
```

## 4. UI/UX Design System (The "Bento Box" Dark Theme)
The current design employs a highly unique, futuristic aesthetic:
*   **Layout**: A masonry "Bento Box" grid (`grid-cols-12` in Tailwind) that tightly packs information cards of varying sizes.
*   **Navigation**: A floating, pill-shaped top navigation bar, completely removing the traditional side-panel.
*   **Glassmorphism**: Cards use a custom `.glass-panel` CSS class (defined in `index.css`) featuring heavy backdrop blur (`blur(12px)`), semi-transparent backgrounds (`rgba(255, 255, 255, 0.04)`), and subtle borders.
*   **Color Palette**: 
    *   **Background**: Deep space radial gradient (`#0F1219` to `#05050A`).
    *   **Accents**: Neon Cyan (`#00E5FF`) and Cyber Purple (`#B400FF`).
*   **Typography**: Massive, heavy-weight numbers combined with a `.neon-text-primary` custom CSS class for glowing text effects.

## 5. API and Data Integration (Current State)
**Status: The frontend currently uses static, hardcoded dummy data for demonstration purposes.** 

There is currently no active backend database or API connected. To make this dashboard fully functional, the following steps are required:
1.  **Develop a Backend API**: Build a backend service (e.g., using Python with FastAPI/Flask or Node.js with Express). The data generation logic from the old `app.py` can be moved here.
2.  **Data Fetching**: Use `fetch`, `axios`, or a library like `React Query` inside the React components (typically within `useEffect` hooks) to request real deal flow data, active signals, and intelligence feeds from the API.
3.  **State Management**: Replace the hardcoded arrays (e.g., `const deals = [...]`) with React state (`useState`) to dynamically render the charts, tables, and AI interview simulations based on the API responses.
