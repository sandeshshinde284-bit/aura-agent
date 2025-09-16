"""
Aura - Cloud Remediation Demo
Google Agent Hackathon 2025
Working version without rerun issues
"""

import streamlit as st
import time
from datetime import datetime

def add_live_features():
    """Add real-time elements and system status"""
    # Current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    st.sidebar.markdown(f"🕐 **Last Updated**: {current_time}")
    
    # System status
    st.sidebar.markdown("### 🟢 System Status")
    st.sidebar.success("✅ All systems operational")
    st.sidebar.info("🔗 Connected: Google Cloud")
    st.sidebar.info("🧠 AI Model: Gemini 2.5 Flash")
    st.sidebar.info("📍 Region: us-central1")
    
    # Add cost calculator
    st.sidebar.markdown("### 💰 ROI Calculator")
    monthly_spend = st.sidebar.number_input("Monthly Cloud Spend ($)", 10000, 1000000, 50000)
    projected_savings = monthly_spend * 0.15  # 15% savings
    st.sidebar.success(f"Projected Savings: ${projected_savings:,.0f}/month")

# Page setup
st.set_page_config(
    page_title="Aura - Autonomous Remediation", 
    page_icon="🤖",
    layout="wide"
)

def main():
    st.markdown("""
    <div style='text-align: center; background: linear-gradient(90deg, #4285f4, #34a853); 
               padding: 20px; border-radius: 10px; margin-bottom: 20px; color: white;'>
    <h1>🤖 AURA - Autonomous Remediation Agent</h1>
    <h3>Google Agent Hackathon 2025</h3>
    <p style='font-size: 18px;'><i>"From Alert to Resolution in Minutes, Not Hours"</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dashboard metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("🚨 Alerts Today", "47", "+12 from yesterday")
    with col2:
        st.metric("⚡ Avg Resolution", "2.3 min", "-67% improvement")  
    with col3:
        st.metric("💰 Cost Saved", "$23,400", "+18% this month")
    with col4:
        st.metric("🎯 Success Rate", "95.3%", "+2.1% this week")
    with col5:
        st.metric("⏱️ Uptime", "99.97%", "SLA exceeded")
    
    st.markdown("---")
    
    # Sidebar controls
    st.sidebar.title("🎮 Demo Controls")
    st.sidebar.markdown("Select a scenario to demonstrate Aura's capabilities:")
    
    # Alert scenarios
    alert_scenarios = {
        "cost_anomaly": "💰 Cost Spike - VM Running Unused ($45/day waste)",
        "security_vulnerability": "🔒 Security Breach - Open Firewall (Critical Risk)",
        "performance_degradation": "⚡ Performance Issue - Memory Exhaustion (94% usage)",
        "storage_waste": "💾 Storage Waste - Orphaned Volumes ($200/month)",
        "network_anomaly": "🌐 Network Spike - Unusual Traffic (Security concern)",
        "compliance_violation": "⚖️ Compliance Risk - Unencrypted Database"
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
    add_live_features()
    
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
    
    st.markdown("### ⚡ Manual vs Aura Comparison")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Manual Process", "23 hours", "❌ Slow")
    with col2:
        st.metric("Aura Process", "2.3 minutes", "✅ Fast")  
    with col3:
        st.metric("Time Savings", "99.8%", "🚀 Improvement")

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
    
    st.markdown("""
        <div style='background: #e8f5e8; padding: 20px; border-radius: 10px; border-left: 5px solid #4caf50;'>
        <h3>🎉 AUTONOMOUS REMEDIATION SUCCESSFUL!</h3>
        <p>Aura has successfully resolved the cloud incident without human intervention.</p>
        </div>
        """, unsafe_allow_html=True)

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
        },
        # ADD THESE 3 NEW SCENARIOS:
        "storage_waste": {
            "severity": "MEDIUM",
            "resource": "orphaned-disks-pool",
            "duration": "30 days",
            "description": "47 unattached disk volumes consuming storage unnecessarily"
        },
        "network_anomaly": {
            "severity": "HIGH", 
            "resource": "frontend-load-balancer",
            "duration": "15 minutes",
            "description": "Traffic spike 400% above normal - potential DDoS attack"
        },
        "compliance_violation": {
            "severity": "CRITICAL",
            "resource": "customer-database",
            "duration": "detected now", 
            "description": "Production database without encryption - GDPR violation risk"
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
        },
        "storage_waste": {
            "confidence": 92,
            "risk": 4,
            "urgency": "Medium",
            "root_cause": "Multiple disk volumes remain unattached after VM deletions",
            "factors": [
                "No automatic cleanup policies configured",
                "Manual VM deletion without disk cleanup",
                "Missing storage lifecycle management"
            ]
        },
        "network_anomaly": {
            "confidence": 88,
            "risk": 7,
            "urgency": "High",
            "root_cause": "Unusual traffic pattern suggests DDoS attack or viral content",
            "factors": [
                "Traffic increased 400% in 15 minutes",
                "No DDoS protection configured",
                "Source IPs from suspicious regions"
            ]
        },
        "compliance_violation": {
            "confidence": 99,
            "risk": 9,
            "urgency": "Critical",
            "root_cause": "Customer database lacks encryption violating GDPR requirements",
            "factors": [
                "Database created without encryption",
                "No compliance monitoring alerts",
                "Sensitive data at risk of exposure"
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
        },
        "storage_waste": {
            "action": "Delete orphaned disk volumes",
            "time": "3 minutes",
            "outcome": "$200/month storage savings",
            "success_rate": 94,
            "commands": """# List orphaned disks
gcloud compute disks list --filter="users:( )"

# Delete unattached volumes
gcloud compute disks delete orphaned-disk-1 orphaned-disk-2 --zone=us-central1-a

# Set up automatic cleanup policy
gcloud compute resource-policies create disk-lifecycle cleanup-policy""",
            "safety": [
                "Verify disks are truly orphaned",
                "Create snapshots before deletion",
                "Automatic policy prevents future waste"
            ],
            "rollback": "gcloud compute disks snapshot [disk-name] --snapshot-names=recovery-backup"
        },
        "network_anomaly": {
            "action": "Enable DDoS protection",
            "time": "2 minutes",
            "outcome": "Traffic normalized, attack blocked",
            "success_rate": 91,
            "commands": """# Enable Cloud Armor DDoS protection
gcloud compute security-policies create ddos-protection

# Apply rate limiting rule
gcloud compute security-policies rules create 1000 --security-policy=ddos-protection --expression="true" --action="rate-based-ban"

# Apply to load balancer
gcloud compute backend-services update frontend-service --security-policy=ddos-protection""",
            "safety": [
                "Gradual rate limiting implementation",
                "Whitelist known good IPs",
                "24/7 monitoring enabled"
            ],
            "rollback": "gcloud compute security-policies delete ddos-protection"
        },
        "compliance_violation": {
            "action": "Enable database encryption",
            "time": "5 minutes",
            "outcome": "GDPR compliance restored",
            "success_rate": 96,
            "commands": """# Create encrypted backup
gcloud sql backups create --instance=customer-database

# Enable encryption at rest
gcloud sql instances patch customer-database --storage-auto-increase --database-flags=cloudsql.enable_encryption_at_rest=on

# Verify encryption status
gcloud sql instances describe customer-database --format="value(settings.storageAutoResize)"




""",
            "safety": [
                "Backup created before changes",
                "Zero-downtime encryption process",
                "Compliance audit trail maintained"
            ],
            "rollback": "gcloud sql backups restore [BACKUP_ID] --restore-instance=customer-database"
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
        },
        "storage_waste": {
            "title": "💾 Storage Optimization Complete",
            "details": [
                "47 orphaned disk volumes deleted",
                "Storage cost reduced by $200/month",
                "Automatic cleanup policy implemented",
                "Future waste prevention enabled"
            ]
        },
        "network_anomaly": {
            "title": "🌐 Network Security Enhanced",
            "details": [
                "DDoS protection successfully enabled",
                "Malicious traffic blocked at edge",
                "Normal traffic flow restored",
                "24/7 monitoring activated"
            ]
        },
        "compliance_violation": {
            "title": "⚖️ Compliance Violation Resolved",
            "details": [
                "Database encryption enabled successfully",
                "GDPR compliance requirements met",
                "Customer data now fully protected",
                "Audit trail maintained for compliance"
            ]
        }
    }
    
    return impacts[scenario]

if __name__ == "__main__":
    main()
