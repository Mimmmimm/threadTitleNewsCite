from django.shortcuts import render

# Create your views here.
import titleExtraction_from2ch
def titleExtraction():
    titleList = titleExtraction_from2ch.extraction()
    return titleList