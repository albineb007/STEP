from django.contrib import admin
from .models import User, Student, Parent


# Removed duplicate UserAdmin class here


from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from .models import User, Student, Parent


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "get_full_name",
        "username",
        "email",
        "is_active",
        "is_student",
        "is_lecturer",
        "is_parent",
        "is_staff",
        "reset_password_link",
    ]
    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_lecturer",
        "is_parent",
        "is_staff",
    ]

    class Meta:
        managed = True
        verbose_name = "User"
        verbose_name_plural = "Users"

    def reset_password_link(self, obj):
        from django.urls import reverse
        from django.utils.html import format_html
        url = reverse('admin:user_reset_password', args=[obj.id])
        return format_html('<a class="button" href="{}">Reset Password</a>', url)
    reset_password_link.short_description = 'Reset Password'
    reset_password_link.allow_tags = True

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:user_id>/reset_password/',
                self.admin_site.admin_view(self.reset_password_view),
                name='user_reset_password',
            ),
        ]
        return custom_urls + urls

    def reset_password_view(self, request, user_id):
        from django.shortcuts import get_object_or_404, render
        from django.contrib.auth.forms import AdminPasswordChangeForm
        from django.contrib.auth import update_session_auth_hash
        from django.http import HttpResponseRedirect
        from django.contrib import messages

        user = get_object_or_404(self.model, pk=user_id)

        if request.method == 'POST':
            form = AdminPasswordChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                self.message_user(request, 'Password changed successfully.', messages.SUCCESS)
                return HttpResponseRedirect(reverse('admin:accounts_user_change', args=[user_id]))
        else:
            form = AdminPasswordChangeForm(user)

        context = {
            'title': 'Reset password: {}'.format(user.username),
            'form': form,
            'user': user,
            'opts': self.model._meta,
            'original': user,
        }
        return render(request, 'admin/accounts/user/reset_password.html', context)


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "get_username",
        "get_email",
        "get_reset_password_link",
    ]

    def get_username(self, obj):
        return obj.student.username

    def get_email(self, obj):
        return obj.student.email

    def get_reset_password_link(self, obj):
        url = reverse('admin:student_reset_password', args=[obj.id])
        return format_html('<a href="{}">Reset Password</a>', url)

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:student_id>/reset_password/',
                self.admin_site.admin_view(self.reset_password_view),
                name='student_reset_password',
            ),
        ]
        return custom_urls + urls

    def reset_password_view(self, request, student_id):
        from django.shortcuts import get_object_or_404, render
        from django.contrib.auth.forms import AdminPasswordChangeForm
        from django.contrib.auth import update_session_auth_hash
        from django.http import HttpResponseRedirect
        from django.contrib import messages
        student = get_object_or_404(self.model, pk=student_id)
        user = student.student

        if request.method == 'POST':
            form = AdminPasswordChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                self.message_user(request, 'Password changed successfully.', messages.SUCCESS)
                return HttpResponseRedirect(reverse('admin:accounts_student_changelist'))
        else:
            form = AdminPasswordChangeForm(user)

        context = {
            'title': 'Reset password: {}'.format(user.username),
            'form': form,
            'student': student,
            'opts': self.model._meta,
            'original': student,
        }
        return render(request, 'admin/accounts/student/reset_password.html', context)

    get_reset_password_link.short_description = "Reset Password"


from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import path

class LecturerAdmin(admin.ModelAdmin):
    list_display = [
        "get_full_name",
        "username",
        "email",
        "is_active",
        "is_lecturer",
        "reset_password_link",
    ]
    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_lecturer",
    ]

    def reset_password_link(self, obj):
        from django.urls import reverse
        from django.utils.html import format_html
        if obj.is_lecturer:
            url = reverse('admin:lecturer_reset_password', args=[obj.id])
            return format_html('<a class="button" href="{}">Reset Password</a>', url)
        return ""
    reset_password_link.short_description = 'Reset Password'
    reset_password_link.allow_tags = True

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:lecturer_id>/reset_password/',
                self.admin_site.admin_view(self.reset_password_view),
                name='lecturer_reset_password',
            ),
        ]
        return custom_urls + urls

    def reset_password_view(self, request, lecturer_id):
        from django.shortcuts import get_object_or_404, render
        from django.contrib.auth.forms import AdminPasswordChangeForm
        from django.contrib.auth import update_session_auth_hash
        from django.http import HttpResponseRedirect
        from django.contrib import messages

        lecturer = get_object_or_404(self.model, pk=lecturer_id)
        user = lecturer

        if request.method == 'POST':
            form = AdminPasswordChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                self.message_user(request, 'Password changed successfully.', messages.SUCCESS)
                return HttpResponseRedirect(reverse('admin:accounts_user_change', args=[lecturer_id]))
        else:
            form = AdminPasswordChangeForm(user)

        context = {
            'title': 'Reset password: {}'.format(user.username),
            'form': form,
            'lecturer': lecturer,
            'opts': self.model._meta,
            'original': lecturer,
        }
        return render(request, 'admin/accounts/user/reset_password.html', context)

# admin.site.unregister(User)  # Commented out because User is not registered yet
admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent)
# admin.site.register(User, LecturerAdmin)  # Commented out to avoid AlreadyRegistered error
