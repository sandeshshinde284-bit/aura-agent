"""
Aura - Cloud Remediation Demo
Google Agent Hackathon 2025
Working version without rerun issues
"""

import streamlit as st
import time
from datetime import datetime

# Page setup
st.set_page_config(
    page_title="Aura - Autonomous Remediation", 
    page_icon="🤖",
    layout="wide"
)

def main():
    st.title("🤖 Aura - Autonomous Remediation Agent")
    st.markdown("*Transforming reactive alerts into proactive autonomous solutions*")
    
    # Dashboard metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Alerts Processed", "1,247", "+23 today")
    with col2:
        st.metric("Issues Resolved", "1,156", "92.7% success")
    with col3:
        st.metric("Cost Saved", "$127,450", "+$2,340 this week")
    with col4:
        st.metric("Avg Resolution", "2.3 min", "-45% faster")
    
    st.markdown("---")
    
    # Sidebar controls
    st.sidebar.title("🎮 Demo Controls")
    st.sidebar.markdown("Select a scenario to demonstrate Aura's capabilities:")
    
    # Alert scenarios
    alert_scenarios = {
        "cost_anomaly": "💰 Cost Spike - VM Running Unused",
        "security_vulnerability": "🔒 Security Breach - Open Firewall",
        "performance_degradation": "⚡ Performance Issue - Low Memory"
    }
    
    selected_scenario = st.sidebar.selectbox(
        "Choose Alert Scenario:",
        list(alert_scenarios.keys()),
        format_func=lambda x: alert_scenarios[x]
    )
    
    # Demo trigger
    demo_started = st.sidebar.button("🚨 Launch Aura Demo", type="primary")
    
    if demo_started:
        st.session_state.demo_running = True
        st.session_state.current_scenario = selected_scenario
    
    # Info section
    with st.sidebar.expander("ℹ️ How Aura Works"):
        st.markdown("""
        **Aura's Autonomous Pipeline:**
        
        1. **🔍 Alert Detection** - Real-time monitoring
        2. **🧠 AI Analysis** - Root cause identification  
        3. **💡 Smart Remediation** - Automated solution generation
        4. **✋ Human Approval** - Safety checkpoint
        5. **🚀 Autonomous Execution** - Automatic problem resolution
        """)
    
    # Run demo if triggered
    if st.session_state.get('demo_running', False):
        run_demo(st.session_state.current_scenario)

def run_demo(scenario):
    """Main demo workflow"""
    
    st.markdown("## 🚨 Step 1: Alert Detection")
    
    # Alert data based on scenario
    alert_info = get_alert_info(scenario)
    
    # Alert metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Severity", alert_info["severity"])
    with col2:
        st.metric("Resource", alert_info["resource"])
    with col3:
        st.metric("Duration", alert_info["duration"])
    with col4:
        st.metric("Status", "🔍 Analyzing")
    
    st.success(f"**Alert Details**: {alert_info['description']}")
    
    with st.expander("📋 Raw Alert Data"):
        st.json(alert_info)
    
    st.markdown("---")
    
    # Step 2: AI Analysis
    st.markdown("## 🧠 Step 2: AI Analysis")
    
    if st.button("🔄 Start Analysis", key="start_analysis"):
        run_analysis(scenario)
    
    if st.session_state.get('analysis_done', False):
        show_analysis_results(scenario)
        st.markdown("---")
        
        # Step 3: Remediation
        st.markdown("## 💡 Step 3: Proposed Remediation")
        show_remediation_plan(scenario)
        st.markdown("---")
        
        # Step 4: Execution
        st.markdown("## 🚀 Step 4: Human Approval & Execution")
        show_execution_section(scenario)

def run_analysis(scenario):
    """Run AI analysis with progress"""
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    analysis_steps = [
        "🔍 Scanning alert patterns...",
        "📊 Analyzing resource metrics...",
        "🧠 Determining root cause...",
        "📈 Calculating confidence score...",
        "✅ Analysis complete!"
    ]
    
    for i, step in enumerate(analysis_steps):
        status_text.text(step)
        progress_bar.progress((i + 1) * 20)
        time.sleep(0.8)
    
    st.session_state.analysis_done = True
    
    # Clear progress indicators
    progress_bar.empty()
    status_text.empty()

def show_analysis_results(scenario):
    """Show analysis results"""
    
    analysis_data = get_analysis_data(scenario)
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("AI Confidence", f"{analysis_data['confidence']}%", "High")
    with col2:
        st.metric("Risk Level", f"{analysis_data['risk']}/10", "Medium")
    with col3:
        st.metric("Urgency", analysis_data['urgency'])
    
    # Root cause
    st.info(f"🎯 **Root Cause**: {analysis_data['root_cause']}")
    
    # Contributing factors
    st.markdown("**Contributing Factors:**")
    for factor in analysis_data['factors']:
        st.markdown(f"• {factor}")

def show_remediation_plan(scenario):
    """Show remediation plan"""
    
    remediation = get_remediation_data(scenario)
    
    # Plan overview
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Action**: {remediation['action']}")
        st.markdown(f"**Time**: {remediation['time']}")
    with col2:
        st.markdown(f"**Outcome**: {remediation['outcome']}")
        st.markdown(f"**Success Rate**: {remediation['success_rate']}%")
    
    # Commands
    st.markdown("### 📝 Execution Commands")
    st.code(remediation['commands'], language="bash")
    
    # Safety info
    with st.expander("🔄 Safety & Rollback"):
        st.markdown("**Safety Measures:**")
        for measure in remediation['safety']:
            st.markdown(f"• {measure}")
        st.markdown("**Rollback Command:**")
        st.code(remediation['rollback'], language="bash")

def show_execution_section(scenario):
    """Show execution and approval section"""
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("✅ Approve & Execute", type="primary", key="approve"):
            execute_remediation(scenario)
    
    with col2:
        if st.button("❌ Reject", key="reject"):
            st.error("❌ Plan rejected. Escalating to human operators.")
    
    with col3:
        if st.button("⏸️ Defer", key="defer"):
            st.warning("⏸️ Execution deferred. Will retry in 1 hour.")
    
    # Show execution results if completed
    if st.session_state.get('execution_done', False):
        show_execution_results(scenario)

def execute_remediation(scenario):
    """Execute the remediation"""
    
    st.markdown("---")
    st.markdown("## ⚡ **EXECUTING REMEDIATION**")
    
    # Execution progress
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    exec_steps = [
        "🔐 Authenticating with Google Cloud...",
        "📡 Establishing connection...",
        "⚡ Executing commands...",
        "✅ Verifying results...",
        "📊 Updating monitoring..."
    ]
    
    for i, step in enumerate(exec_steps):
        status_text.text(step)
        progress_bar.progress((i + 1) * 20)
        time.sleep(1)
    
    st.session_state.execution_done = True
    
    # Clear progress
    progress_bar.empty()
    status_text.empty()

def show_execution_results(scenario):
    """Show final execution results"""
    
    st.success("🎉 **REMEDIATION EXECUTED SUCCESSFULLY!**")
    
    # Results metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Execution Time", "2.3 seconds")
    with col2:
        st.metric("Commands Run", "3/3")
    with col3:
        st.metric("Status", "✅ Success")
    with col4:
        st.metric("Rollback", "Available")
    
    # Impact details
    impact_data = get_impact_data(scenario)
    
    st.markdown(f"### {impact_data['title']}")
    for detail in impact_data['details']:
        st.markdown(f"• {detail}")
    
    # Timeline
    st.markdown("### ⏱️ Resolution Timeline")
    timeline = [
        ("🚨 Alert Received", "00:00:00"),
        ("🧠 Analysis Complete", "00:00:08"),
        ("💡 Plan Generated", "00:00:12"),
        ("✋ Human Approved", "00:02:15"),
        ("🚀 Execution Started", "00:02:18"),
        ("✅ Issue Resolved", "00:02:23")
    ]
    
    for event, time_stamp in timeline:
        st.markdown(f"**{time_stamp}** - {event}")
    
    # Success celebration
    st.balloons()
    
    # Final message
    st.markdown("---")
    st.success("🤖 **Aura has successfully resolved the issue autonomously!** Ready for the next alert.")
    
    # Reset button
    if st.button("🔄 Run Another Demo"):
        keys_to_clear = [
        'demo_running', 
        'analysis_done', 
        'execution_done', 
        'current_scenario'
       ]
        # Clear session state
        for key in keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun() 

# Data functions
def get_alert_info(scenario):
    """Get alert information based on scenario"""
    alerts = {
        "cost_anomaly": {
            "severity": "HIGH",
            "resource": "expensive-vm",
            "duration": "18 hours",
            "description": "VM running with 2% CPU usage - likely abandoned workload"
        },
        "security_vulnerability": {
            "severity": "CRITICAL",
            "resource": "allow-all-firewall",
            "duration": "2 days",
            "description": "Firewall rule allows unrestricted access from 0.0.0.0/0"
        },
        "performance_degradation": {
            "severity": "MEDIUM", 
            "resource": "web-server",
            "duration": "35 minutes",
            "description": "Memory usage sustained above 90%"
        }
    }
    
    return alerts[scenario]

def get_analysis_data(scenario):
    """Get analysis results"""
    analysis = {
        "cost_anomaly": {
            "confidence": 95,
            "risk": 3,
            "urgency": "Medium",
            "root_cause": "VM instance running with minimal CPU utilization, indicating abandoned workload",
            "factors": [
                "No automatic shutdown policies configured",
                "VM oversized for actual workload",
                "Missing cost monitoring alerts"
            ]
        },
        "security_vulnerability": {
            "confidence": 98,
            "risk": 9,
            "urgency": "Critical",
            "root_cause": "Firewall rule permits unrestricted access from any IP on all ports",
            "factors": [
                "Rule likely created for testing and forgotten",
                "No regular security policy audits",
                "Missing principle of least privilege"
            ]
        },
        "performance_degradation": {
            "confidence": 87,
            "risk": 5,
            "urgency": "High",
            "root_cause": "Web server undersized for current traffic load causing memory exhaustion",
            "factors": [
                "Traffic increased beyond instance capacity",
                "No auto-scaling configured",
                "Memory-intensive apps not optimized"
            ]
        }
    }
    
    return analysis[scenario]

def get_remediation_data(scenario):
    """Get remediation plan data"""
    plans = {
        "cost_anomaly": {
            "action": "Stop unused VM instance",
            "time": "2 minutes",
            "outcome": "$30/day cost savings",
            "success_rate": 95,
            "commands": """# Stop expensive VM
gcloud compute instances stop expensive-vm --zone=us-central1-a

# Create backup snapshot
gcloud compute disks snapshot expensive-vm --snapshot-names=backup-$(date +%Y%m%d)""",
            "safety": [
                "Backup snapshot created",
                "Non-critical workload verified",
                "Can restart anytime"
            ],
            "rollback": "gcloud compute instances start expensive-vm --zone=us-central1-a"
        },
        "security_vulnerability": {
            "action": "Replace firewall rule",
            "time": "1 minute",
            "outcome": "99% attack surface reduction",
            "success_rate": 92,
            "commands": """# Remove dangerous rule
gcloud compute firewall-rules delete allow-all-traffic --quiet

# Create secure replacement
gcloud compute firewall-rules create secure-web-access --allow tcp:80,tcp:443""",
            "safety": [
                "Replacement rule created immediately",
                "Only essential ports exposed",
                "Change logged for audit"
            ],
            "rollback": "# Not recommended - recreates vulnerability"
        },
        "performance_degradation": {
            "action": "Upgrade instance type",
            "time": "4 minutes", 
            "outcome": "2x memory capacity",
            "success_rate": 89,
            "commands": """# Stop for upgrade
gcloud compute instances stop web-server --zone=us-west1-a

# Upgrade machine type
gcloud compute instances set-machine-type web-server --machine-type=n1-standard-4

# Restart upgraded server
gcloud compute instances start web-server --zone=us-west1-a""",
            "safety": [
                "Maintenance window scheduled",
                "Health checks configured",
                "Gradual traffic restoration"
            ],
            "rollback": "gcloud compute instances set-machine-type web-server --machine-type=n1-standard-2"
        }
    }
    
    return plans[scenario]

def get_impact_data(scenario):
    """Get impact assessment data"""
    impacts = {
        "cost_anomaly": {
            "title": "💰 Cost Optimization Complete",
            "details": [
                "VM 'expensive-vm' safely stopped",
                "Cost reduced from $45/day to $15/day", 
                "Monthly savings: $900",
                "Backup created for safety"
            ]
        },
        "security_vulnerability": {
            "title": "🔒 Security Vulnerability Eliminated",
            "details": [
                "Dangerous firewall rule removed",
                "Secure replacement created",
                "Attack surface reduced by 99%",
                "Critical risk eliminated"
            ]
        },
        "performance_degradation": {
            "title": "⚡ Performance Issue Resolved",
            "details": [
                "Server upgraded to n1-standard-4",
                "Memory doubled from 8GB to 16GB",
                "Performance restored to optimal",
                "Expected 70% reduction in memory pressure"
            ]
        }
    }
    
    return impacts[scenario]

if __name__ == "__main__":
    main()
