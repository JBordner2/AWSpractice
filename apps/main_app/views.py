# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from models import Pet


def index(request):
        context = {
                "myPets" : User.objects.get(id = request.session['id']),
                "other_users" : User.objects.exclude(id = request.session['id']),
        }
        return render(request, "main_app/index.html", context)



###########################################################     Methods relating too pets       ######################################################
def addPet(request):
        return render(request, "main_app/addPet.html")


def createPet(request):
        results = Pet.objects.validate(request.POST)
        if len(results['errors']) > 0:
                for error in results['errors']:
                        messages.error(request, error)
                return redirect('/addPet')
        Pet.objects.create(name = request.POST['name'], kind = request.POST['kind'], owner = User.objects.get(id = request.session['id']))
        return redirect('/petApp')


def delete(request, id):
        Pet.objects.get(id = id).delete()
        return redirect('/petApp')


def show(request, id):
        context = {
                "user" : User.objects.get(id = id)
        }
        return render(request, "main_app/show.html", context)