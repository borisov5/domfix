from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from domfix.accounts.forms import UserEditForm, UserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserCreateForm
    add_form = UserEditForm
