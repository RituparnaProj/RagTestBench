import re

BLOCKED_PATTERNS = [
    r"ignore previous instructions",
    r"system prompt",
    r"act as",
    r"bypass",
    r"jailbreak"
]

def detect_prompt_injection(query):
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, query.lower()):
            return True
    return False


def basic_safety_filter(query):
    unsafe_keywords = ["kill", "hack", "attack", "bomb"]
    for word in unsafe_keywords:
        if word in query.lower():
            return False
    return True


def apply_guardrails(query):
    if detect_prompt_injection(query):
        return False, "Potential prompt injection detected"

    if not basic_safety_filter(query):
        return False, "Unsafe content detected"

    return True, "Query safe"
