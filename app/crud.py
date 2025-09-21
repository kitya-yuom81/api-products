from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session
from . import models, schemas

def create_product(db: Session, data: schemas.ProductCreate) -> models.Product:
    prod = models.Product(**data.dict())
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod

def get_product(db: Session, pid: int) -> models.Product | None:
    return db.get(models.Product, pid)

def list_products(
    db: Session,
    *,
    skip: int = 0,
    limit: int = 50,
    q: str | None = None,
    category: str | None = None,
    sort_by: str = "id",      # id | name | price | category
    order: str = "asc",       # asc | desc
) -> Sequence[models.Product]:
    stmt = select(models.Product)

    if q:
        like = f"%{q.lower()}%"
        stmt = stmt.where(models.Product.name.ilike(like))

    if category:
        stmt = stmt.where(models.Product.category == category)

    # sorting
    sort_col = getattr(models.Product, sort_by, models.Product.id)
    stmt = stmt.order_by(sort_col.desc() if order.lower() == "desc" else sort_col.asc())

    # pagination
    stmt = stmt.offset(skip).limit(limit)

    return db.execute(stmt).scalars().all()

def replace_product(db: Session, pid: int, data: schemas.ProductCreate) -> models.Product | None:
    prod = get_product(db, pid)
    if not prod:
        return None
    for k, v in data.dict().items():
        setattr(prod, k, v)
    db.commit()
    db.refresh(prod)
    return prod

def update_product(db: Session, pid: int, data: schemas.ProductUpdate) -> models.Product | None:
    prod = get_product(db, pid)
    if not prod:
        return None
    for k, v in data.dict(exclude_unset=True).items():
        setattr(prod, k, v)
    db.commit()
    db.refresh(prod)
    return prod

def delete_product(db: Session, pid: int) -> bool:
    prod = get_product(db, pid)
    if not prod:
        return False
    db.delete(prod)
    db.commit()
    return True
