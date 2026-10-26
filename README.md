# Marek Burza · Staff Software Engineer

[https://linkedin.com/in/mkburza](https://linkedin.com/in/mkburza) <!-- EMAIL --> <!-- PHONE -->

---

## SUMMARY

I take data and AI/ML systems from research prototypes to production and keep them there: training and inference pipelines, their data and ETL plumbing, and the model packaging, release and regression tooling that makes shipping a model routine rather than a project. Greenfield and existing systems: a multi-tenant IIoT platform on AWS at OSRAM, a fall-prevention ML service at Philips scaled past 100k users, a model release process at Paige taken from a multi-sprint, team-wide effort to a one-day, single-engineer operation, and a computer vision pipeline at Helsing taken to 2.8x throughput.

**Languages & platforms:** Python (20+ yrs), Rust, Go, Bash · AWS, Azure · Docker · Linux

**AI/ML:** PyTorch · distributed training (DDP, SLURM, Prefect) · TensorRT · model packaging and release automation · experiment tracking and metrics visualization (W&B, Neptune, Plotly)

**Platform & data:** CI/CD (GitLab CI, GitHub Actions) · ETL and data pipelines · S3 data lakes · PostgreSQL, TimescaleDB, MongoDB, Redis · FastAPI · observability (Grafana, DataDog)

**Performance & troubleshooting:** throughput and memory optimization · distributed-system debugging · automated regression monitoring · PyTorch Profiler, perf, pprof, mprof, Nsight

**Leadership:** teams of 9 (OSRAM), 5 (Paige), 4 (Huawei, Siemens) · product owner alongside engineering · mentoring, code reviews, cross-functional coordination in large organizations

## PROFESSIONAL EXPERIENCE

### Staff AI/ML Software Engineer - under NDA

*March 2026 - present*; *München, Germany*

**Technologies:** Python, PyTorch, cuML, pandas, numpy, Anthropic SDK, LangChain, Claude Code, MCP

### Staff Software Engineer - [Helsing](https://helsing.ai/)

*October 2024 - February 2026*; *München, Germany*

Worked with research scientists on productization of a computer vision and telemetry pipeline for defense applications, with focus on system integration, profiling and optimization. Highlights:

- Optimized the computer vision processing pipeline to operate at 2.8x of the original framerate.
- Integrated the pipeline with telemetry acquisition, actuation, as well as safety harness and overrides - making it part of a product.
- Implemented the ETL pipeline and introduced automated regression monitoring of algorithm performance metrics - allowing the team to visualize trends and catch regressions early.

**Technologies:** Rust, Python, Bash, perf, pprof, TensorRT, GitLab CI, Plotly, pandas, numpy, protobuf, Neptune, Grafana, Claude Code, LangChain, MCP

**Reference letter:** available upon request

### Staff AI Software Engineer - [Paige](https://paige.ai/)

*April 2022 - July 2024*; *München, Germany*

Drove the full lifecycle of AI/ML clinical cancer diagnostics products, from research to production, and developed the AI/ML tooling and infrastructure behind it. Highlights:

- Released models spanning tissue types (e.g. prostate, breast, colon) and covering cancer detection, classification and segmentation - in compliance with FDA/CE-IVDR/ISO regulations; collaborated on the Virchow pathology foundation model and its release as the pan-cancer detection product.
- Transformed packaging of trained models from a manual, multi-sprint, team-wide process into a one-day, single-engineer operation, through implementation of templating for configuration of model inference and transformations of its outputs - which scaled teams to more products.
- Orchestrated experiments and model training (Prefect, Slurm) across an on-prem cluster (DGX nodes with A100/V100 GPUs) alongside data scientists.
- Profiled and resolved computational performance and memory issues from training to production inference; optimized inference on AWS T4 instances with model compilation (TensorRT), reducing latency and cutting the operational costs by 15%.
- Promoted in 2023 to team lead of the cross-functional clinical product team of 5 engineers and scientists (coordinating with medical, UX and frontend, infrastructure and regulatory staff); mentored engineers (e.g. best practices, CI/CD use, idiomatic Python) and ran code reviews.
- Automated regulatory acceptance tests across teams, eliminating error-prone manual release tasks.
- Built an LLM-assisted data labeling workflow, maintained shared ML libraries, improved collection and visualization of metrics.
- Collaborated with major pharma partners on research related to biomarker detection.

**Technologies:** Python, PyTorch, PyTorch Profiler, cuML, scikit-learn, pandas, numpy, mprof, TensorRT, Docker, GitLab CI (later migrated to GitHub Actions), Artifactory, wandb, Gradio, FastAPI, DataDog, Grafana, AWS (EC2, S3, IAM), Prefect, SLURM

**Links:** [Virchow foundation model on Hugging Face](https://huggingface.co/paige-ai/Virchow2)

**Reference letter:** [Christina Segro](https://drive.google.com/file/d/14PnujOmryrHBF8FR2tbL7sZCFBzRaIDa/view) - General Counsel

### Principal/Senior Software Engineer - [ams OSRAM](https://ams-osram.com/)

*April 2018 - March 2022*; *München, Germany*

Lead software engineer in the Fluence unit of OSRAM, on the Smart Farming team tasked with digitization of vertical farming and greenhouse operations. Highlights:

- In the Senior role, I led a team of 3 who developed a Node.js/Electron app, and I implemented a CLI in Go (open-sourced) for PHYTOFY research light control - used by e.g. NASA, 3rd-party (climate chamber) integrators, the Customer Cultivation Support Lab, a factory for system test automation.
- Advised the CEO office on 3rd-party partner and systems selection in merger/acquisition projects.
- Automated lab & testbed sites operations (secure remote access for telemetry and control, etc.).
- Promoted to the Principal role, I led a team of 9 engineers while also engineering critical paths. The team developed, launched and operated a multi-tenant IIoT platform on AWS, tailored to operating indoor / greenhouse plant production, integrating 3rd-party vendors for lighting actuation scheduling and sensor data acquisition. The platform also featured production status dashboards, alerts and notifications, as well as decision-support tools leveraging satellite-based climate lighting models. This covered: cloud infrastructure, backend services, web frontend and mobile app.
- Mentored the broader engineering team, raised the engineering bar and enabled transition from PoCs to launched products: rollout of CI/CD build and deployment automation, AWS best practices, introduction of postmortems for production issues, UX harmonization across frontends, unification of roadmap and prioritization of backlog items to improve team's coordination, integration with enterprise security scanning infrastructure, as well as migration of the time-series database to a managed service to unblock scaling issues and improve the cost-effectiveness.

**Technologies:** Python, Go, AWS (ECS, ECR, SQS, RDS, SNS, WorkMail, Cognito, Lambda, API Gateway, EB, EFS, EC2, CloudFormation, CloudWatch), Azure (AKS, Azure Active Directory, Azure Blob Storage), Kubernetes, Docker, Terraform, Bitbucket Pipelines, GitHub Actions, PostgreSQL, TimescaleDB, Redis, FastAPI, Plotly, TypeScript, Vue, Vuetify

**Links:** [PHYTOFY at NASA](https://youtu.be/bSFfbB5mT-o)

**Reference letter**: [Timo Bongartz](https://drive.google.com/file/d/1m2mDOi7TUNZDttUs_mprnTVC9Vldvnig/view) - EMEA Head of Fluence by OSRAM

### Senior Software Engineer (Dev Tools) - [Huawei](https://www.huawei.com/)

*March 2017 - March 2018*; *München, Germany*

Senior member of the Testing and Reliability Engineering team tasked with development of the software engineering tools used by the mobile and cloud business units to accelerate their work and improve the quality of their output. Highlights:

- Implemented microservices for the Huawei-internal cloud-native IDE, e.g.: single sign-on integration, services for software testing and static code analysis; optimized the platform for short start-up time and low resource consumption.
- Introduced CI/CD automation to the team, dockerized the testing environment, automated all unit and end-to-end tests, along with the platform builds and deployment of the CI/CD runners.
- Led a team of 4 external contractors and coordinated with a wider distributed Huawei team.

**Technologies:** Python, JavaScript, Go, Bash, Docker, Linux, GitLab CI, CI/CD, Ansible, Java, pytest

**Reference letter:** [Nokhaz Yaqub](https://drive.google.com/file/d/1qFYgkJPeczUuLbjvT2_P-L6bQUbXbFVc/view) - Technical Director for the Testing and Reliability Engineering Center

### Software Engineer and Research Scientist - [Philips](https://www.philips.com/)

*May 2005 - February 2017*; *Eindhoven, The Netherlands*

Engineered new Philips products and services, initially for consumer electronics and video streaming, later for personal fitness and healthcare. Projects combined various languages, technologies, and spanned from resource-constrained IoT devices to backend/cloud platforms. Highlights:

- Developed custom tools for performance profiling which allowed me to optimize the cache memory and memory bus bandwidth footprint of an H.264 decoder on a multicore DSP CPU.
- Implemented temporal scalability QoS techniques (for Linux kernel and userspace) for streaming of (encrypted) H.264 video, used in STB810 set-top-box and VP5500 VoIP phone.
- Prototyped an OpenGL transcoder for the cloud gaming Games@Large EU project.
- Optimized frame buffer access in a specialized LED display (Lumalive) raising framerate by an order of magnitude (and enabling video playback).
- Implemented social features for the DirectLife fitness tracking cloud service and created prototypes for monitoring of all pillars of physical fitness.
- Implemented the software (C on MSP430 and ARM Cortex M0; Python services on GCP) for the Lifeline GoSafe personal emergency response system (incl. connectivity and location positioning). Later replicated the functionality as an Android app in a hackathon challenge.
- Designed and implemented a fall prevention system - coupling an AWS-deployed ML model with telemetry from GoSafe wearables, through a bespoke ETL pipeline (custom-designed compression & DSP preprocessing in Python) and event processing architecture. The system scaled cost-effectively to 100k+ production users.
- My responsibilities also included: technology evaluation and selection, IP creation and circumvention, acting as a Scrum master, mentoring of junior software engineers and PhD students, cooperation with EU projects and standardization bodies.

**Technologies:** C, Python, JavaScript, AWS (ECS, Lambda, API Gateway, SQS, S3, CloudWatch), GCP, Docker, numpy, GitLab CI, Linux, MySQL, ETL, MSP430, ARM, location positioning, TCP/IP

**Reference letter:** [Dr. Jörg Habetha](https://drive.google.com/file/d/1By3QR1zh2hZJozD9wbcvgPp2e-GGwvjp/view) - Personal Health Department Head

### Software Engineer and Project Leader - [Siemens](https://www.siemens.com/)

*November 2002 - July 2004*; *Wrocław, Poland*

Designed and developed the software for real-time metering and billing for telecommunication services (e.g. calls, SMS and mobile payments), integrated as a part of the Siemens 3G network control platform (used later in production by major mobile network operators). Highlights:

- Implemented custom Java serialization for a 2x performance improvement and stable operation.
- Built a specialized testing harness which reduced testing time by an order of magnitude.
- Extended testing harness with automatic conversion of fault logs to test cases.
- Led a team of 4 software engineers and testers; championed Agile development practices (e.g. short-cycle incremental planning, TDD, automation) prior to their widespread adoption.

**Technologies:** Java, Linux, Oracle Database

**Reference letter:** [Seweryn Krajewski](https://drive.google.com/file/d/1vGHlXgqhkMgBcvCsY59PsuL2zDawjuCe/view) - Department Manager


## EDUCATION

### Ph.D. student (left for Philips Research) - [RijksUniversiteit Groningen](https://www.rug.nl/)

*August 2004 - April 2005*; *Groningen, The Netherlands*

**Links:** [Dynamic Logic for Security - research proposal](https://www.cs.rug.nl/~grl/resproj/dylos.pdf)

### Master in Computer Science (M.Sc. honors) - [Wroclaw University of Technology](https://pwr.wroc.pl/)

*October 1997 - June 2002*; *Wrocław, Poland*

**Links:** [university transcripts](https://drive.google.com/file/d/1cZYAoD3jZDP8NkcD8pKR7jTxDZKVp5h_/view), [diploma](https://drive.google.com/file/d/1NRYuOZRb6r-1-Q7Tcax-pMLpwRYEikwR/view)

**Reference letters:** [Prof. Jerzy Kisilewicz](https://drive.google.com/file/d/1LNdBUWfoGesww-c7HHMZFg7s32URPquR/view) - Supervisor, [Prof. Andrzej Kasprzak](https://drive.google.com/file/d/1sMyZCZ4Yw3JOBDOHeTMWI9gv2fZYNRB8/view) - Advisor


## LANGUAGES

**Polish** native,
**English** fluent ([C1/C2](https://drive.google.com/file/d/1pKQZOM_w39EURcypCaU3uurhzbryZnuo/view)),
**Dutch** intermediate ([B2](https://drive.google.com/file/d/1LfgcwvuKa54zjyZGPeY0h4Lo3paRu0n4/view)),
**German** intermediate ([B1](https://results.telc.net/vb?credential=telc-IYbVvXS))


## PUBLICATIONS, PATENTS AND CERTIFICATIONS

- [Building with the Anthropic API](https://verify.skilljar.com/c/quv8w9xc35g7) incl. MCP, RAG (certificate; 2026)
- [Claude Code in Action](https://verify.skilljar.com/c/uc2uoce28xyj) by Anthropic (certificate; 2026)
- [Controlled Agricultural Systems and Methods of Managing Agricultural Systems](https://patents.google.com/patent/US20190259108A1) (invention; 2019)
- [Machine Learning](https://www.coursera.org/account/accomplishments/certificate/9D7SPM5ABRN4) by Stanford University (certificate; 2016)
- [Mobile help buttons with multiple location technologies](https://patents.google.com/patent/US20160094953A1) (invention; 2016)
- [Professional Scrum Master level I](https://www.scrum.org/User-Profile/userId/174800) (certificate; 2016)
- [A method of communicating information between nodes](https://www.google.com/patents/WO2013190415A2) (invention; 2013)
- ISO QMS and risk management - [14971](https://drive.google.com/file/d/1wiFbGbPZjK36LgXC8q5_FiN4u-YCOA0G/view), [13485:2003 and 14971:2009](https://drive.google.com/file/d/1rle_iuCptdx-SCbLiNdqRsbAQwojk9Ko/view) (certificates; 2009 and 2012)
- [Fitness test system](https://patents.google.com/patent/EP2324762A1) (invention; 2010)
- [Enabling Temporal Bit Rate Adaptation in Encrypted Video Streams](https://ieeexplore.ieee.org/document/5421797) (CCNC publication, IEEE; 2010)
- [Adaptive Streaming of Audio/Video Content over Wireless Networks](https://link.springer.com/chapter/10.1007/11907381_2) (MMNS publication; 2006)
