"""
RecallVantage - Main Application with Navigation
================================================

Unified dashboard with organized navigation structure
"""

import streamlit as st
from datetime import datetime
import sys

# Page configuration
st.set_page_config(
    page_title="RecallVantage - Automotive Recall Intelligence",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# NAVIGATION STRUCTURE
# ============================================================================

def render_top_navigation():
    """Render top navigation bar with dropdown menus"""
    
    # Logo and branding
    col1, col2, col3 = st.columns([1, 4, 1])
    
    with col1:
        try:
            st.image('RecallVantage_Logo_Official.png', width=150)
        except:
            # Fallback if logo not found
            st.markdown("### 🚗 **RecallVantage**")
            st.caption("Automotive Recall Intelligence")
    
    with col3:
        st.markdown(f"**{st.session_state.get('user_name', 'User')}** 👤")
    
    st.markdown("---")
    
    # Main navigation tabs
    tabs = st.tabs([
        "🏠 Home",
        "🚗 Vehicle Analysis", 
        "🎲 Simulation",
        "📊 Portfolio",
        "📚 Resources"
    ])
    
    return tabs


def render_sidebar_navigation():
    """Render sidebar with sub-navigation based on current page"""
    
    st.sidebar.title("Navigation")
    
    # Main page selector
    page = st.sidebar.radio(
        "Main Menu",
        [
            "🏠 Home",
            "🔍 Search & Analyze",
            "📊 Compare Vehicles", 
            "🏭 OEM Overview",
            "📈 Industry Trends",
            "🔔 Watchlist",
            "🎲 Monte Carlo",
            "💰 Price Impact",
            "📈 Portfolio",
            "⚙️ Settings"
        ],
        key="main_nav"
    )
    
    return page


# ============================================================================
# PAGE: HOME
# ============================================================================

def page_home():
    """Home page - Dashboard overview"""
    
    st.title("🏠 Welcome to RecallVantage")
    
    # User greeting
    st.markdown(f"### Hello, {st.session_state.get('user_name', 'Analyst')}!")
    
    # Activity metrics
    st.markdown("---")
    st.subheader("📈 Your Activity This Week")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Vehicles Analyzed", "12", "+3")
    with col2:
        st.metric("Simulations Run", "5", "+2")
    with col3:
        st.metric("STRONG BUY Signals", "2", "+1")
    with col4:
        st.metric("Watchlist Items", "8", "0")
    
    # Quick Actions
    st.markdown("---")
    st.subheader("🎯 Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔍 Analyze New Vehicle", use_container_width=True, type="primary"):
            st.session_state.main_nav = "🔍 Search & Analyze"
            st.rerun()
    
    with col2:
        if st.button("🎲 Run Simulation", use_container_width=True):
            st.session_state.main_nav = "🎲 Monte Carlo"
            st.rerun()
    
    with col3:
        if st.button("📊 View Portfolio", use_container_width=True):
            st.session_state.main_nav = "📈 Portfolio"
            st.rerun()
    
    # Recent Analyses
    st.markdown("---")
    st.subheader("📋 Recent Analyses")
    
    recent_data = [
        {"vehicle": "Tesla Model Y", "stage": 4, "risk": 8.7, "time": "2 hours ago"},
        {"vehicle": "Ford F-150", "stage": 2, "risk": 5.2, "time": "Yesterday"},
        {"vehicle": "Lexus ES", "stage": 0, "risk": 1.8, "time": "3 days ago"},
    ]
    
    for item in recent_data:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
        
        with col1:
            st.markdown(f"**{item['vehicle']}**")
        with col2:
            stage_color = ["🟢", "🟡", "🟡", "🟠", "🔴"][item['stage']]
            st.markdown(f"{stage_color} Stage {item['stage']}")
        with col3:
            st.markdown(f"Risk: {item['risk']}")
        with col4:
            st.markdown(f"*{item['time']}*")
    
    # High-Risk Alerts
    st.markdown("---")
    st.subheader("🔥 High-Risk Alerts")
    
    st.warning("⚠️ **Tesla Model Y**: Drift score increased to 0.95! (+0.02)")
    st.warning("🔥 **Rivian R1T**: Stage upgraded from 2 → 3")
    
    # Industry Overview
    st.markdown("---")
    st.subheader("📊 Industry Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**High-Risk OEMs**")
        st.markdown("1. 🔴 Tesla (7.2/10)")
        st.markdown("2. 🟠 Ford (6.8/10)")
        st.markdown("3. 🟡 GM (6.1/10)")
    
    with col2:
        st.markdown("**Low-Risk OEMs**")
        st.markdown("1. ✅ Lexus (2.1/10)")
        st.markdown("2. ✅ Honda (3.4/10)")
        st.markdown("3. ✅ Mazda (3.8/10)")


# ============================================================================
# PAGE: SEARCH & ANALYZE
# ============================================================================

def page_search_analyze():
    """Single vehicle deep dive analysis"""
    
    st.title("🔍 Search & Analyze")
    
    # Search section
    st.subheader("Search for a Vehicle")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        make = st.selectbox("Make", ["TESLA", "FORD", "LEXUS", "GM", "TOYOTA", "HONDA"])
    with col2:
        # Pre-populate model based on make
        default_models = {
            "TESLA": "MODEL Y",
            "FORD": "F-150",
            "LEXUS": "ES",
            "GM": "SILVERADO",
            "TOYOTA": "CAMRY",
            "HONDA": "ACCORD"
        }
        model = st.text_input("Model", value=default_models.get(make, "MODEL Y"), key="model_search")
    with col3:
        year = st.number_input("Year", 2020, 2025, 2023)
    
    # Quick presets
    st.markdown("**Or select a preset:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔴 Tesla Model Y (High Risk)", use_container_width=True):
            st.session_state.selected_vehicle = "TESLA MODEL Y"
    with col2:
        if st.button("🟡 Ford F-150 (Moderate Risk)", use_container_width=True):
            st.session_state.selected_vehicle = "FORD F-150"
    with col3:
        if st.button("🟢 Lexus ES (Safe)", use_container_width=True):
            st.session_state.selected_vehicle = "LEXUS ES"
    
    # Results section
    if st.button("🔍 Analyze", type="primary"):
        st.markdown("---")
        
        # Risk Profile Card
        st.subheader(f"📊 Risk Profile: {make} {model} {year}")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Overall Risk", "8.7/10", "+0.3")
        with col2:
            st.metric("Stage", "4 (CRITICAL)", "+1")
        with col3:
            st.metric("Drift Score", "0.913", "+0.02")
        with col4:
            st.metric("Total Complaints", "2,843", "+124")
        
        # Key Metrics
        st.markdown("---")
        st.subheader("📈 Key Metrics")
        
        metrics_data = {
            "Drift Score": {"value": 0.913, "interpretation": "Very High - Exponential growth pattern"},
            "Velocity": {"value": "24.5/month", "interpretation": "Rapid complaint acceleration"},
            "Acceleration": {"value": "+3.2/month", "interpretation": "Rising trajectory"},
            "Total Complaints": {"value": "2,843", "interpretation": "Well above critical threshold"}
        }
        
        for metric, data in metrics_data.items():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**{metric}:**")
            with col2:
                st.markdown(f"{data['value']} - *{data['interpretation']}*")
        
        # Trajectory Chart (placeholder)
        st.markdown("---")
        st.subheader("📉 Complaint Trajectory")
        st.info("📊 Interactive chart would appear here (integrate from dashboard_app_v6.py)")
        
        # Recommendation
        st.markdown("---")
        st.subheader("🎯 Recommendation")
        st.error("""
        ### ⚠️ HIGH RECALL RISK
        
        **Action:** Consider shorting TSLA
        
        **Rationale:**
        - Stage 4 classification (imminent recall likely)
        - Drift 0.913 (very high exponential growth)
        - 2,843 complaints (significant volume)
        - Rising trajectory (acceleration +3.2/month)
        
        **Next Steps:**
        - Run Monte Carlo simulation for profit estimate
        - Check live stock price impact
        - Set position size using Kelly Criterion
        """)
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎲 Run Monte Carlo", use_container_width=True, type="primary"):
                st.session_state.main_nav = "🎲 Monte Carlo"
                st.rerun()
        with col2:
            if st.button("🔔 Add to Watchlist", use_container_width=True):
                st.success("✅ Added to watchlist!")
        with col3:
            if st.button("📥 Export Report", use_container_width=True):
                st.info("📄 Report download would trigger here")


# ============================================================================
# PAGE: COMPARE VEHICLES
# ============================================================================

def page_compare_vehicles():
    """Side-by-side vehicle comparison"""
    
    st.title("📊 Compare Vehicles")
    
    st.markdown("Select up to 4 vehicles to compare:")
    
    # Vehicle selectors
    cols = st.columns(4)
    
    vehicles = []
    for i, col in enumerate(cols):
        with col:
            make = st.selectbox(f"Make {i+1}", ["", "TESLA", "FORD", "LEXUS"], key=f"make_{i}")
            if make:
                model = st.text_input(f"Model {i+1}", key=f"model_{i}")
                if model:
                    vehicles.append({"make": make, "model": model})
    
    if len(vehicles) >= 2 and st.button("Compare", type="primary"):
        st.markdown("---")
        st.subheader("Side-by-Side Comparison")
        
        # Comparison table
        comparison_data = {
            "Metric": ["Stage", "Risk Score", "Drift", "Complaints", "Trend"],
            "Tesla Model Y": ["4 🔴", "8.7", "0.913", "2,843", "Rising"],
            "Ford F-150": ["2 🟡", "5.2", "0.58", "485", "Stable"],
            "Lexus ES": ["0 🟢", "1.8", "0.15", "45", "Flat"]
        }
        
        st.table(comparison_data)
        
        st.success("**Winner:** Lexus ES (lowest risk)")
        st.error("**Loser:** Tesla Model Y (highest risk)")


# ============================================================================
# PAGE: OEM OVERVIEW
# ============================================================================

def page_oem_overview():
    """Manufacturer-level risk analysis"""
    
    st.title("🏭 OEM Overview")
    
    manufacturer = st.selectbox(
        "Select Manufacturer",
        ["TESLA", "FORD", "GM", "TOYOTA", "LEXUS", "HONDA"]
    )
    
    if st.button("Analyze OEM", type="primary"):
        st.markdown("---")
        
        st.subheader(f"🏭 {manufacturer} - Manufacturer Overview")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Overall Risk", "7.2/10", "HIGH")
        with col2:
            st.metric("Total Models", "5")
        with col3:
            st.metric("Total Complaints", "8,429")
        with col4:
            st.metric("Trend", "Rising", "↑")
        
        # Model breakdown
        st.markdown("---")
        st.subheader("📊 Model Breakdown")
        
        model_data = {
            "Model": ["Model Y", "Model 3", "Model S", "Model X", "Cybertruck"],
            "Stage": ["4 🔴", "3 🟠", "2 🟡", "3 🟠", "1 🟢"],
            "Risk": [8.7, 7.8, 5.2, 6.9, 3.1],
            "Complaints": [2843, 2134, 1892, 1328, 232],
            "Sales %": ["40%", "35%", "10%", "15%", "<1%"]
        }
        
        st.table(model_data)
        
        # Weighted risk
        st.markdown("---")
        st.subheader("🎯 Weighted Risk (by sales volume)")
        
        st.markdown("""
        - Model Y (40%) × 8.7 = **3.48**
        - Model 3 (35%) × 7.8 = **2.73**
        - Model S (10%) × 5.2 = **0.52**
        - Model X (15%) × 6.9 = **1.04**
        - Cybertruck (<1%) × 3.1 = **0.03**
        
        **Total Weighted Risk: 7.80/10**
        """)
        
        st.warning("⚠️ 55% of sales volume at Stage 3-4 (high risk)")


# ============================================================================
# PAGE: MONTE CARLO SIMULATION
# ============================================================================

def page_monte_carlo():
    """Monte Carlo simulation page"""
    
    st.title("🎲 Monte Carlo Simulation")
    
    st.info("""
    ### What This Does
    
    Runs 10,000 probabilistic scenarios to estimate:
    - Win probability
    - Expected profit/loss  
    - Risk metrics (VaR, CVaR, Sharpe)
    - Optimal position sizing (Kelly Criterion)
    """)
    
    # STEP 1: Vehicle
    st.subheader("STEP 1: Select Vehicle")
    
    col1, col2 = st.columns(2)
    
    with col1:
        make = st.selectbox("Make", ["TESLA", "FORD", "LEXUS"])
    with col2:
        model = st.text_input("Model", "MODEL Y")
    
    # Preload from previous analysis
    if "selected_vehicle" in st.session_state:
        st.success(f"✅ Loaded from analysis: {st.session_state.selected_vehicle}")
    
    # STEP 2: Position
    st.markdown("---")
    st.subheader("STEP 2: Position Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        direction = st.selectbox("Direction", ["Short", "Long"])
    with col2:
        shares = st.number_input("Shares", 0, 1000000, 100000, 10000)
    with col3:
        entry_price = st.number_input("Entry Price ($)", 0.0, 1000.0, 224.50)
    
    # STEP 3: Parameters
    st.markdown("---")
    st.subheader("STEP 3: Simulation Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        iterations = st.selectbox("Iterations", [1000, 5000, 10000, 50000], index=2)
    with col2:
        confidence = st.slider("Confidence Level (%)", 90, 99, 95)
    
    # RUN button
    st.markdown("---")
    
    if st.button("🎲 RUN SIMULATION", type="primary", use_container_width=True):
        
        # Progress bar
        with st.spinner(f"Running {iterations:,} simulations..."):
            import time
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
        
        st.success("✅ Simulation Complete!")
        
        # Results
        st.markdown("---")
        st.subheader("📊 Results Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Win Rate", "95.3%", "✅")
        with col2:
            st.metric("Expected P&L", "$3,345,129")
        with col3:
            st.metric("Risk/Reward", "15.88:1")
        with col4:
            st.metric("Sharpe Ratio", "1.35")
        
        # Price Impact
        st.markdown("---")
        st.subheader("💰 Price Impact")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Current Price", f"${entry_price:.2f}")
        with col2:
            st.metric("Expected Price", "$191.05", "-14.9%")
        
        st.info("📊 Interactive price impact chart would appear here (from stock_price_viz.py)")
        
        # Scenario Breakdown
        st.markdown("---")
        st.subheader("📊 Scenario Distribution")
        
        scenarios = {
            "Media Firestorm": 48.2,
            "NHTSA Investigation": 34.1,
            "Legal Action": 12.8,
            "Voluntary Recall": 3.7,
            "Silent Fix": 1.0,
            "No Event": 0.2
        }
        
        for scenario, pct in scenarios.items():
            st.markdown(f"**{scenario}:** {pct}%")
        
        # Recommendation
        st.markdown("---")
        st.subheader("🎯 Recommendation")
        
        st.success("""
        ### 🟢 STRONG BUY
        
        **Confidence:** Very High
        
        **Rationale:**
        - Win rate: 95.3% (exceptional)
        - Risk/Reward: 15.9:1 (highly asymmetric)
        - Expected value: $3.3M (strong positive)
        - Sharpe ratio: 1.35 (excellent risk-adjusted returns)
        
        **Suggested Position:** 23.7% of capital (quarter-Kelly)
        """)
        
        # Actions
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📥 Download Report", use_container_width=True):
                st.info("Report download would trigger")
        with col2:
            if st.button("💼 Save to Portfolio", use_container_width=True):
                st.success("✅ Saved!")
        with col3:
            if st.button("📤 Share", use_container_width=True):
                st.info("Share dialog would open")


# ============================================================================
# PAGE: PORTFOLIO
# ============================================================================

def page_portfolio():
    """Portfolio tracking page"""
    
    st.title("📊 Portfolio Management")
    
    # Explanation
    st.info("""
    ### 💼 What is Portfolio?
    
    Track all your active and historical trades in one place:
    - **Monitor P&L** in real-time
    - **Track performance** across all positions
    - **Calculate returns** automatically
    - **Historical record** of all trades
    
    This helps you manage risk and optimize your trading strategy.
    """)
    
    st.markdown("---")
    st.subheader("🎯 Active Positions (3 trades)")
    
    # Positions table with dates
    positions = [
        {
            "symbol": "TSLA", 
            "direction": "Short", 
            "shares": 100000, 
            "entry": 224.50, 
            "current": 218.30, 
            "pnl": 620000, 
            "entry_date": "Feb 9, 2025",
            "days": 12
        },
        {
            "symbol": "F", 
            "direction": "Short", 
            "shares": 100000, 
            "entry": 62.50, 
            "current": 64.10, 
            "pnl": -160000,
            "entry_date": "Feb 13, 2025", 
            "days": 8
        },
        {
            "symbol": "GM", 
            "direction": "Short", 
            "shares": 100000, 
            "entry": 41.20, 
            "current": 40.50, 
            "pnl": 70000,
            "entry_date": "Feb 16, 2025", 
            "days": 5
        },
    ]
    
    for pos in positions:
        with st.expander(f"**{pos['symbol']}** - {pos['direction']} {pos['shares']:,} shares", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Entry Date", pos['entry_date'])
                st.metric("Entry Price", f"${pos['entry']:.2f}")
            
            with col2:
                st.metric("Days Held", pos['days'])
                st.metric("Current Price", f"${pos['current']:.2f}")
            
            with col3:
                pnl_delta = f"{((pos['current'] - pos['entry']) / pos['entry'] * 100):+.1f}%"
                st.metric("Price Change", pnl_delta)
                st.metric("Shares", f"{pos['shares']:,}")
            
            with col4:
                pnl_color = "normal" if pos['pnl'] > 0 else "inverse"
                st.metric(
                    "P&L", 
                    f"${abs(pos['pnl']):,}", 
                    f"{'Profit' if pos['pnl'] > 0 else 'Loss'}",
                    delta_color=pnl_color
                )
            
            # Action buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"Update {pos['symbol']}", key=f"update_{pos['symbol']}"):
                    st.info("Price update would refresh here")
            with col2:
                if st.button(f"Close Position", key=f"close_{pos['symbol']}", type="secondary"):
                    st.warning("Close position confirmation would appear")
            with col3:
                if st.button(f"Set Stop Loss", key=f"stop_{pos['symbol']}"):
                    st.info("Stop loss settings would open")
    
    st.markdown("---")
    
    # Total Summary
    total_pnl = sum(p['pnl'] for p in positions)
    total_invested = sum(p['entry'] * p['shares'] for p in positions)
    total_pct = (total_pnl / total_invested) * 100
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("**Total Positions**", "3")
    with col2:
        st.metric("**Total Invested**", f"${total_invested:,.0f}")
    with col3:
        color = "normal" if total_pnl > 0 else "inverse"
        st.metric("**Total P&L**", f"${abs(total_pnl):,}", f"{total_pct:+.1f}%", delta_color=color)
    with col4:
        win_rate = sum(1 for p in positions if p['pnl'] > 0) / len(positions) * 100
        st.metric("**Win Rate**", f"{win_rate:.0f}%")
    
    # Add new position button
    st.markdown("---")
    if st.button("➕ Add New Position", type="primary"):
        st.info("Form to add new position would appear here")


# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application entry point"""
    
    # Initialize session state
    if 'user_name' not in st.session_state:
        st.session_state.user_name = "Analyst"
    
    if 'main_nav' not in st.session_state:
        st.session_state.main_nav = "🏠 Home"
    
    # Sidebar navigation
    selected_page = render_sidebar_navigation()
    
    # Route to appropriate page
    if selected_page == "🏠 Home":
        page_home()
    
    elif selected_page == "🔍 Search & Analyze":
        page_search_analyze()
    
    elif selected_page == "📊 Compare Vehicles":
        page_compare_vehicles()
    
    elif selected_page == "🏭 OEM Overview":
        page_oem_overview()
    
    elif selected_page == "🎲 Monte Carlo":
        page_monte_carlo()
    
    elif selected_page == "📈 Portfolio":
        page_portfolio()
    
    else:
        st.info(f"Page '{selected_page}' coming soon!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 12px;'>
    RecallVantage v2.1 | © 2025 | 
    <a href='#'>Terms</a> | <a href='#'>Privacy</a> | <a href='#'>Support</a>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
