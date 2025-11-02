from sqlalchemy import Column, Integer, String, Text, LargeBinary, DECIMAL, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import enum



class CoffeeStatus(enum.Enum):
    active = "active"
    inactive = "inactive"

class AddCoffee(Base):
    __tablename__ = "coffees"

    id = Column(String(50), primary_key=True, unique=True)
    aid = Column(Integer, ForeignKey("admin.aid", ondelete="CASCADE"))
    name = Column(String(100), nullable=False)
    description = Column(Text)
    image = Column(LargeBinary)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"))
    price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum("active", "inactive", name="coffee_status"), default="active")

    # ✅ Fix: define relationship back to Admin
    admin = relationship("Admin", back_populates="coffees")






