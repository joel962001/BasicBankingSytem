from django.shortcuts import render,redirect
from .models import Customer,History
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def history(request):
    if request.method == 'GET':
        hist=History.objects.filter().order_by('-timestamp')
        return render(request,'history.html',{'hist':hist})    


def tp(request):
    list = Customer.objects.all()
    res_dict = {'list': list}
    return render(request,'tp.html',context=res_dict)

def new(request):
    list = Customer.objects.all()
    res_dict = {'list': list}
    return render(request,'new.html',context=res_dict)


def transaction(request,sr_no):
    print(sr_no)
    data=Customer.objects.filter(sr_no=sr_no)
    all=Customer.objects.all()

    if request.method == 'GET':
        return render(request,'new.html',{'data':data,'all':all}) 
    
    if request.method == 'POST':
        r_acc = int(request.POST['reciever'])
        r_amt = request.POST['amt']
        
        sender=Customer.objects.get(sr_no=sr_no)
        sender_id = int(sender.sr_no)
        sender_name = str(sender.name)
        sender_acc = int(sender.acc_no)
        b=sender.balance

        try:
            check_acno=Customer.objects.get(acc_no=r_acc)
        except:
            return render(request,'new.html',{'customer':sender,'invalid_account':1,'cur_cust_id':r_acc,'data':data})
        
        x1=check_acno.acc_no
        n=check_acno.name

        if sender_acc == check_acno.acc_no:
            return render(request,'new.html',{'customer':sender,'sameuser':1,'curr_cust_id':r_acc,'data':data})
        
              

        if int(r_amt)>int(b):
            return render(request,'new.html',{'customer':sender,'insufficientbalance':1,'curr_cust_id':r_acc,'data':data})  

        sender.balance=sender.balance -int(r_amt)
        sender.save()
        check_acno.balance=check_acno.balance+int(r_amt)
        check_acno.save()

        History(sender=sender_name,  reciever=str(n),amount=int(r_amt)).save()
       
        return render(request,'new.html',{'customer':sender,'success':1,'curr_id':r_acc,'data':data}) 