import time
from random import choice

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# create PostgreSQL engine
engine = create_engine('postgresql://username:password@hostname:5432/database')

# create session to interact with database
Session = sessionmaker(bind=engine)
session = Session()

# create base class for declarative models
Base = declarative_base()


# tables declaration
class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    address = Column(String(200))
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    orders = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    order_date = Column(Date)
    total_amount = Column(Numeric(10, 2))
    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem")

    @classmethod
    def get(cls, order_id):
        return session.query(cls).get(order_id)

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        session.commit()

    @classmethod
    def bulk_update(cls, data):
        session.execute(update(cls), data)
        session.commit()


class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(100))
    products = relationship("Product")


class Supplier(Base):
    __tablename__ = 'suppliers'
    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String(100))
    supplier_email = Column(String(100))
    supplier_phone = Column(String(20))
    supplier_address = Column(String(200))


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    description = Column(String(500))
    price = Column(Numeric(10, 2))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    category = relationship("Category")

    @classmethod
    def list(cls):
        return session.query(cls).all()


class OrderItem(Base):
    __tablename__ = 'order_items'
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity = Column(Integer)
    price = Column(Numeric(10, 2))
    order = relationship("Order")
    product = relationship("Product")

    @classmethod
    def list_distinct(cls):
        return session.query(cls).distinct().all()

    @classmethod
    def bulk_insert(cls, lst):
        session.bulk_save_objects(lst)
        session.commit()


# create tables if not exists
Base.metadata.create_all(engine)


def insert_order_items():
    orders_to_add = []
    orders_to_update = []
    all_products = Product.list()

    # Existem 9994 orders na tabela
    for order_id in range(1, 9995):
        number_products = choice(range(1, 10))
        used_products = []
        for _ in range(0, number_products + 1):
            # Existem 1232 products na tabela
            product_id = choice(range(1, 1232))
            while product_id in used_products:
                product_id = choice(range(1, 1232))
            used_products.append(product_id)

        temp_amount = 0
        for p in used_products:
            prod = list(filter(lambda x: x.product_id == p, all_products))[0]
            order_item = OrderItem()
            order_item.order_id = order_id
            order_item.product_id = prod.product_id
            order_item.quantity = choice(range(1, 10))
            order_item.price = prod.price
            orders_to_add.append(order_item)
            temp_amount += (order_item.price * order_item.quantity)

        order = {"order_id": order_id, "total_amount": temp_amount}
        orders_to_update.append(order)

    # insert data on order_items table
    OrderItem.bulk_insert(orders_to_add)

    # update field total_amount of orders table
    Order.bulk_update(orders_to_update)


if __name__ == '__main__':
    start = time.monotonic()
    insert_order_items()
    print(time.monotonic() - start)
    exit(0)
