from django.shortcuts import render


# def upload_file_view(request):
# 	form = CsvModelForm(request.POST or None, request.FILES or None)
# 	if form.is_valid(): 	
# 		form.save()
# 		form = CsvModelForm()
# 		obj = Csv.objects.get(activated=False)
# 		with open(obj.file_name.path, 'r') as f:
# 			reader = csv.reader(f)
# 			for i, row in enumerate(reader):
# 				if i==0:
# 					pass
# 				else:
# 					datetime_obj = parser.parse(row[8])						
# 					conductor_sales_report.objects.create(
# 						company_id	= int(row[0]),
# 						company_name = row[1],	
# 						device	= row[2],
# 						conductor_id = int(row[3]),	
# 						conductor_first_name = row[4],
# 						conductor_last_name = row[5],
# 						number	= int(row[6]),
# 						amount	= row[7],
# 						date = datetime_obj,
# 					)
					
# 			obj.activated = True
# 			obj.save()
# 			#  index  upload
# 	return render(request, 'conductor_sales_report.html', {'form': form})

def home_view(request):
    return render(request, 'home.html',)
