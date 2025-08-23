# AGENTS.md

This document describes the agents (automated and human roles) that interact with the MCP repository.

---

## 1. MCP_GitHub_Bot

- **Description:**  
  Automates GitHub workflows, issue triage, and labeling.

- **Owner:**  
  @omdesign

- **Invocation:**  
  Triggered automatically on:
    - New issue creation
    - New or updated pull requests
    - Scheduled repository scans

- **Permissions:**  
  Write access to Issues and Pull Requests

- **Configuration:**  
  `.github/workflows/` directory (GitHub Actions)
  See workflow YAML files for details.

---

## 2. Humanify_Policy_AI

- **Description:**  
  Monitors and enforces compliance with the Humanify License guidelines.

- **Owner:**  
  @omdesign

- **Invocation:**  
  Runs on PRs that touch legal, license, or policy files (`LICENSE.md`, `humanify-template.md`).

- **Permissions:**  
  Commenting on and closing PRs; raising policy flags

- **Configuration:**  
  `.github/humanify-policy.yml`

---

## 3. Maintainer (Human)

- **Role:**  
  Reviews code, merges PRs, manages releases, and handles escalations from automated agents.

- **Contact:**  
  [omdesign.is@gmail.com](mailto:omdesign.is@gmail.com)

---

## 4. Contributor (Human)

- **Role:**  
  Proposes changes, creates issues/PRs, and participates in discussions.

- **Onboarding:**  
  See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 5. External Integrations (Optional)

_List any API integrations or webhook agents (e.g., Slack notifier, Grant management bot) here._

---

> **Note:**  
> Update this file whenever adding, removing, or changing agents or role responsibilities.

---

Last updated: August 23, 2025
