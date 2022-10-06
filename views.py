from django.http import HttpResponse

def Docker(request):
    return HttpResponse("""What is Docker?
    Docker makes development efficient and predictable Docker takes away...""")