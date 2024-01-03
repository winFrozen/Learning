from django.contrib import admin
from .models import Courses, Courses1, Popcourses, Experts, Aboutus, Experts1, Contact, Testimonial

# Register your models here.

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Courses1)
admin.site.register(Popcourses)
admin.site.register(Experts)
admin.site.register(Aboutus)
admin.site.register(Experts1)
admin.site.register(Contact)
admin.site.register(Testimonial)








