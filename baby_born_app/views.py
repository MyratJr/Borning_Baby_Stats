from django.shortcuts import render
from .models import*
from django.db.models import Q


nm = {
    1:"Ýanwar",
    2:"Fewral",
    3:"Mart",
    4:"Aprel",
    5:"Maý",
    6:"Iýun",
    7:"Iýul",
    8:"Awgust",
    9:"Sentýabr",
    10:"Oktýabr",
    11:"Noýabr",
    12:"Dekabr"
}


def index(request):
    a0 = Carousel.objects.last()
    a1 = Carousel.objects.filter(~Q(id=a0.id))[:10]
    context = {
        "a1" : a1,
        'a0' : a0
    }
    return render(request, "index.html", context)

def doctors(request, group):
    context = {}
    if group == "ahli":
        a1 = Doctor.objects.all()
        context["a2"] = "a2"
    elif group == "b1":
        a1 = Doctor.objects.filter(work_time=3)
        context["a3"] = 'a3'
    elif group == "b2":
        a1 = Doctor.objects.filter(work_time=1)
        context["a4"] = 'a4'
    elif group == "b3":
        a1 = Doctor.objects.filter(work_time=2)
        context["a5"] = 'a5'
    context["a1"] = a1
    return render(request, 'doctors.html', context)

def babies(request, type, id):
    context = {'nn':nm}
    if id > 0:
        if type == 'all':
            w1 = Baby.objects.filter(babydoctor=Doctor.objects.get(id=id)).select_related("gender", "babydoctor")
            context["w1"] = w1
            context["q1"] = "q1"
        elif type == "alive":
            w2 = Baby.objects.filter(is_alive=True, babydoctor=Doctor.objects.get(id=id)).select_related("gender", "babydoctor")
            context["w1"] = w2
            context["q2"] = 'q2'
        elif type == "not_alive":
            w3 = Baby.objects.filter(is_alive=False, babydoctor=Doctor.objects.get(id=id)).select_related("gender", "babydoctor")
            context["w1"] = w3
            context["q3"] = 'q3'
        context['lukman'] = id
    else:
        if type == 'all':
            w1 = Baby.objects.all().select_related("gender", "babydoctor")
            context["w1"] = w1
            context["q1"] = "q1"
        elif type == "alive":
            w2 = Baby.objects.filter(is_alive=True).select_related("gender", "babydoctor")
            context["w1"] = w2
            context["q2"] = 'q2'
        elif type == "not_alive":
            w3 = Baby.objects.filter(is_alive=False).select_related("gender", "babydoctor")
            context["w1"] = w3
            context["q3"] = 'q3'
        context['ahli'] = "ahli"
    return render(request, "services.html", context)


def hospital(request):
    a0 = Carousel.objects.last()
    a1 = Carousel.objects.filter(~Q(id=a0.id))[:10]
    context = {
        "a1" : a1,
        'a90' : a0,
        "r5" : "r5"
    }
    return render(request, "hospital.html", context)

def search(request):
    if request.method == "POST":
        got = request.POST.get('gozleg')
        s1 = Baby.objects.filter(surname__icontains=got)
        return render(request, "services.html", {"s1":s1, "nn":nm})