# No curso de e-comerce da udemy, diz que esse codigo é necessário para fazer
#login com o email, no entanto no meu caso não funcionou, só precisei alterar
# no models do meu user personalizado no app accounts a variavel USERNAME_FIELDS
# passou a receber o valor 'email' e o trecho REQUIRED_FIELDS foi comentado.
# E no settings o trecho AUTHENTICATION_BACKENDS foi comentado.
# Não sei se essa é a forma correta, mas funcionou.



# from django.contrib.auth.backends import ModelBackend as BaseModelBackend
#
# from .models import User
#
#
#
#
# class ModelBackend(BaseModelBackend):
#
#     def authenticate(self, username=None, password=None):
#         if not username is None:
#             try:
#                 user = User.objects.get(email=username)
#                 if user.check_password(password):
#                     return user
#
#             except Exception as e:
#                 pass