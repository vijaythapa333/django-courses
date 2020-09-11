from django.shortcuts import render, redirect
from .models import Course, Lecture, Enroll
from django.contrib import messages
from django.contrib.auth.decorators import login_required # for Access Control


# Create your views here.

def index(request):
    courses = Course.objects.filter(course_is_active='Yes')
    context = {
        'courses': courses,
    }
    return render(request, 'courses/index.html', context)


def courses(request):
    courses = Course.objects.filter(course_is_active='Yes')
    context = {
        'courses': courses,
    }
    return render(request, 'courses/courses.html', context)


def course_detail(request, course_slug):
    try:
        course = Course.objects.get(course_slug=course_slug)
        lectures = Lecture.objects.filter(course=course.id)

        # Check
        if request.user.is_authenticated:
            enrolled = Enroll.objects.filter(course=course, user=request.user)
        else:
            enrolled = None
        

        context = {
            'course': course,
            'lectures': lectures,
            'enrolled': enrolled,
        }
        return render(request, 'courses/course_detail.html', context)

    except:
        messages.error(request, "Course Does not Exist.")
        return redirect(index)


def lecture(request, course_slug):
    try:
        course = Course.objects.get(course_slug=course_slug)
        lectures = Lecture.objects.filter(course=course.id)
        first_lecture = Lecture.objects.filter(course=course.id)[:1]
        context = {
            'course': course,
            'lectures': lectures,
            'first_lecture': first_lecture,
        }
        return render(request, 'courses/lecture.html', context)

    except:
        messages.error(request, "Course Does not Exist.")
        return redirect(index)


def lecture_selected(request, course_slug, lecture_slug):
    try:
        course = Course.objects.get(course_slug=course_slug)
        lectures = Lecture.objects.filter(course=course.id)
        lecture_selected = Lecture.objects.get(lecture_slug=lecture_slug)
        context = {
            'course': course,
            'lectures': lectures,
            'lecture_selected': lecture_selected,
        }
        return render(request, 'courses/lecture_selected.html', context)

    except:
        messages.error(request, "Course Does not Exist.")
        return redirect(index)


@login_required(login_url='account_login')
def enroll(request, course_id):
    user = request.user
    course = Course.objects.get(id=course_id)

    try:
        Enroll.objects.create(user=user, course=course)
        messages.success(request, "Successfully enrolled to the Course.")
        return redirect(index)

    except:
        messages.error(request, "Couldn't Enroll to the course. Please try again later.")
        return redirect(index)


@login_required(login_url='account_login')
def enrolled_courses(request):

    try:
        courses = Enroll.objects.filter(user=request.user)
        context = {
            'courses': courses,
        }
        return render(request, 'courses/enrolled_courses.html', context)

    except:
        messages.error(request, "Couldn't Enroll to the course. Please try again later.")
        return redirect(index)
    

        

