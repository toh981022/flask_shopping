# flask関連のパッケージを取得
from flask import render_template, request, url_for, session, redirect, flash

# 「__init__.py」で宣言した変数appを取得
from admin import app

# Itemモデルを取得
from lib.models import Item, Category
from lib.models import Category

# SQLAlchemyを取得
from lib.db import db

# デコレーターに使用
from functools import wraps

# 商品一覧を表示
@app.route('/test_it')
def index():
  items = Item.query.order_by(Item.id.desc()).all()
  return render_template('item.html', items=items)

@app.route('/test_cate')
def category():
  category = Category.query.order_by(Category.id.desc()).all()
  return render_template('category.html', category=category)

@app.route('/test_it/<int:id>')
def show1(id):
  item = Item.query.get(id)
  return render_template('show1.html', item=item)

@app.route('/test_cate/<int:id>')
def show(id):
  category = Category.query.get(id)
  return render_template('show2.html', category=category)
