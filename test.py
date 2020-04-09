# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    :  2020/4/8 15:53
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""


from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('oracle://tianjin:tianjin@Tj307440205@127.0.0.1:1521/orcl', echo=True)
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
Base.metadata.drop_all()
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')

session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
