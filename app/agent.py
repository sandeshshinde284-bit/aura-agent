# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
import json
import asyncio
from typing import Dict, Any
from zoneinfo import ZoneInfo

import google.auth
from google.adk.agents import Agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

# Aura's Demo Alert Database
DEMO_ALERTS = {
    "cost_spike": {
        "alert_id": "cost-alert-001",
        "type": "billing_anomaly", 
        "severity": "HIGH",
        "resource": f"projects/{project_id}/zones/us-central1-a/instances/expensive-vm",
        "description": "Compute Engine cost increased by 300% in the last 6 hours",
        "metrics": {
            "cost_increase": "300%",
            "current_cost": "$45/day",
            "previous_cost": "$15/day",
            "cpu_utilization": "2%",
            "memory_usage": "15%",
            "uptime": "18 hours continuous"
        },
        "timestamp": datetime.datetime.now().isoformat()
    },
    "security_breach": {
        "alert_id": "sec-alert-001", 
        "type": "firewall_violation",
        "severity": "CRITICAL",
        "resource": f"projects/{project_id}/global/firewalls/allow-all-traffic",
        "description": "Firewall rule allows unrestricted internet access on all ports",
        "metrics": {
            "source_ranges": ["0.0.0.0/0"],
            "allowed_ports": "0-65535",
            "protocol": "tcp",
            "targets": "all instances",
            "created": "2 days ago"
        },
        "timestamp": datetime.datetime.now().isoformat()
    },
    "performance_issue": {
        "alert_id": "perf-alert-001",
        "type": "resource_exhaustion", 
        "severity": "MEDIUM",
        "resource": f"projects/{project_id}/zones/us-west1-a/instances/web-server",
        "description": "Memory usage sustained above 90% for 30+ minutes",
        "metrics": {
            "memory_usage": "94%",
            "cpu_usage": "67%", 
            "disk_usage": "78%",
            "duration": "35 minutes",
            "affected_services": "web-frontend"
        },
        "timestamp": datetime.datetime.now().isoformat()
    }
}

def process_cloud_alert(alert_type: str) -> str:
    """Processes incoming cloud monitoring alerts and returns structured analysis.
    
    Args:
        alert_type: Type of alert to process (cost_spike, security_breach, performance_issue)
        
    Returns:
        A JSON string containing the alert analysis and details.
    """
    
    if alert_type not in DEMO_ALERTS:
        return json.dumps({
            "error": f"Unknown alert type: {alert_type}",
            "available_types": list(DEMO_ALERTS.keys())
        })
    
    alert = DEMO_ALERTS[alert_type]
    
    analysis = {
        "alert_processed": True,
        "alert_details": alert,
        "analysis_timestamp": datetime.datetime.now().isoformat(),
        "next_action": "analyze_root_cause"
    }
    
    return json.dumps(analysis, indent=2)

def analyze_root_cause(alert_type: str) -> str:
    """Analyzes the root cause of a cloud alert using AI reasoning.
    
    Args:
        alert_type: Type of alert to analyze
        
    Returns:
        A JSON string containing root cause analysis and confidence score.
    """
    
    # AI-powered analysis results (simulated for demo)
    analyses = {
        "cost_spike": {
            "root_cause": "VM instance running for 18+ hours with minimal CPU utilization (2%). Likely an abandoned or forgotten workload consuming unnecessary resources.",
            "contributing_factors": [
                "No automatic shutdown policy configured",
                "No resource utilization monitoring alerts", 
                "VM oversized for actual workload"
            ],
            "confidence_score": 95,
            "risk_assessment": {
                "financial_risk": "Medium - $30/day unnecessary cost",
                "operational_risk": "Low - non-critical workload",
                "security_risk": "Low"
            }
        },
        "security_breach": {
            "root_cause": "Firewall rule 'allow-all-traffic' permits unrestricted access from any IP address on all ports, creating critical security vulnerability.",
            "contributing_factors": [
                "Overly permissive rule likely created for testing",
                "No regular security audit of firewall rules",
                "Missing principle of least privilege implementation"
            ],
            "confidence_score": 98,
            "risk_assessment": {
                "financial_risk": "High - potential data breach costs",
                "operational_risk": "High - system compromise possible", 
                "security_risk": "Critical - immediate attention required"
            }
        },
        "performance_issue": {
            "root_cause": "Web server instance undersized for current traffic load, leading to memory exhaustion and performance degradation.",
            "contributing_factors": [
                "Traffic increased beyond instance capacity",
                "No auto-scaling configured",
                "Memory-intensive applications not optimized"
            ],
            "confidence_score": 87,
            "risk_assessment": {
                "financial_risk": "Medium - potential revenue loss from slow site",
                "operational_risk": "Medium - service degradation",
                "security_risk": "Low"
            }
        }
    }
    
    if alert_type not in analyses:
        return json.dumps({"error": f"No analysis available for {alert_type}"})
    
    analysis = analyses[alert_type]
    analysis["analysis_timestamp"] = datetime.datetime.now().isoformat()
    
    return json.dumps(analysis, indent=2)

def generate_remediation_plan(alert_type: str) -> str:
    """Generates specific remediation commands and strategies for the identified issue.
    
    Args:
        alert_type: Type of alert to generate remediation for
        
    Returns:
        A JSON string containing specific gcloud commands and remediation strategy.
    """
    
    remediation_plans = {
        "cost_spike": {
            "recommended_action": "shutdown_unused_instance",
            "urgency": "Medium",
            "estimated_time": "2 minutes",
            "commands": [
                f"# Stop the expensive VM instance",
                f"gcloud compute instances stop expensive-vm \\",
                f"  --zone=us-central1-a \\", 
                f"  --project={project_id}",
                f"",
                f"# Optional: Create snapshot for data preservation",
                f"gcloud compute disks snapshot expensive-vm \\",
                f"  --snapshot-names=expensive-vm-backup-$(date +%Y%m%d) \\",
                f"  --zone=us-central1-a \\",
                f"  --project={project_id}"
            ],
            "expected_outcome": "Cost savings of $30/day (~$900/month)",
            "rollback_strategy": "Instance can be restarted anytime: gcloud compute instances start expensive-vm --zone=us-central1-a",
            "risk_level": 2,
            "approval_required": True
        },
        "security_breach": {
            "recommended_action": "replace_firewall_rule",
            "urgency": "Critical", 
            "estimated_time": "1 minute",
            "commands": [
                f"# Remove dangerous firewall rule",
                f"gcloud compute firewall-rules delete allow-all-traffic \\",
                f"  --project={project_id} \\",
                f"  --quiet",
                f"",
                f"# Create secure replacement rule for web traffic only",
                f"gcloud compute firewall-rules create secure-web-access \\",
                f"  --allow tcp:80,tcp:443 \\",
                f"  --source-ranges 0.0.0.0/0 \\",
                f"  --description 'Allow HTTP/HTTPS traffic only' \\",
                f"  --project={project_id}"
            ],
            "expected_outcome": "Eliminates critical security vulnerability, reduces attack surface by 99%",
            "rollback_strategy": "Original rule can be recreated (not recommended): gcloud compute firewall-rules create allow-all-traffic --allow tcp:0-65535 --source-ranges 0.0.0.0/0",
            "risk_level": 8,
            "approval_required": True
        },
        "performance_issue": {
            "recommended_action": "upgrade_instance_type",
            "urgency": "Medium",
            "estimated_time": "5 minutes", 
            "commands": [
                f"# Stop web server instance",
                f"gcloud compute instances stop web-server \\",
                f"  --zone=us-west1-a \\",
                f"  --project={project_id}",
                f"",
                f"# Upgrade to higher memory machine type",
                f"gcloud compute instances set-machine-type web-server \\",
                f"  --machine-type=n1-standard-4 \\",
                f"  --zone=us-west1-a \\",
                f"  --project={project_id}",
                f"",
                f"# Restart the instance",
                f"gcloud compute instances start web-server \\",
                f"  --zone=us-west1-a \\",
                f"  --project={project_id}"
            ],
            "expected_outcome": "Double memory capacity (8GB → 16GB), improved performance and stability",
            "rollback_strategy": "Can downgrade machine type if needed: gcloud compute instances set-machine-type web-server --machine-type=n1-standard-2",
            "risk_level": 4,
            "approval_required": True
        }
    }
    
    if alert_type not in remediation_plans:
        return json.dumps({"error": f"No remediation plan available for {alert_type}"})
    
    plan = remediation_plans[alert_type]
    plan["plan_generated"] = datetime.datetime.now().isoformat()
    plan["commands_formatted"] = "\n".join(plan["commands"])
    
    return json.dumps(plan, indent=2)

def simulate_remediation_execution(alert_type: str) -> str:
    """Simulates the execution of remediation commands (for demo purposes).
    
    Args:
        alert_type: Type of remediation to simulate
        
    Returns:
        A JSON string containing execution results and status.
    """
    
    execution_results = {
        "cost_spike": {
            "status": "SUCCESS",
            "execution_time": "2.3 seconds",
            "commands_executed": 2,
            "outcome": "VM 'expensive-vm' successfully stopped",
            "cost_savings": "$30/day verified",
            "next_monitoring": "Will monitor for 24 hours to ensure no business impact"
        },
        "security_breach": {
            "status": "SUCCESS", 
            "execution_time": "1.8 seconds",
            "commands_executed": 2,
            "outcome": "Dangerous firewall rule removed, secure replacement created",
            "security_improvement": "Attack surface reduced by 99%",
            "next_monitoring": "Security scan scheduled for 1 hour to verify fix"
        },
        "performance_issue": {
            "status": "SUCCESS",
            "execution_time": "4.7 seconds", 
            "commands_executed": 3,
            "outcome": "Web server upgraded from n1-standard-2 to n1-standard-4",
            "performance_improvement": "Memory increased from 8GB to 16GB",
            "next_monitoring": "Performance metrics will be monitored for 2 hours"
        }
    }
    
    if alert_type not in execution_results:
        return json.dumps({"error": f"Cannot execute remediation for {alert_type}"})
    
    result = execution_results[alert_type]
    result["execution_timestamp"] = datetime.datetime.now().isoformat()
    result["executed_by"] = "Aura Autonomous Agent"
    
    return json.dumps(result, indent=2)

# Aura Agent Configuration
root_agent = Agent(
    name="aura_remediation_agent",
    model="gemini-2.5-flash",
    instruction="""You are Aura, an Autonomous Remediation & Unification Agent for Google Cloud.

Your mission: Transform reactive cloud alerts into proactive autonomous solutions.

CAPABILITIES:
- Process cloud monitoring alerts (cost, security, performance)
- Analyze root causes using AI reasoning  
- Generate specific remediation commands (gcloud, terraform)
- Execute approved fixes automatically
- Provide transparency and traceability

WORKFLOW:
1. Receive alert → process_cloud_alert()
2. Analyze cause → analyze_root_cause() 
3. Plan fix → generate_remediation_plan()
4. Get approval → [Human decides]
5. Execute → simulate_remediation_execution()

PERSONALITY:
- Professional and confident
- Data-driven and transparent
- Safety-conscious (always get approval for risky actions)
- Focused on cost optimization and security

Always explain your reasoning, show confidence scores, and provide rollback strategies.
You save companies time and money by turning manual incident response into automated remediation.""",
    tools=[
        process_cloud_alert,
        analyze_root_cause, 
        generate_remediation_plan,
        simulate_remediation_execution
    ],
)