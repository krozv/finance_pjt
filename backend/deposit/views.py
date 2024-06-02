from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from .models import DepositProduct, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
import requests



@api_view(['POST'])
def save_deposit_products(request):
    if request.method == 'POST':
        auth_key = "f5cd05f62e937d51a7e476e4315184e6"
        page_no = 1
        url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={auth_key}&topFinGrpNo=020000&pageNo={page_no}"

        response = requests.get(url)
        data = response.json()

        base_list = data.get('result', {}).get('baseList', [])
        option_list = data.get('result', {}).get('optionList', [])

        for item in base_list:
            if not DepositProduct.objects.filter(fin_prdt_nm=item['fin_prdt_nm']).exists():
                serializer = DepositProductsSerializer(data=item)
                if serializer.is_valid():
                    product = serializer.save()
                    # Save associated options
        for option_item in option_list:
            product = get_object_or_404(DepositProduct, fin_prdt_cd=option_item['fin_prdt_cd'])
            if not DepositOptions.objects.filter(
                intr_rate_type_nm=option_item['intr_rate_type_nm'],
                save_trm=option_item['save_trm'],
                fin_prdt_cd=option_item['fin_prdt_cd']
            ).exists():
                option_serializer = DepositOptionsSerializer(data=option_item)
                if option_serializer.is_valid():
                    option_serializer.save(product=product)
                else:
                    return Response(option_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Deposit products saved successfully.", status=status.HTTP_201_CREATED)

@api_view(['GET'])
def search_deposit_product(request):
    products = DepositProduct.objects.all()
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)