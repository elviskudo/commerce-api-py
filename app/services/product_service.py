from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate, ProductUpdate

class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_products(self):
        return self.db.query(Product).all()

    def get_product_by_id(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create_product(self, product: ProductCreate):
        new_product = Product(
            name=product.name,
            price=product.price,
            stock=product.stock,
            category_id=product.category_id
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def update_product(self, product_id: int, product_data: ProductUpdate):
        product = self.get_product_by_id(product_id)
        if not product:
            return None
        for key, value in product_data.dict(exclude_unset=True).items():
            setattr(product, key, value)
        self.db.commit()
        return product

    def delete_product(self, product_id: int):
        product = self.get_product_by_id(product_id)
        if not product:
            return None
        self.db.delete(product)
        self.db.commit()
        return True