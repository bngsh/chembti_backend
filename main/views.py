from django.shortcuts import render, redirect
from .models import Chembti, Question, Choice


def index(request):
    chembtis = Chembti.objects.all()
    totalCount = 0
    
    for chembti in chembtis:
        totalCount += chembti.count
    
    context = {
        'totalCount': totalCount,
    }
    
    return render(request, 'main/index.html', context=context)


def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions': questions,
    }
    
    return render(request, 'main/form.html', context)


def submit(request):
    queN = Question.objects.count()    
    typeScore = [0] * 8;    #einsftjp대로 index 0~7
    shift = 0
    chemCode = 0
    
    for q in range(1, queN+1):
        typeN = int(request.POST[f'question-{q}'][0])    #해당 질문의 선택된 mbtiType
        typeScore[typeN] += 1
    
    for k in range(4):
        shift = max(k<<1, (k<<1)+1, key = lambda x: typeScore[x])    #e=1, i=2, n=4, ..., 로 mbti 유형 비트마스킹
        chemCode += 1<<shift
    
    best_chembti = Chembti.objects.get(code=chemCode)
    best_chembti.count += 1
    best_chembti.save()
    
    context = {
        'chembti': best_chembti
        # 'chembti': chemCode
    }
    
    # return redirect(f'/result/{best_chembti.mbti}')
    return redirect('main:result', mbti=best_chembti.mbti)


def result(request, mbti):
    chembtis = Chembti.objects.all()
    totalCount = 0
    
    for chembti in chembtis:
        totalCount += chembti.count
    
    chembti = chembtis.get(mbti=mbti)
    
    match = chembtis.get(pk=chembti.data["matchmis"][0])
    
    if chembti.data["matchmis"][1] == 0:
        mismatch = chembti
    else:
        mismatch = chembtis.get(pk=chembti.data["matchmis"][1])
        
    proportion = float(chembti.count)/totalCount * 100
    
    context = {
        'chembti': chembti,
        'match': match,
        'mismatch': mismatch,
        'proportion': proportion,
    }
    
    return render(request, 'main/result.html', context)
