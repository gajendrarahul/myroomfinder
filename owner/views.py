from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . form import AddRoomForm
from . models import Room


# Create your views here.
@login_required(login_url='login')
def ownerpage(request):
    context = {
        'room': Room.objects.all()
    }
    return render(request, 'ownerpage.html', context)


@login_required(login_url='login')
def addroom(request):
    if request.method == "GET":
        form = AddRoomForm()
        return render(request,'addroompage.html',{'form':form})
    else:
        form = AddRoomForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            data.owner_id = request.user.owner.id
            data.save()
            return redirect('ownerpage')
        else:
            return render(request, 'addroompage.html', {'form': form})