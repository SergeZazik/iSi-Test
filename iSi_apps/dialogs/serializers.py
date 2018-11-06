from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from iSi_apps.accounts.models import UserTypes
from iSi_apps.dialogs.models import Message, Thread


class OneAdminValidator(object):
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, attrs):
        for field, value in attrs.items():
            if field in self.fields:
                admins_amount = sum(1 for participant in value if participant.user_type == UserTypes.ADMIN.value)

                if admins_amount < 1:
                    raise ValidationError({field: 'Thread must have admin'})
                elif admins_amount > 1:
                    raise ValidationError({field: 'Thread can have only one admin'})


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'
        read_only_fields = ('created', 'updated')

        validators = [
            OneAdminValidator(
                fields=('participants', ),
            )
        ]


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if not super(MessageSerializer, self).is_valid(raise_exception):
            return False

        user_in_thread = self._validated_data['sender'].threads.filter(pk=self._validated_data['thread'].pk).exists()

        if not user_in_thread:
            raise serializers.ValidationError('This user is not a participant of specified thread')
