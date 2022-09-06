from django.shortcuts import render
from django.http import HttpResponse




# def error_400_view(request, exception):
# 	return render(request,'dashboard/400.html',  status=400)

# def error_403_view(request, exception):
# 	return render(request,'dashboard/403.html',  status=403)

def error_404_view(request, exception):
	return render(request,'dashboard/404.html',  status=404)

# def error_500_view(request):
# 	return render(request,'dashboard/500.html',  status=500)