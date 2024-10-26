from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Many-to-One Relationship with Category
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, stock={self.stock})>"