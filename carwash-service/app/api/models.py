from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True

class VehicleBase(BaseModel):
    make: str
    model: str
    year: int
    license_plate: str
    customer_id: int

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    pass

class VehicleOut(VehicleBase):
    vehicle_id: int

    class Config:
        orm_mode = True

class ServiceBase(BaseModel):
    name: str
    price: float

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(ServiceBase):
    pass

class ServiceOut(ServiceBase):
    service_id: int

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    vehicle_id: int
    service_id: int
    transaction_date: datetime

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    transaction_id: int

    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    employee_id: int

    class Config:
        orm_mode = True

class ShiftBase(BaseModel):
    employee_id: int
    start_time: datetime
    end_time: datetime

class ShiftCreate(ShiftBase):
    pass

class ShiftUpdate(ShiftBase):
    pass

class ShiftOut(ShiftBase):
    shift_id: int

    class Config:
        orm_mode = True

class PromotionBase(BaseModel):
    name: str
    description: Optional[str] = None
    discount: float

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(PromotionBase):
    pass

class PromotionOut(PromotionBase):
    promotion_id: int

    class Config:
        orm_mode = True

class MembershipBase(BaseModel):
    customer_id: int
    start_date: datetime
    end_date: datetime

class MembershipCreate(MembershipBase):
    pass

class MembershipUpdate(MembershipBase):
    pass

class MembershipOut(MembershipBase):
    membership_id: int

    class Config:
        orm_mode = True
