# FastAPI User Service (Advanced Scaffold)

A production-style scaffold showing **FastAPI + async SQLAlchemy 2.0 + Alembic + Repositories + Services + DI + JWT Auth + Background Jobs + Http Clients**.

## Quickstart

1) Create and fill `.env` from `.env.example`:
```
cp .env.example .env
```

2) Create Postgres DB:
```
createdb fastapi_user_service
```

3) Install deps (uv, pip, or pipenv):
```
pip install -e .
```

4) Initialize DB schema (Alembic):
```
alembic upgrade head
```

5) Run:
```
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## Notes
- Uses **Pydantic v2**, **SQLAlchemy 2.x**, **Alembic**, **httpx**, **PyJWT**, **passlib**.
- Async DB via `asyncpg`.
- Soft-delete implemented. `restore` and `force-delete` endpoints included for Users.
- Background job sends "welcome" email through a generic `EmailHttpClient` (HTTP POST).

