from sqlalchemy import Column, Integer, String, Text, LargeBinary, DECIMAL, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import enum

class CartStatus(enum.Enum):
    small = "small"
    medium = "medium"
    large = "large"

class OrderItems(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    coffee_id = Column(String(50), ForeignKey("coffees.id"))
    size = Column(Enum(CartStatus), default=CartStatus.small)
    quantity = Column(Integer, nullable=False)