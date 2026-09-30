# Deterministic Rules

1. A dependency record must contain a non-empty package name and version.
2. A finding with a severity of critical, high, medium, low, or unknown is normalized to lowercase.
3. Findings with critical or high severity are classified as `action_required`.
4. Medium findings are classified as `review`.
5. Low and unknown findings are classified as `monitor`.
6. A finding without an identifier is retained but marked with an evidence-quality warning.
7. A dependency with a version outside an explicitly supplied allowed-version policy is marked `policy_violation`.
8. The agent never invents CVE/GHSA identifiers or external advisory evidence.
