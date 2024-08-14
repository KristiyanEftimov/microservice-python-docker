import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date, ForeignKey
from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

# Table for customers
customer = Table(
    'customer', metadata,
    Column('customer_id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('phone', String(20)),
)

# Table for vehicles
vehicle = Table(
    'vehicle', metadata,
    Column('vehicle_id', Integer, primary_key=True),
    Column('make', String(50)),
    Column('model', String(50)),
    Column('year', Integer),
    Column('license_plate', String(20)),
    Column('customer_id', Integer, ForeignKey('customer.customer_id')),
)

# Table for services
service = Table(
    'service', metadata,
    Column('service_id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('price', Float),
)

# Table for transactions
transaction = Table(
    'transaction', metadata,
    Column('transaction_id', Integer, primary_key=True),
    Column('vehicle_id', Integer, ForeignKey('vehicle.vehicle_id')),
    Column('service_id', Integer, ForeignKey('service.service_id')),
    Column('transaction_date', Date),
)

# Table for employees
employee = Table(
    'employee', metadata,
    Column('employee_id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('phone', String(20)),
)

# Table for shifts
shift = Table(
    'shift', metadata,
    Column('shift_id', Integer, primary_key=True),
    Column('employee_id', Integer, ForeignKey('employee.employee_id')),
    Column('start_time', Date),
    Column('end_time', Date),
)

# Table for promotions
promotion = Table(
    'promotion', metadata,
    Column('promotion_id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('description', String(255)),
    Column('discount', Float),
)

# Table for customers' memberships
membership = Table(
    'membership', metadata,
    Column('membership_id', Integer, primary_key=True),
    Column('customer_id', Integer, ForeignKey('customer.customer_id')),
    Column('start_date', Date),
    Column('end_date', Date),
)

database = Database(DATABASE_URI)
