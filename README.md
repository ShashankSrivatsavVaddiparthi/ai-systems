# **ai-systems**

This repository contains a unified collection of AI engineering projects, tools, and shared infrastructure developed for applied AI, agentic systems, multimodal applications, and data-centric workflows.

The monorepo follows a structured, scalable layout:

* A **`common/`** directory for shared libraries
* A **`projects/`** directory for clean, refactored systems
* A **`legacy/`** directory containing older prototypes for reference
* A **`docs/`** directory for architectural design, standards, and patterns
* A **`scripts/`** directory for automation and tooling
* An **`envs/`** directory for standardized environment configurations

This structure ensures consistency, reusability, and maintainability across all current and future AI projects.

---

## **Repository Structure**

<pre class="overflow-visible!" data-start="2637" data-end="3009"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>ai-systems/
├── common/        </span><span># Shared utilities (logging, config, helpers)</span><span>
├── projects/      </span><span># Clean, refactored implementations (initially empty)</span><span>
├── legacy/        </span><span># Imported older projects (unrefactored)</span><span>
├── envs/          </span><span># Environment definitions</span><span>
├── docs/          </span><span># Architectural and design documentation</span><span>
├── scripts/       </span><span># Helper scripts</span><span>
└── README.md
</span></span></code></div></div></pre>

---

## **Goals of This Monorepo**

1. Provide a **clean, consistent foundation** for all future AI engineering projects.
2. Maintain a **professional structure** suitable for long-term development, open-source release, and potential commercialization.
3. Enable  **shared tooling** , such as:
   * Observability & tracing framework
   * Synthetic data generator
   * Unified logging/config layers
4. Allow existing experimental repos to be preserved under `legacy/` while new refactored implementations live under `projects/`.

---

## **Migration Strategy**

* Older standalone repositories are copied into `legacy/`  **without history** .
* As each project is upgraded, it is rebuilt or refactored inside `projects/`.
* Shared logic gradually moves into `common/`.
* Legacy content remains available for reference until fully replaced.

---

## **Phased Development Plan**

**Phase 0:** Monorepo setup

**Phase 1:** Observability & Synthetic Data utilities

**Phase 2+:** Clean project migrations and new system development (multimodal, robotics, DS automation, etc.)

---

## **License**

MIT License

---

## **Status**

Active development — structure and utilities are being prepared.
