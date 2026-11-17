import os
from typing import Literal

import psycopg2
import psycopg2.extras
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@db:5432/fastapi_db"
)

app = FastAPI(title="FastAPI Calculator", version="1.0.0")


def query(sql: str, params: tuple = ()):
    """Run a raw SQL SELECT and return rows as dicts."""
    try:
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(sql, params)
                return cur.fetchall()
    except psycopg2.errors.UndefinedTable:
        raise HTTPException(
            status_code=404,
            detail="Tables not created yet - run sql/01_create_tables.sql in pgAdmin.",
        )
    except psycopg2.OperationalError as exc:
        raise HTTPException(status_code=503, detail=f"Database unavailable: {exc}")


class CalcRequest(BaseModel):
    a: float
    b: float
    operation: Literal["add", "subtract", "multiply", "divide"]


@app.get("/")
def root():
    return {"message": "FastAPI Calculator is running", "docs": "/docs"}


@app.get("/health")
def health():
    rows = query("SELECT version() AS postgres_version;")
    return {"status": "ok", "database": rows[0]["postgres_version"]}


@app.post("/calculate")
def calculate(req: CalcRequest):
    if req.operation == "add":
        result = req.a + req.b
    elif req.operation == "subtract":
        result = req.a - req.b
    elif req.operation == "multiply":
        result = req.a * req.b
    else:
        if req.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = req.a / req.b
    return {"a": req.a, "b": req.b, "operation": req.operation, "result": result}


@app.get("/users")
def list_users():
    return query("SELECT * FROM users ORDER BY id;")


@app.get("/calculations")
def list_calculations():
    return query(
        """
        SELECT u.username, c.id, c.operation, c.operand_a, c.operand_b, c.result
        FROM calculations c
        JOIN users u ON c.user_id = u.id
        ORDER BY c.id;
        """
    )
