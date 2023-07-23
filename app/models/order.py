import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, intpk, str128


class Order(Base):
    __tablename__ = "nimbbl_order"

    id: Mapped[intpk]
    merchant_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    sub_merchant_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    order_date: Mapped[datetime.datetime]
    order_id: Mapped[str128]
    amount_before_tax: Mapped[float]
    
    # access_key = Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    # access_secret = Mapped[str128]
    # access_secret_hash = Mapped[str128]
    # sub_merchant_id = Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    # active = Mapped[bool]
    # type = Mapped[str128]
    # token = Mapped[str] = mapped_column(String(256), index=True, unique=True)
    # token_expiration = Mapped[DateTime]
    # last_accessed_on = Mapped[DateTime]
    # number_of_token_per_minute = Mapped[int]

    # id = Column(Integer, primary_key=True)
    # merchant_id = Column(Integer, index=True, nullable=False)
    # sub_merchant_id = Column(Integer, index=True, nullable=False)
    # order_date = Column(DateTime(128))
    # order_id = Column(String(128))
    # amount_before_tax = Column(Float)
    # tax = Column(Float, default=0)
    # total_amount = Column(Float)
    # referrer_platform = Column(String(128))
    # referrer_platform_version = Column(String(128))
    # invoice_id = Column(String(128))
    # merchant_shopfront_domain = Column(String(128))
    # user_id = Column(Integer, index=True)
    # orignal_user_id = Column(Integer, index=True)
    # shipping_address_id = Column(Integer, index=True)
    # attempts = Column(Integer, index=True)
    # device_user_agent = Column(String(120))
    # status = Column(String(128))
    # order_from_ip = Column(String(128))
    # partner_id = Column(Integer, index=True)
    # max_retries = Column(Integer, default=15)
    # currency = Column(String(128))
    # description = Column(Text)
    # # order_metadata = Column(Text)
    # # custom_attributes = Column (Text)
    # callback_url = Column(Text)
    # callback_mode = Column(String(120))
    # cancellation_reason = Column(Text)
    # browser_name = Column(String(128), nullable=True)
    # device_name = Column(String(128), nullable=True)
    # os_name = Column(String(128), nullable=True)
    # fingerprint = Column(String(128), nullable=True)
    # checkout_status = Column(String(128))
    # additional_charges = Column(Float, default=0)
    # order_transac_type = Column(String(128))
    # grand_total_amount = Column(Float)
    # payment_link_id = Column(Integer, index=True)

    # # offer
    # offer_discount = Column(Float, default=0)
    # offer = Column(Integer, index=True)
    # transaction_card = Column(String(128))