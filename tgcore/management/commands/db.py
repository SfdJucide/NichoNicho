from tgcore.models import TgUser, Product

def add_user(user_id, username):
    if not TgUser.objects.filter(user_id=user_id):
        user = TgUser(
            user_id=user_id,
            username=username,
            )
        user.save()