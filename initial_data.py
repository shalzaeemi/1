import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from inventory.models import Category, Product, Stock, GoldPrice
from decimal import Decimal

def create_initial_data():
    # إنشاء الفئات
    categories = {
        'ذهب': Category.objects.create(name='ذهب', description='منتجات الذهب بمختلف العيارات'),
        'مجوهرات': Category.objects.create(name='مجوهرات', description='مجوهرات وإكسسوارات'),
        'ألماس': Category.objects.create(name='ألماس', description='مجوهرات الألماس'),
    }
    
    # إنشاء المنتجات
    products = [
        {
            'name': 'ذهب عيار 21',
            'category': categories['ذهب'],
            'code': 'G21-001',
            'karat': 21,
            'weight': Decimal('10.000'),
            'making_charge': Decimal('50.00'),
            'price': Decimal('2150.00'),
            'description': 'ذهب عيار 21 - نقاء 875',
        },
        {
            'name': 'ذهب عيار 18',
            'category': categories['ذهب'],
            'code': 'G18-001',
            'karat': 18,
            'weight': Decimal('15.000'),
            'making_charge': Decimal('45.00'),
            'price': Decimal('1850.00'),
            'description': 'ذهب عيار 18 - نقاء 750',
        },
        {
            'name': 'خاتم ألماس',
            'category': categories['ألماس'],
            'code': 'D18-001',
            'karat': 18,
            'weight': Decimal('3.500'),
            'making_charge': Decimal('200.00'),
            'price': Decimal('4200.00'),
            'description': 'خاتم ألماس عيار 18 - وزن الألماس 0.5 قيراط',
        },
        {
            'name': 'سوار ذهب',
            'category': categories['مجوهرات'],
            'code': 'J21-001',
            'karat': 21,
            'weight': Decimal('12.500'),
            'making_charge': Decimal('75.00'),
            'price': Decimal('3500.00'),
            'description': 'سوار ذهب عيار 21 مع تصميم عصري',
        },
    ]
    
    # إنشاء المنتجات والمخزون
    for product_data in products:
        product = Product.objects.create(**product_data)
        Stock.objects.create(
            product=product,
            quantity=50,
            min_quantity=10
        )
    
    # إنشاء أسعار الذهب
    gold_prices = [
        {'karat': 18, 'price_per_gram': Decimal('185.00')},
        {'karat': 21, 'price_per_gram': Decimal('215.00')},
        {'karat': 24, 'price_per_gram': Decimal('245.00')},
    ]
    
    for price_data in gold_prices:
        GoldPrice.objects.create(**price_data)

if __name__ == '__main__':
    # مسح البيانات القديمة
    Category.objects.all().delete()
    Product.objects.all().delete()
    Stock.objects.all().delete()
    GoldPrice.objects.all().delete()
    
    # إنشاء البيانات الجديدة
    create_initial_data()
