from rest_framework import serializers
from django.core.mail import send_mail
from app.users.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone",
            "password"
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        old_email = instance.email
        new_email = validated_data.get('email', old_email)

        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        instance = super().update(instance, validated_data)

        if old_email != new_email and new_email:
            send_mail(
                subject="Ваш email изменен",
                message=f"Внимание, {instance.username}!\n\nДанные вашего профиля были изменены.",
                from_email=None,
                recipient_list=[new_email],
                fail_silently=True
            )
        return instance