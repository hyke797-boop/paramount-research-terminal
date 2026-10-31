import streamlit as st
import pandas as pd
from datetime import datetime

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Paramount Innovation | Research Terminal", layout="wide", page_icon="📈")

# --- CUSTOM CSS FOR "INSTITUTIONAL" LOOK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    .signal-card { background-color: #1c2128; border-left: 5px solid #ffcc00; padding: 20px; border-radius: 5px; margin-bottom: 20px; }
    h1, h2, h3 { color: #ffcc00 !important; }
    .stButton>button { background-color: #ffcc00; color: black; border-radius: 5px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.sidebar.title("Paramount Innovation")
st.sidebar.subheader("Dubai | Singapore Desk")
page = st.sidebar.radio("Go to:", ["Market Terminal", "Active Signals", "Research Brief", "Results Archive"])

# --- PAGE 1: MARKET TERMINAL ---
if page == "Market Terminal":
    st.title("🏛️ Institutional Research Terminal")
    st.write(f"**Market Status:** 🟢 Open | **Current Date:** {datetime.now().strftime('%d %B %Y')}")

    col1, col2, col3 = st.columns(3)
    col1.metric("XAU/USD", "4,014.31", "+14.30 (Relief Bounce)")
    col2.metric("Market Bias", "Neutral/Bullish")
    col3.metric("Volatility", "High", "News Pending")

    st.subheader("Live Market Structure (1H)")
    st.components.v1.html("""
        <div class="tradingview-widget-container" style="height:500px;width:100%">
          <div id="tradingview_12345" style="height:500px;width:100%"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget({
          "autosize": true, "symbol": "OANDA:XAUUSD", "interval": "60", "timezone": "Etc/UTC",
          "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6",
          "enable_publishing": false, "hide_side_toolbar": false, "allow_symbol_change": true,
          "container_id": "tradingview_12345"
        });
          </script>
        </div>
    """, height=500)

# --- PAGE 2: ACTIVE SIGNALS ---
elif page == "Active Signals":
    st.title("🎯 Live Execution Signals")
    st.markdown("""
        <div class="signal-card">
            <h3>GOLD (XAU/USD) - BUY LIMIT</h3>
            <p><b>Entry Zone:</b> 4,005.00 - 4,010.00</p>
            <p><b>Take Profit:</b> 4,025.00</p>
            <p><b>Stop Loss:</b> 3,995.00</p>
            <p><i>Note: High precision recovery move. Risk size suggestion: 0.05 for €2k accounts.</i></p>
        </div>
    """, unsafe_allow_html=True)

# --- PAGE 3: RESULTS ARCHIVE ---
elif page == "Results Archive":
    st.title("🏆 Verified Performance")
    st.success("Client: Fabrizio (Poland) | Profit: +$336.00")
    st.success("Client: Gerhard (Austria) | FTMO Phase 1 PASSED")
    st.success("Client: Luca (Italy) | Funding Pips Phase 2 PASSED")

st.sidebar.markdown("---")
st.sidebar.write("Logged in as: Senior Research Expert")
