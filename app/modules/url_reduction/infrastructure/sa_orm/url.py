"""Модуль описания объектно-реляционной модели объекта информации оurl"""

from sqlalchemy import TEXT, VARCHAR, Column, Index, Integer

from app.database import Base
from .constant import URL_LONG_URL, URL_ROW_ID, URL_SHORT_URL


class Url(Base):
    """Класс описания объектно-реляционной модели объекта информации оurl"""

    __tablename__ = "url"

    id = Column(Integer, primary_key=True, comment=URL_ROW_ID)
    long_url = Column(TEXT, comment=URL_LONG_URL)
    short_url = Column(VARCHAR(16), comment=URL_SHORT_URL)


Index('url_short_url_idx', Url.short_url)
