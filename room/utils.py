from django.shortcuts import render, get_object_or_404

def detail_view(request, obj_id, obj_class, characters):
    class_name = obj_class.__name__.lower()
    obj = get_object_or_404(obj_class, id=obj_id)
    return render(request, 'detail.html', {class_name: obj, "characters":characters})