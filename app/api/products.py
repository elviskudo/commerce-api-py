from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database
from app.schemas.product import ProductCreate
from app.models.product import Product
from app.utils import hash_password

router = APIRouter()

@router.post("/create", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(database.get_db)):
    db_product = Product(full_name=product.full_name, email=product.email, password=hash_password(product.password))
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product