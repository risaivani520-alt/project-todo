from django.contrib import admin
from .models import Users,Todo


class UserAdmin(admin.ModelAdmin):
    user_details=['id','name','email','password']

admin.site.register(Users,UserAdmin)

class TodoAdmin(admin.ModelAdmin):
    todo_details=['sno','title','date']

admin.site.register(Todo,TodoAdmin)


    

