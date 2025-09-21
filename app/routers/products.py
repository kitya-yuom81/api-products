from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .. import schemas, crud
from ..deps import get_db, get_current_user

router = APIRouter(prefix="/products", tags=["products"])

@router.get("", response_model=List[schemas.ProductOut])
def list_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    q: str | None = Query(None, description="Search in name"),
    category: str | None = Query(None, description="Filter by category"),
    sort_by: str = Query("id", pattern="^(id|name|price|category)$"),
    order: str = Query("asc", pattern="^(asc|desc)$"),
    db: Session = Depends(get_db),
):
    return crud.list_products(
        db,
        skip=skip,
        limit=limit,
        q=q,
        category=category,
        sort_by=sort_by,
        order=order,
    )

@router.get("/{pid}", response_model=schemas.ProductOut)
def get_product(pid: int, db: Session = Depends(get_db)):
    prod = crud.get_product(db, pid)
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod

@router.post("", response_model=schemas.ProductOut, status_code=201)
def create_product(
    data: schemas.ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return crud.create_product(db, data)

@router.put("/{pid}", response_model=schemas.ProductOut)
def replace_product(
    pid: int,
    data: schemas.ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    prod = crud.replace_product(db, pid, data)
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod

@router.patch("/{pid}", response_model=schemas.ProductOut)
def update_product(
    pid: int,
    data: schemas.ProductUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    prod = crud.update_product(db, pid, data)
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod

@router.delete("/{pid}", status_code=204)
def delete_product(
    pid: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    ok = crud.delete_product(db, pid)
    if not ok:
        raise HTTPException(status_code=404, detail="Product not found")
    return None
