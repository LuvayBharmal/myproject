from django.shortcuts import render
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from ai4bharat.transliteration import XlitEngine

class ApiErrorException(Exception):
    pass
            
class GetLangugeData(APIView):
    def get(self,request):
        try:
            laninp = input("Enter language: ")
            if not laninp:
                raise ApiErrorException("pls enter language name.")
            e = XlitEngine(laninp)
            word = input("Enter word: ")
            out = e.translit_word(word, topk=5, beam_width=10)
            return Response(out)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
