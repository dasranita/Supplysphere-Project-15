# SupplySphere — Project 15
Local educational manufacturing prototype. Next.js / Express / PostgreSQL / FastAPI.

## Run
Install Docker Desktop, then `docker compose up --build`. Open http://localhost:3000. API health: http://localhost:4000/health. Planning Swagger: http://localhost:8000/docs.

## Demo
Receive the seeded 100 steel units. Create a bracket work order (3 steel per bracket), reserve, produce, release quality hold, dispatch. Try reserving two orders of 30 brackets each: the second should fail. Duplicate receipts return a replay response. Inspect ledger and reservations.

## Architecture
Browser → Express → PostgreSQL. FastAPI is a separate stateless planning calculator. Redis is provisioned but unused. PostgreSQL conditional updates lock stock rows and transactions roll back all reservations on shortage. Work order row locks serialize state changes. Quality hold is represented by order state; finished stock is added only on release. Quantities use integer base units. This is not lot-level traceability.

## Tests
`docker compose run --rm planning pytest -q`; `node --check api/index.js`. The concurrency demo above is a manual test, not executed evidence.

## Limitations
No authentication or resource permissions; localhost only, synthetic data. No real supplier or shipping integrations, warehouse/bin management, batch-level allocation, BOM versioning, full analytics, automated concurrency tests or cloud deployment. Local database password is demo-only. Do not deploy publicly. See docs/assessment-status.md.
