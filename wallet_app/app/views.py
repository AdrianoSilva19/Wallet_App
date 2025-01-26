from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .code.main import handle_pipeline
from .code.ETL.transform import Transformer
from .code.ETL.extract import Extractor
from django.views import View

# Create your views here.
@api_view(['GET'])
def get_whole_data(request):
    transformed_df = handle_pipeline()
    return Response(transformed_df)

@api_view(['GET'])
def get_wages_data(request):
    data_extractor = Extractor("app/data/")
    whole_dataframe = data_extractor.extract_general_xls()
    return Response(Transformer.extract_wages(whole_dataframe))

@api_view(['GET'])
def get_house_expenses(request):
    data_extractor = Extractor("app/data/")
    whole_dataframe = data_extractor.extract_general_xls()
    return Response(Transformer.extract_house_expenses(whole_dataframe))

@api_view(['GET'])
def get_fuel_expenses(request):
    data_extractor = Extractor("app/data/")
    whole_dataframe = data_extractor.extract_general_xls()
    return Response(Transformer.extract_fuel_expenses(whole_dataframe))

@api_view(['GET'])
def get_holidays_expenses(request):
    data_extractor = Extractor("app/data/")
    whole_dataframe = data_extractor.extract_general_xls()
    return Response(Transformer.select_holidays_expenses(whole_dataframe))

@api_view(['GET'])
def get_beverages_and_food(request):
    data_extractor = Extractor("app/data/")
    whole_dataframe = data_extractor.extract_general_xls()
    return Response(Transformer.extract_beverages_and_food(whole_dataframe))