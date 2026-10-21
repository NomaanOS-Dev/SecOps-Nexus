import os
import re
import math
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="SecOps Nexus Hub", page_icon="🛡️", layout="wide")

st.title("🛡️ SecOps Nexus - Unified Master Security Hub")
st.caption("All-in-One AI-Powered Cyber Security Operations Center (SOC) Suite | Built by NomaanOS-Dev")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

module = st.sidebar.radio(
    "Select Security Module:",
    ["🚨 SIEM Log Analyzer", "🛡️ Firmware Security Guardian", "📄 Document Threat Investigator"]
)

st.sidebar.markdown("---")
st.sidebar.info("Unified SOC platform powered by LangChain and GPT-4o-mini.")

# Module 1: SIEM Log Analyzer
if module == "🚨 SIEM Log Analyzer":
    st.subheader("🚨 SIEM & Security Log Anomaly Analyzer")
    log_input = st.text_area("Paste Security Logs (auth.log, syslog, access.log):", height=200)
    
    if log_input and openai_api_key:
        if st.button("Analyze Logs"):
            with st.spinner("Analyzing threat patterns..."):
                os.environ["OPENAI_API_KEY"] = openai_api_key
                prompt = ChatPromptTemplate.from_template(
                    "You are a Lead SOC Analyst. Analyze these logs for suspicious activities, brute force attempts, or anomalies:\n\n{logs}"
                )
                chain = prompt | ChatOpenAI(model="gpt-4o-mini", temperature=0) | StrOutputParser()
                st.write(chain.invoke({"logs": log_input}))

# Module 2: Firmware Security Guardian
elif module == "🛡️ Firmware Security Guardian":
    st.subheader("🛡️ Firmware & Binary Vulnerability Scanner")
    uploaded_file = st.file_uploader("Upload Configuration or Binary Script", type=["txt", "conf", "log", "py", "json", "env"])
    
    if uploaded_file and openai_api_key:
        content = uploaded_file.getvalue().decode("utf-8", errors="ignore")
        st.code(content[:1000], language="text")
        
        if st.button("Run Vulnerability Scan"):
            with st.spinner("Scanning for hardcoded secrets and risks..."):
                os.environ["OPENAI_API_KEY"] = openai_api_key
                prompt = ChatPromptTemplate.from_template(
                    "You are a Firmware Security Expert. Audit this code/config for hardcoded secrets, keys, or security vulnerabilities:\n\n{content}"
                )
                chain = prompt | ChatOpenAI(model="gpt-4o-mini", temperature=0) | StrOutputParser()
                st.write(chain.invoke({"content": content[:2000]}))

# Module 3: Document Threat Investigator
elif module == "📄 Document Threat Investigator":
    st.subheader("📄 Security Document & Policy Investigator")
    doc_text = st.text_area("Paste Security Policy / Incident Document Text:", height=200)
    query = st.text_input("Ask a Security Question:")
    
    if doc_text and query and openai_api_key:
        if st.button("Investigate Document"):
            with st.spinner("Extracting insights..."):
                os.environ["OPENAI_API_KEY"] = openai_api_key
                prompt = ChatPromptTemplate.from_template(
                    "Answer the security question based on this document context:\n\nContext:\n{context}\n\nQuestion: {query}"
                )
                chain = prompt | ChatOpenAI(model="gpt-4o-mini", temperature=0) | StrOutputParser()
                st.write(chain.invoke({"context": doc_text[:2000], "query": query}))
