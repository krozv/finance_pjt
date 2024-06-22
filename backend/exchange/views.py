from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
import requests

@api_view(['GET'])
def currency_converter(request):
    try:
        base_currency = request.query_params.get('base_currency', 'USD')
        target_currency = request.query_params.get('target_currency', 'KRW')
        amount = float(request.query_params.get('amount', 1.0))

        today = datetime.datetime.now()
        if today.weekday() >= 5:
            diff = today.weekday() - 4
            today = today - datetime.timedelta(days=diff)

        today = today.strftime('%Y%m%d')
        auth = 'xGFUFeb5zQ169d3eofGEw87VEx7QiixQ'
        url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={auth}&searchdate={today}&data=AP01'

        res = requests.get(url)
        data = res.json()
        
        base_rate = None
        target_rate = None

        for d in data:
            if d['cur_unit'] == base_currency:
                base_rate = float(d['tts'].replace(',', ''))
            if base_currency == 'KRW':
                base_rate = 1000.0
            
            if d['cur_unit'] == target_currency:
                target_rate = float(d['tts'].replace(',', ''))
            if target_currency == 'KRW':
                target_rate = 1000.0

        if base_rate and target_rate:
            conversion_rate = target_rate / base_rate
            converted_amount = amount * conversion_rate
            return Response({'base_currency': base_currency, 'target_currency': target_currency, 'amount': amount, 'converted_amount': converted_amount})

        return Response({'error': '환율 정보를 찾을 수 없습니다.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)