import requests
from django.shortcuts import render, redirect, get_object_or_404
from conf.settings import secrets # setting에 import한 secrets를 불러옴
from .models import Shopping
from .forms import ShoppingForm

for secret, key in secrets.items():
    if secret == 'DJANGO_APP_KAKAOPAY_API_ADMIN_KEY':
        DJANGO_APP_KAKAOPAY_API_ADMIN_KEY = key         # kakao api admin code save

def home(request):
    if request.method == 'POST':
        check_form = ShoppingForm(request.POST) # form태그에서 전송된 정보 저장
        if check_form.is_valid():
            print("is_valid?")
            form = check_form.save(commit = False) # DB 저장은 보류
            form.total_amount = int(form.quantity) * int(form.item_price)
            form.save()

            URL = 'https://kapi.kakao.com/v1/payment/ready'
            headers = {
                "Authorization": "KakaoAK " + DJANGO_APP_KAKAOPAY_API_ADMIN_KEY,
                "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
            }
            params ={ 
                "cid": "TC0ONETIME", # 테스트용 제휴코드 
                "partner_order_id": form.id,     # 주문번호
                "partner_user_id": form.customer_name,    # 유저 아이디
                "item_name": form.item_name,        # 구매 물품 이름
                "quantity": form.quantity,                # 구매 물품 수량
                "total_amount": form.total_amount,        # 구매 물품 가격
                "tax_free_amount": form.tax_free_amount,         # 구매 물품 비과세
                "approval_url": "http://127.0.0.1:8000/approval", 
                "cancel_url": "http://127.0.0.1:8000/cancel", 
                "fail_url": "http://127.0.0.1:8000/fail", 
            }
            response = requests.post(URL, headers=headers, params=params)
            request.session['tid'] = response.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
            request.session['order_id'] = form.id      # 결제 승인시 사용할 order_id를 세션에 저장
            request.session['customer_name'] = form.customer_name      # 결제 승인시 사용할 customer_name을 세션에 저장
            # 정보를 웹 서버에 저장시켜둔다. cookie는 웹 브라우저에 저장하는 것. approval에서 사용함

            next_url = response.json()['next_redirect_pc_url']
            return redirect(next_url)
    else:
        form = ShoppingForm()
        context = {'form':form}
        return render(request, 'home.html', context)

def approval(request):
    if request.method == 'GET':
        order_id = request.session['order_id'] # 웹 서버에 저장시켜둔 id 저장
        shopped_history = get_object_or_404(Shopping, pk=order_id)
        shopped_history.is_complete = True # 해당 제품 구매 완료 처리
        shopped_history.save() # DB에 저장

        URL = 'https://kapi.kakao.com/v1/payment/approve'
        headers = {
            "Authorization": "KakaoAK " + DJANGO_APP_KAKAOPAY_API_ADMIN_KEY,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        params = { 
            "cid": "TC0ONETIME", # 테스트용 코드 
            "tid": request.session['tid'], # 결제 요청시 세션에 저장한 tid 
            "partner_order_id": order_id, # 주문번호 
            "partner_user_id": request.session['customer_name'], # 유저 아이디 
            "pg_token": request.GET.get("pg_token"), # 쿼리 스트링으로 받은 pg토큰 
        }
        response = requests.post(URL, headers=headers, params=params)
        amount = response.json()['amount']['total']
        context = {
            'response': response.json(), # 응답 객체를 json 파일 형태로 저장시킴
            'amount': amount
        }
        return render(request, 'approval.html', context)

def history(request): # 구매 리스트 함수
    # DB에 Shopping 목록을 미리 저장해야 함.
    histories = Shopping.objects.filter(is_complete=True).order_by("-shopped_date")
    context = {'histories':histories}
    return render(request, 'history.html', context)
