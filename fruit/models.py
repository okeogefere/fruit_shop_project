from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from users.models import User




# Create your models here.
STATUS_CHOICE = (
    ('process', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    
)

STATUS = (
    ('draft', 'draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in review', 'In Review'),
    ('published', 'published'),
    
)
RATING = (
    ('1', '★☆☆☆☆'),
    ('2', '★★☆☆☆'),
    ('3', '★★★☆☆'),
    ('4', '★★★★☆'),
    ('5', '★★★★★'),
)

QUALITY = (
    ('Organic', 'Organic'),
    ('Non-Organic', 'Non-Organic'),
    ('Other', 'Other'),
)

CHECK_STATUS = (
    ('Healthy', 'Healthy'),
    ('Not Healthy', 'Not Healthy'),
    ('Other', 'Other'),

)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename) 


class Category(models.Model):
    cid = ShortUUIDField(
        unique=True, length=10, max_length=30, 
        prefix="cat", alphabet='abcdefghijk1234567890')
    title = models.CharField(max_length=200, default='cloths')
    image = models.ImageField(upload_to="category", default='category.jpg')

    class Meta:
        verbose_name_plural = 'Categories'


    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title



class Product(models.Model):
    pid = ShortUUIDField(
    unique=True, length=10, max_length=30, 
    prefix="prd", alphabet='abcdefghijk1234567890')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    title = models.CharField(max_length=200, default='Apple')

    image = models.ImageField(upload_to="user_directory_path", default='product.jpg')
    description = models.TextField(null=True, blank=True, default='This is an amazing fruit')
    country = models.CharField(max_length=200, default='Canada', null=True, blank=True)

    weight = models.DecimalField(max_digits=9999999999, decimal_places=2, default='1.00')
    max_weight = models.DecimalField(max_digits=999999999, decimal_places=2, default='2.00')
    quality = models.CharField(choices=QUALITY, max_length=200, default='None')
    check_status = models.CharField(choices=CHECK_STATUS, max_length=200, default='None')

    price = models.DecimalField(max_digits=9999999999, decimal_places=2, default='1.00')
    old_price = models.DecimalField(max_digits=9999999999, decimal_places=2, default='2.00')

    
        
    product_status = models.CharField(choices=STATUS, max_length=200, default='in_review')

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Products'


    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    

################################################### cart ###################################################
    
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999, decimal_places=2, default='1.00')
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default='processing')

    class Meta:
        verbose_name_plural = 'Cart Order'



class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)

    #product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999, decimal_places=2, default='1.00')
    total = models.DecimalField(max_digits=9999999999, decimal_places=2, default='1.00')

    
    class Meta:
        verbose_name_plural = 'Cart Order Items'
    
    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    


################################################### product review ###################################################
    
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'

    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating