# M10 PMLS - Final Exam (Assignment)
## Productionization of ML Systems

Answers based on the course slides **M10 Unit 6 - Monitoring and Logging Models** and
**M10 Unit 7 - MLOps for Continuous Deployment and Monitoring**.

---

## Q1. Model Deployment

**Discuss different methods of model deployment in brief.**

A trained model only creates business value once it is made available to consumers (users,
applications, or other systems). There are several common ways to deploy a model, each suited to
a different scale and reliability requirement:

1. **Direct API deployment (Flask/FastAPI)**
   The model is wrapped in a lightweight web framework (e.g. FastAPI) that exposes it as a REST
   endpoint (`/predict`). Any client can send input data over HTTP and receive a prediction back
   in JSON. This is the fastest way to turn a trained model into a usable service and is the
   starting point of the ML lifecycle's "Deployment" stage.

2. **Containerized deployment (Docker)**
   The API, the model artifact, and all its dependencies are packaged into a Docker image - an
   immutable snapshot of the application and its environment. Running that image as a container
   guarantees the model behaves identically regardless of where it runs (a developer's laptop, a
   test server, or a cloud machine), removing "it works on my machine" issues.

3. **Orchestrated deployment (Kubernetes)**
   For production systems that need to handle variable traffic, containers are managed by an
   orchestrator such as Kubernetes, which provides auto-scaling (adding containers as load
   increases), load balancing (distributing requests across containers), and fault tolerance
   (automatically restarting failed containers).

4. **CI/CD-automated deployment**
   Continuous Integration validates code, data, and the model itself (unit tests, data
   validation, model validation) on every change; Continuous Deployment then automatically ships
   an approved model into production. This removes manual, error-prone release steps and reduces
   deployment risk.

5. **Registry-based staged deployment**
   A model registry stores trained models and their metadata and moves them through governed
   stages - **Development** (trained and logged) -> **Staging** (validated against held-out data)
   -> **Production** (approved, serving live traffic) -> **Archived** (retired but kept for
   audit). This gives traceability and an approval workflow before a model reaches real users.

In practice, these methods are combined: a model is served through FastAPI, packaged with
Docker, deployed and scaled with Kubernetes (if necessary), released through a CI/CD pipeline,
and governed through a model registry - together forming the "Deployment & Infrastructure" pillar 
of an MLOps architecture.

---

## Q2. Model Monitoring and Logging

**Explain the importance of model monitoring and logging.**

Training a model is only half the job - real-world data keeps changing, and model performance
can silently degrade in production without anyone noticing. *"If you don't monitor your model,
you don't control it."*

**Why monitoring matters**
- **Model drift**: performance degrades over time as the real world diverges from the training
  conditions. There are two types:
  - *Data drift* - the input data distribution changes (incoming features look statistically
    different from the training data).
  - *Concept drift* - the relationship between input and output changes (the patterns the model
    learned no longer hold), e.g. a fraud model trained on 2022 data failing to catch new 2025
    fraud patterns.
- **Failure modes that are otherwise invisible**: accuracy drops, input distribution shifts, API
  latency spikes or errors, unexpected/edge-case user inputs, and preprocessing pipeline
  mismatches between training and serving.
- **What should be monitored**: model performance metrics (accuracy, RMSE, F1), input data
  distribution, prediction output distribution, API metrics (latency, error rate, request
  volume), and system health (CPU, memory).
- **Monitoring drives retraining**: a model is retrained when accuracy falls below a threshold,
  significant drift is detected, or enough new data becomes available - keeping the model current
  (e.g. a credit scoring model retrained monthly on the latest customer data).

**Why logging matters**
Logging means recording the events that occur during model execution - request logs (who called
the API and when), prediction logs (inputs received and outputs returned), and error logs
(failures and exceptions). Logging is what makes debugging and auditing possible: *"you cannot
monitor what you have not logged."*

| Dimension  | Logging          | Monitoring            |
|------------|------------------|------------------------|
| Purpose    | Records events   | Tracks trends          |
| Use case   | Debugging        | Alerts & insights       |
| Data type  | Raw event data   | Aggregated metrics      |

Logging and monitoring are complementary: logs are the raw material, monitoring aggregates and
visualizes them to produce alerts and trend insights. Together they form the observability
pipeline of a production ML system (API layer -> logging layer -> storage -> dashboards &
alerts), typically implemented with tools such as Python's built-in `logging` module (or
structured logging inside FastAPI endpoints) for logs, and Prometheus, Grafana, the ELK stack,
or Evidently AI for metrics, dashboards, and drift detection.

**Bottom line**: a model that cannot be observed is a model that cannot be trusted. Monitoring
and logging are not optional extras - they are what keeps a deployed model reliable, auditable,
and correctable over its entire production lifetime.
