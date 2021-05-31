from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {
            'id': 1,
            'nome':'Luis Otávio Andrade',
            'idade':20
        }
        return JsonResponse(aluno)
