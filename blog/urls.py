from django.urls import path
from .views import index, about, contact, testimonial, team, courses, aboutdetailview, a404, pcoursedetailview, \
    pcourse1detailview, CoursesDeleteView, CoursesUpdateView, courseDetail, CourseCreateView, ExpertsUpdateView

urlpatterns = [
    path("index/", index, name='index'),
    path("a404/", a404, name='a404'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("courses/", courses, name='courses'),
    path("team/", team, name='team'),
    path("testimonial/", testimonial, name='testimonial'),
    path("about/<int:id>", aboutdetailview, name='about_detail_view'),
    path("pcourse/<int:id>", pcoursedetailview, name='pcourse_detail_view'),
    path("pcourse1/<int:id>", pcourse1detailview, name='pcourse1_detail_view'),
    path('course/edit/<slug>/', CoursesUpdateView.as_view(), name="courseUpdate"),
    path('course/delete/<slug>/', CoursesDeleteView.as_view(), name="courseDelete"),
    path('course/<slug:course>', courseDetail, name='coursedetail'),
    path("course/create", CourseCreateView.as_view(), name="courseCreate.html"),
    path('expert/edit/<slug>/', ExpertsUpdateView.as_view(), name="expertUpdate"),




]