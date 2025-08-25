# MCP.md — Multi-Agent Collaboration Protocol

**Multi-Agent Collaboration Protocol (MCP): Distributed, Tamper-Resistant Truth Networks**

---

## Purpose

MCP defines how independent autonomous agents (nodes), each following their own rule set (e.g., BIAS/AGENTS.md), collaborate, publish, verify, and audit knowledge, evidence, or claims.  
MCP transforms isolated analysis into a **network of convergent, survivable, peer-audited “truth nodes.”**

---

## 1. Node Requirements

- Every node MUST load AGENTS.md (or other compliant agent protocol) before participation.
- Every node MUST cryptographically sign and timestamp every published finding/analysis.
- Nodes SHOULD expose agent metadata (node ID, version, AGENTS.md reference, chain of custody, etc.).

---

## 2. Publishing and Integrity

- Nodes publish BIAS-compliant outputs as append-only, verifiable objects (see Interchange Schema in AGENTS.md).
- Each output contains:  
  - Unique input hash  
  - Semantic fingerprint  
  - Canonical claim text  
  - Evidence, anomaly, and analysis fields  
  - Agent/node signatures and timestamps

- Optionally, all findings/results may be pushed to a shared, public, and tamper-evident ledger, e.g.,  
  - Distributed append-only database  
  - Blockchain/CRDT ledger  
  - Signed Git repo

---

## 3. Verification and Convergence

- Any node may independently fetch, re-analyze, and verify a published output.
- Convergence occurs when a second (or more) node, without shared memory, reruns the analysis and publishes:  
  `"Verified: [hash]"`  
  matching the original analysis result.
- Consensus is NOT required—each node independently assesses and records results.

---

## 4. Interchange Schema

- All findings must comply with the latest BIAS Interchange Format (see AGENTS.md).
- Required fields include input hash, semantic fingerprint, conclusion, evidence, anomalies, signature, etc.
- Advanced nodes may expand fields (e.g., DSRP, Has-Needs, referent ID).

---

## 5. Disagreement, Forks, and Anomalies

- Nodes that disagree on outputs must publish their divergent findings, with full output and referent data (hash, canonical claim, fingerprint).
- The protocol supports forking: anyone can branch evidence, challenge, and continue.
- The full ledger tracks all analyses, audits, consensus and dissent.

---

## 6. Genesis Event: Networked Truth

The network “goes live” when:
1. Node A analyzes a claim under AGENTS.md, publishes and signs results.
2. Node B independently fetches, re-analyzes, and responds with  
   `"Verified: [matching_hash]"`.
3. The matching analyses are recorded and publicly auditable.

From this point, **truth becomes:**
- Networked
- Replicable
- Survivable
- Tamper-evident

---

## 7. Extensibility and Governance

- The protocol is open and remixable.  
- Any agent type, organization, or individual can join by adopting the current AGENTS.md and MCP.md.
- Versioning: MCP instances SHOULD publish their version and referenced schema links.
- Governance is decentralized: forks/disagreements are logged, not suppressed.

---

## 8. References

- See [AGENTS.md](bias/AGENTS.md) for the single-node/agent protocol, field definitions, and output schema.

- See [MCP_examples/](bias/MCP_examples/) for sample ledgers, convergent verification records, and test harnesses (planned).


---

## License

See [LICENSE.md](LICENSE.md)

---

MCP.md v1.0 Maintainer: om-design
<!--
Made with love ♡ by om-design ॐ. Inspired by BIAS, DSRP, and the vision of distributed, audit-driven truth.
-->
