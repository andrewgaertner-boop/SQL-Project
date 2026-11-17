# Module 9 - Raw SQL in pgAdmin (FastAPI + PostgreSQL + pgAdmin)

## Services

| Service | URL / Port | Notes |
|---|---|---|
| FastAPI | http://localhost:8000 (docs at `/docs`) | Calculator + read-only DB endpoints |
| PostgreSQL | `localhost:5432` (host `db` inside Docker) | DB `fastapi_db`, user/password `postgres` |
| pgAdmin | http://localhost:5050 | No login needed (desktop mode) |

## Run

```bash
docker compose up -d --build
docker compose ps
```

## Register the server in pgAdmin

Right-click **Servers > Register > Server**:

- General > Name: `FastAPI Calculator DB`
- Connection > Host: **`db`** (not `localhost`), Port `5432`
- Maintenance database: `fastapi_db`, Username `postgres`, Password `postgres`

Open **Query Tool** on `fastapi_db` and run the scripts in `sql/` in order (`01` to `05`).

## Layout

```
docker-compose.yml  Dockerfile  requirements.txt
app/main.py         FastAPI app (raw SQL via psycopg2)
sql/                01_create_tables ... 05_delete_record
screenshots/        Evidence screenshots (numbered)
deliverables/       Report + reflection (DOCX and PDF)
tools/              Script that builds the deliverables
```

## Stop

```bash
docker compose down        # keep data
docker compose down -v     # also delete the database volume
```
