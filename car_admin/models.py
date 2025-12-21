from django.db import models
class Service(models.Model):
    ser_icon=models.CharField(max_length=200)
    ser_title=models.CharField(max_length=200)
    ser_desc=models.TextField()

# Create your models here.

#  create numbering section 
class Numbering(models.Model):
    num_icon=models.CharField(max_length=200)
    num_counter=models.CharField(max_length=200)
    num_title=models.CharField()

# create cental process
class Centalprocess(models.Model):
    pro_title=models.CharField(max_length=200)
    pro_number=models.CharField(max_length=200)
    pro_desc=models.TextField()

#  create cental features
class Centalfeatures(models.Model):
     feat_icon=models.CharField(max_length=200)
     feat_title=models.CharField(max_length=200)
     feat_desc=models.TextField()

# create cental blog & News
class Blog(models.Model):
    blog_image=models.ImageField(upload_to='media/',blank=True, default='image/car-1.png')
    blog_date=models.DateField(max_length=200)
    blog_authorname=models.CharField(max_length=200)
    blog_comment=models.CharField(max_length=200)
    blog_title=models.CharField(max_length=200)
    blog_desc=models.TextField()

#  create vehicle categories
class Cat(models.Model):
     cat_image=models.ImageField(upload_to='media/',blank=True,null=True)
     cat_tilte=models.CharField(max_length=200)
     cat_rate=models.CharField(max_length=200)


#  create client review
class Review(models.Model):
      review_image=models.ImageField(upload_to='media/',blank=True, default='image/car-3.png')
      review_title=models.CharField(max_length=200)
      review_icon=models.CharField(max_length=200)
      review_desc=models.TextField()


    
