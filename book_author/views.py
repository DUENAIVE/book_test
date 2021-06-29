from django.shortcuts import render, redirect
from django.views.generic.base import View
from utils.restful import *

from .models import *

class AuthorView(View):
    def get(self,request):
        '''
           :method get:
           :param: {"Name":"西门吹雪"}
           
        '''

        param_dict = request.GET.dict()

        author = Author.objects.filter(Name=param_dict['Name'])[0]
        print(author.Born_Date)
        return response_succeed(count=0)

    def post(self,request):
        '''
           :method post:
           :param: {"Name":"西门吹雪","Gender":1,"Born_Date":"2021-11-04"}

        '''

        param_dict =  request.POST.dict()

        try:
            author = Author(**param_dict)
            author.save()
            return response_succeed(count=0)
        except:
            return response_error(count=0)



class BookView(View):
    def get(self, request):
        '''
       :method get:
       :param: {"BookName":"三国演义"}

    '''

        param_dict = request.GET.dict()
        book_name = param_dict['BookName']
        print(book_name)
        book = Book.objects.filter(BookName=book_name)[0]
        print(book.Publish_Date)
        return response_succeed(count=0)
    def post(self, request):
        '''
                   :method post:
                   :param: {"Author":"1","BookName":"三国演义","Publish_Date":"2021-11-04","Country":"1"}

                '''

        param_dict = request.POST.dict()

        author = Author.objects.filter(id=param_dict['Author'])[0]

        param_dict['Author'] = author


        try:
            book = Book(**param_dict)
            book.save()
            return response_succeed(count=0)
        except Exception as e:
            print(e)

            return response_error(count=0)
