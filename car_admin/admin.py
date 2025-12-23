from django.contrib import admin
from car_admin.models import Service,Blog,Cat,Review,Centalfeatures,Centalprocess,Numbering,BookingForm


class ServiceAdmin(admin.ModelAdmin):
    list_display1=('ser_icon', 'ser_title', 'ser_desc')
admin.site.register(Service,ServiceAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display2=('blog_image','blog_date','blog_authorname','blog_comment','blog_title','blog_desc')
admin.site.register(Blog,BlogAdmin)

class CatAdmin(admin.ModelAdmin):
    list_display3=('cat_image','cat_title','cat_rate')
admin.site.register(Cat,CatAdmin)


class ReviewAdmin(admin.ModelAdmin):
     list_display=('review_image','review_title','review_icon','review_desc')
admin.site.register(Review,ReviewAdmin)

class CentalfeaturesAdmin(admin.ModelAdmin):
     list_display=('feat_icon','feat_title','feat_desc')
admin.site.register(Centalfeatures,CentalfeaturesAdmin)

class CentalprocessAdmin(admin.ModelAdmin):
     list_display=('pro_title','pro_number','pro_desc')
admin.site.register(Centalprocess,CentalprocessAdmin)

class NumberingAdmin(admin.ModelAdmin):
     list_display=('num_icon','num_counter','num_title')
admin.site.register(Numbering,NumberingAdmin)

class BookingFormAdmin(admin.ModelAdmin):
     list_display=('car_type','pickup_location','drop_location','pickup_date','pickup_time','drop_date','drop_time')
admin.site.register(BookingForm,BookingFormAdmin)



#  Register your models here.
