from django.shortcuts import render
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from ai4bharat.transliteration import XlitEngine

class ApiErrorException(Exception):
    pass
        
class GetLanguageDetails(APIView):
    def get(self,request,language,word):
        try:
            if not language and word:
                raise ValueError("Language or word is not Entered")
            language = language
            language_input = XlitEngine(language)
            if not language_input:
                raise ValueError(f"Failed to Translate from English to {language}")
            word = word
            list_of_converted_words = language_input.translit_word(word, topk=5, beam_width=10)
            if not list_of_converted_words or len(list_of_converted_words) is None :
                raise ValueError("Aarrayconveter list is empty ")
            return Response(list_of_converted_words)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
