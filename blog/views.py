from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy

from blog.models import Courses, Courses1, Popcourses, Experts, Aboutus, Experts1, Testimonial
from .forms import ContactForms
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView

# Create your views here.

def index(request):
    course = Courses.objects.all()
    course1 = Courses1.objects.all()
    pcourse = Popcourses.objects.all()
    expert = Experts.objects.all()
    about = Aboutus.objects.all()
    testimon = Testimonial.objects.all()
    context = {
        "index": index,
        "about": about,
        "course": course,
        "course1": course1,
        "pcourse": pcourse,
        "expert": expert,
        "testimon": testimon

    }
    return render(request, "index.html", context=context)

def a404(request):
    context = {
        "a404": a404
    }
    return render(request, "a404.html", context=context)

def about(request):
    expert = Experts.objects.all()
    about = Aboutus.objects.all()
    context = {
        "expert": expert,
        "about": about,
    }
    return render(request, "about.html", context=context)

def contact(request):
    form = ContactForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")
    context = {
        "form": form,
    }
    return render(request, 'contact.html', context=context)

def courses(request):
    courses1 = Courses1.objects.all()
    course = Courses.objects.all()
    pcourse = Popcourses.objects.all()
    context = {
        "courses1": courses1,
        "course": course,
        "pcourse": pcourse
    }
    return render(request, "courses.html", context=context)

def team(request):
    expert1 = Experts1.objects.all()
    context = {
        "expert1": expert1
    }
    return render(request, "team.html", context=context)

def testimonial(request):
    testimon = Testimonial.objects.all()
    print("Malumot = ", testimon)
    context = {
        "testimon": testimon
    }
    return render(request, "testimonial.html", context=context)

def aboutdetailview(request, id):
    try:
        about = Aboutus.objects.get(id=id)
        context = {
            "about": about
        }
    except contact.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "about_detail.html", context=context)

def pcoursedetailview(request, id):
    try:
        pcourse = Popcourses.objects.get(id=id)
        context = {
            "pcourse": pcourse
        }
    except contact.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "pcourse_detail.html", context=context)

def pcourse1detailview(request, id):
    try:
        pcourse1 = Popcourses.objects.get(id=id)
        context = {
            "pcourse1": pcourse1
        }
    except contact.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "pcourse1_detail.html", context=context)

class CoursesUpdateView(UpdateView):
    model = Courses
    fields = ('name', 'son', )
    template_name = 'coursesEdit.html'



def courseDetail(request, course):
    course = get_object_or_404(Courses, slug=course)
    context = {
        "course": course
    }
    return render(request, "courseDetail.html", context=context)

class CourseCreateView(CreateView):
    model = Courses
    template_name = "courseCreate.html"
    fields = ("name", "son", "slug")

class ExpertsUpdateView(UpdateView):
    model = Experts
    fields = ('name', 'bio', 'slug')
    template_name = 'ExpertsEdit.html'

class CoursesDeleteView(DeleteView):
    name = Courses
    template_name = 'coursesDelete.html'
    success_url = reverse_lazy('index')



















