import json

# Sample input JSON
data = {
    "ts": 1749040087,
    "success": True,
    "errors": None,
    "response": {
        "cluster_id": "prod-cluster",
        "namespace": "default",
        "allowed": False,
        "recommendations": [
            {
                "action": "auto_stopping",
                "cost_before": 100,
                "cost_after": 66.67,
                "savings": 33.33,
                "savings_percentage": 33.33
            },
            {
                "action": "right_sizing",
                "meta": {
                    "cpu": "2",
                    "memory": "4Gi",
                    "repclia": 2
                },
                "cost_before": 66.67,
                "cost_after": 33.33,
                "savings": 66.67,
                "savings_percentage": 66.67
            }
        ]
    }
}

recommendations = data.get("response", {}).get("recommendations", [])

print(f"\n📊 Recommendations for Cluster: {data['response'].get('cluster_id')} (Namespace: {data['response'].get('namespace')})\n")
print("-" * 60)

for i, rec in enumerate(recommendations, 1):
    action = rec.get("action")
    print(f"Recommendation {i}:")

    if action == "auto_stopping":
        print(f"🔧 Action Type: Auto-Stopping")
        print("🛑 Explanation:")
        print("  - Enable auto-stopping for idle workloads or resources.")
        print("  - Helps reduce costs by shutting down unused infrastructure components.")
    elif action == "right_sizing":
        print(f"🔧 Action Type: Right Sizing (Re-sizing the workloads)")
        print("🛠️ Explanation:")
        print("  - Suggests adjusting CPU and memory allocations to better match actual usage.")
        print("  - Helps optimize resource utilization and reduce overprovisioning costs.")
    else:
        print(f"🔧 Action Type: {action}")

    print(f"💵 Cost Before: ${rec.get('cost_before'):.2f}")
    print(f"💰 Cost After:  ${rec.get('cost_after'):.2f}")
    print(f"✅ Savings:     ${rec.get('savings'):.2f} ({rec.get('savings_percentage'):.2f}%)")

    if rec.get("meta"):
        print("📦 Workload Resource Details:")
        for k, v in rec["meta"].items():
            label = "Replica" if k == "repclia" else k.capitalize()
            print(f"   - {label}: {v}")

    print("-" * 60)