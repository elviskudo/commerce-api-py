from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    
    # One-to-Many Relationship with Product
    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(name={self.name})>"