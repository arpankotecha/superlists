from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from lists.models import Item, List

# Create your views here.
def home_page(request):
  return render(request, 'home.html')
# end

def view_list(request, list_id):
  list_ = List.objects.get(id=list_id)
  return render(request, 'list.html', {'list':list_})
# end

def new_list(request):
  list_ = List.objects.create()
  new_item_text = request.POST['item_text']
  item = Item(text=new_item_text, list=list_)
  try:
    item.full_clean()
    item.save()
  except ValidationError:
    list_.delete()
    error = "You can't have an empty list item"
    return render(request, 'home.html', {'error':error})
  return redirect('/lists/{}/'.format(list_.id))
# end

def add_item(request, list_id):
  list_ = List.objects.get(id=list_id)
  new_item_text = request.POST['item_text']
  Item.objects.create(text=new_item_text, list=list_)
  return redirect('/lists/{}/'.format(list_.id))
# end
