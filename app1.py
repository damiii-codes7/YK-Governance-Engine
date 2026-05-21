import streamlit as st

# Streamlit App Styling & Layout
st.set_page_config(page_title="YK Compliance - EU AI Act Classifier", page_icon="⚖️", layout="centered")

st.title("⚖️ EU AI Act Risk Classifier & Governance Engine")
st.write("Developed by **Adv. Damini Yasodai K.** for the +rhett. Legal-Tech Hackathon")
st.markdown("---")

st.subheader("🔮 Analyze an AI System for Regulatory Risk")
user_input = st.text_area(
    "Enter a detailed description of the AI system, its deployment domain, and its core functionalities:",
    placeholder="e.g., An AI algorithm used by a banking institution to evaluate individual credit scores and determine loan eligibility."
)

if st.button("Run Compliance Audit"):
    if user_input.strip() == "":
        st.warning("Please enter an AI system description to run the audit.")
    else:
        text = user_input.lower()
        
        # Defining Risk Criteria Keywords
        prohibited_keywords = ["social scoring", "biometric identification", "subliminal manipulation", "behavioral manipulation", "predictive policing"]
        high_risk_keywords = ["credit scoring", "recruitment", "resume screening", "employment evaluation", "critical infrastructure", "judicial", "law enforcement", "border control", "medical device"]
        limited_risk_keywords = ["chatbot", "deepfake", "generative text", "image generation", "ai writer", "customer support assistant"]

        # Evaluation Logic Block
        if any(keyword in text for keyword in prohibited_keywords):
            tier = "🔴 UNACCEPTABLE RISK (PROHIBITED)"
            rationale = "The system utilizes functionalities explicitly banned under Article 5 of the EU AI Act (e.g., biometric profiling, social tracking, or behavioral manipulation)."
            actions = [
                "**IMMEDIATE ACTION:** This deployment is illegal within the EU market.",
                "Cease development or strip the prohibited tracking capabilities immediately."
            ]
            color = "error"
            
        elif any(keyword in text for keyword in high_risk_keywords):
            tier = "🟠 HIGH-RISK SYSTEM"
            rationale = "The application operates in a regulated domain affecting critical infrastructure, personal safety, or core fundamental human rights (e.g., employment, banking, or justice systems)."
            actions = [
                "Establish a comprehensive, documented Risk Management System.",
                "Ensure high-quality, unbiased datasets are used for training models.",
                "Implement continuous, automated operational logging for technical audits.",
                "Enable 'Human-in-the-loop' continuous oversight parameters.",
                "Register the system in the official EU High-Risk AI database before deployment."
            ]
            color = "warning"
            
        elif any(keyword in text for keyword in limited_risk_keywords):
            tier = "🟡 LIMITED RISK / TRANSPARENCY OBLIGATIONS"
            rationale = "The AI system interacts directly with humans or generates synthetic media (e.g., chatbots, LLM content, or deepfakes)."
            actions = [
                "**Mandatory Transparency Notice:** Users must be explicitly notified that they are interacting with an artificial entity.",
                "Audio, visual, or text outputs must be watermarked or disclosed as AI-generated content."
            ]
            color = "info"
            
        else:
            tier = "🟢 MINIMAL RISK"
            rationale = "The system falls into a low-stakes software or processing category (e.g., generic optimization, internal operations, or text filtering) with no severe human impact."
            actions = [
                "No mandatory legal obligations required under the strict EU AI Act guidelines.",
                "Recommended: Voluntarily align with basic corporate ethical code guidelines."
            ]
            color = "success"

        # Displaying Results in UI
        st.markdown(f"### **Assigned Tier:** {tier}")
        if color == "error": st.error(rationale)
        elif color == "warning": st.warning(rationale)
        elif color == "info": st.info(rationale)
        else: st.success(rationale)
        
        st.markdown("#### 📋 Mandatory Governance Checklist:")
        for action in actions:
            st.write(f"- {action}")