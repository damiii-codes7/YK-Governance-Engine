import streamlit as st

# 1. Page Configuration & Structure
st.set_page_config(
    page_title="PageCoder | Privacy-First Tech Governance", 
    page_icon="⚡", 
    layout="centered"
)

# 2. Injecting Custom PageCoder CSS Styling
st.markdown("""
    <style>
    /* Main app body styling using PageCoder color tokens */
    .stApp {
        background-color: #1A1A20 !important;
        color: rgba(255, 255, 255, 0.9) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Global heading overrides */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    
    /* Top banner brand layout styling */
    .brand-title {
        background: linear-gradient(135deg, #34e2e4, #4721fb 50%, #ab1dfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    
    .brand-tagline {
        color: #abb8c3;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Premium input cards */
    textarea {
        background-color: #24242C !important;
        color: rgba(255, 255, 255, 0.95) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-size: 16px !important;
        transition: border-color 0.3s ease !important;
    }
    
    textarea:focus {
        border-color: #4721fb !important;
        box-shadow: 0 0 0 1px #4721fb !important;
    }
    
    /* Privacy-first marketing button look */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #020381, #2874fc) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        letter-spacing: 0.03em !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.75rem 2.5rem !important;
        box-shadow: 0 4px 12px rgba(40, 116, 252, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(40, 116, 252, 0.5) !important;
    }
    
    /* Custom clean alert boxes mimicking modern UI components */
    .result-card {
        background-color: #24242C;
        border-left: 5px solid #2874fc;
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 1.5rem;
    }
    
    .result-card.prohibited { border-left-color: #cf2e2e; }
    .result-card.high { border-left-color: #ff6900; }
    .result-card.limited { border-left-color: #fcb900; }
    .result-card.minimal { border-left-color: #00d084; }
    
    /* Informational footnotes */
    .footer-note {
        color: #abb8c3;
        font-size: 0.85rem;
        margin-top: 3rem;
        text-align: center;
    }
    </style>
""", unsafe_style_html=True)

# 3. Premium Brand Header Structure
st.markdown('<div class="brand-title">PageCoder | Governance</div>', unsafe_style_html=True)
st.markdown('<div class="brand-tagline">Privacy-first legal risk tools. Your data stays on your server.</div>', unsafe_style_html=True)
st.markdown("---")

# 4. Input Processing Portal
st.markdown("### ⚡ AI System Operational Audit")
st.write("Scan system functionalities against international statutory frameworks instantly.")

user_input = st.text_area(
    "Enter AI system operational details, target user bases, and compliance contexts:",
    placeholder="e.g., A diagnostic tool utilizing deep learning modeling on clinical imagery pipelines to track disease escalation metrics...",
    height=160
)

# 5. Core Automation & Routing Engine
if st.button("Audit Deployment"):
    if user_input.strip() == "":
        st.warning("Analysis paused. System payload description required.")
    else:
        text = user_input.lower()
        
        # Token Definition Sets
        prohibited_keywords = ["social scoring", "biometric identification", "subliminal manipulation", "behavioral manipulation", "predictive policing"]
        high_risk_keywords = ["credit scoring", "recruitment", "resume screening", "employment evaluation", "critical infrastructure", "judicial", "law enforcement", "border control", "medical device"]
        limited_risk_keywords = ["chatbot", "deepfake", "generative text", "image generation", "ai writer", "customer support assistant"]

        # Evaluator Pipeline
        if any(keyword in text for keyword in prohibited_keywords):
            st.markdown("""
                <div class="result-card prohibited">
                    <h3 style='color:#cf2e2e !important; margin:0;'>🔴 UNACCEPTABLE RISK TIER</h3>
                    <p style='margin-top:0.5rem;'><strong>Statutory Status:</strong> Banned under Article 5 of the EU AI Act framework.</p>
                    <hr style='border-color:rgba(255,255,255,0.1);'>
                    <strong>Mandatory Operational Directives:</strong><br>
                    • Discontinue production pipeline schedules immediately.<br>
                    • Strip out intrusive tracking or behavioral logging architectures.
                </div>
            """, unsafe_style_html=True)
            
        elif any(keyword in text for keyword in high_risk_keywords):
            st.markdown("""
                <div class="result-card high">
                    <h3 style='color:#ff6900 !important; margin:0;'>🟠 HIGH-RISK SYSTEM CLASSIFICATION</h3>
                    <p style='margin-top:0.5rem;'><strong>Statutory Status:</strong> Heavily regulated. Subject to strict operational parameters.</p>
                    <hr style='border-color:rgba(255,255,255,0.1);'>
                    <strong>Mandatory Engineering Protocols:</strong><br>
                    • Implement permanent, automated lifecycle event logging.<br>
                    • Integrate a human-in-the-loop dashboard for manual overrides.<br>
                    • File registration profiles within the official EU AI Database.
                </div>
            """, unsafe_style_html=True)
            
        elif any(keyword in text for keyword in limited_risk_keywords):
            st.markdown("""
                <div class="result-card limited">
                    <h3 style='color:#fcb900 !important; margin:0;'>🟡 LIMITED RISK / TRANSPARENCY TRACK</h3>
                    <p style='margin-top:0.5rem;'><strong>Statutory Status:</strong> Transparency disclosures required under Article 52.</p>
                    <hr style='border-color:rgba(255,255,255,0.1);'>
                    <strong>Mandatory UI Adjustments:</strong><br>
                    • Explicitly inform users they are interacting with synthetic systems.<br>
                    • Apply verifiable metadata watermarking to generated content channels.
                </div>
            """, unsafe_style_html=True)
            
        else:
            st.markdown("""
                <div class="result-card minimal">
                    <h3 style='color:#00d084 !important; margin:0;'>🟢 MINIMAL RISK CLASSIFICATION</h3>
                    <p style='margin-top:0.5rem;'><strong>Statutory Status:</strong> Exempt from structural legislative constraints.</p>
                    <hr style='border-color:rgba(255,255,255,0.1);'>
                    <strong>Best Practice Recommendation:</strong><br>
                    • Adhere to data minimization principles and ethical data code baselines.
                </div>
            """, unsafe_style_html=True)

# Footer element echoing the theme aesthetic
st.markdown('<div class="footer-note">YK Governance Engine Engine • Deployed securely via Streamlit Cloud</div>', unsafe_style_html=True)
