from django.shortcuts import render ,redirect
from .models import Employee_details
from .serializer import Employee_serialize

def add_data(request):
    if request.method == 'POST':
        data = request.POST
        emp_id = data.get('emp_id')
        emp_name = data.get('emp_name')
        emp_email = data.get('emp_email')
        emp_gender= data.get('emp_gender')
        emp_designation = data.get('emp_designation')
        
        emp_data  = Employee_details( emp_id =  emp_id , emp_name = emp_name , emp_email=emp_email, emp_gender=emp_gender ,emp_designation=emp_designation)
        emp_data.save()
        
    
    return render(request, 'insert.html')

def view_data(request):
    query_set = Employee_details.objects.all()
    serialize_data = Employee_serialize(query_set , many=True)
    context  = {"emp_details" : query_set}
    print('query_set: ',query_set)
    print('serialize_data: ' ,serialize_data.data)
    return render(request , 'show.html' , context)

def update_data(request ,id):
    if request.method == 'POST':
        query_set = Employee_details.objects.get(id = id)
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')
        emp_gender = request.POST.get('emp_gender')
        emp_designation = request.POST.get('emp_designation')

        query_set.emp_id = emp_id
        query_set.emp_name = emp_name
        query_set.emp_email = emp_email
        query_set.emp_gender = emp_gender
        query_set.emp_designation = emp_designation
        query_set.save()

    
    return render(request , 'update.html')  


def delete_data(request ,id):   
    query_set = Employee_details.objects.get(id = id)
    query_set.delete()
    return redirect('/')
      