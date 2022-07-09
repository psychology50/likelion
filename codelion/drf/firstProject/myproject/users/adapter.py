from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.email = data.get('email')
        user.user_name = data.get('user_name')
        user.password = data.get('password')
        user.profile_image = data.get('profile_image')
        user.save()
        return user