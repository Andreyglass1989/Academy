from django.shortcuts import render

#
# # def base(request):
# #     title = "Base"
# #     context = {
# #         "title_docum":title,
# #     }
# #     return render(request,"base.html",context)
#
#
# def base(request):
# 	staffs = Staff.objects.all()
# 	title = "Staff"
# 	context = {"title_docum":title, "staffs": staffs}
# 	return render(request,"base.html",context)

def winner(request):
    title = "winner"
    context = {
        "title":title,
    }
    return render(request,"winner.html",context)