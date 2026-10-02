"""Synthetic demo inputs; values and clock are not real adoption evidence."""

from datetime import datetime, timezone


NOW = datetime(2026, 10, 2, 12, tzinfo=timezone.utc)
START = "2026-10-01T00:00:00Z"
END = "2026-10-02T00:00:00Z"
NEXT_REVIEW = "2026-10-09T12:00:00Z"


def initiative_data(owner="owner-a"):
    return {
        "title": "Synthetic assisted support pilot",
        "outcome": "Meet the response quality threshold for the eligible sample",
        "owner": owner, "beneficiaries": "Fixture support staff and customers",
        "baseline": "Unknown; reviewer must establish a comparable baseline before an improvement claim",
        "assumptions": ["The sample represents the declared eligible population"],
        "alternatives": ["Improve support guidance without assisted drafting"],
        "criteria": [{"id": "quality", "claim": "Sampled drafts meet the rubric",
                      "unit": "percent", "operator": "gte", "threshold": 95,
                      "maxAgeSeconds": 604800, "method": "rubric-v1", "population": "eligible-cases-v1"}],
        "budgetMinor": 60000, "currency": "USD", "reviewAt": NEXT_REVIEW,
        "stopConditions": ["Pause for a quality breach or exhausted reservation budget"],
        "dependencies": ["Reviewed knowledge-base fixture"],
    }


def mandate_data(initiative_ref, delegate="agent-a"):
    return {
        "initiativeRef": initiative_ref, "purpose": "Reserve resources for assisted drafting",
        "delegate": delegate, "actions": ["draft"], "targets": ["support-queue"],
        "dataScope": "Synthetic eligible support cases only", "budgetMinor": 60000,
        "startsAt": START, "expiresAt": "2026-10-15T00:00:00Z",
        "escalation": "Fixture owner reviews uncertainty; pause blocks new local reservations only",
        "furtherDelegation": False,
    }


def observation_data(initiative_ref, value=90):
    return {
        "initiativeRef": initiative_ref, "kind": "outcome", "criterionId": "quality",
        "status": "measured", "value": value, "unit": "percent",
        "source": "synthetic-evaluation-01", "method": "rubric-v1", "population": "eligible-cases-v1",
        "windowStart": START, "windowEnd": END, "observedAt": "2026-10-02T10:00:00Z",
        "limitations": ["Synthetic observations; no causal or customer-benefit claim"], "supersedes": None,
    }
