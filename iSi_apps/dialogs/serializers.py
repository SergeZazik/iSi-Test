from rest_framework import serializers
from iSi_apps.accounts.models import CustomUser
from iSi_apps.dialogs.models import Message, Thread


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = '__all__'

    def update(self, instance, validated_data):
        if CustomUser.ADMIN in instance.participant.all().values_list('user_type', flat=True):
            raise serializers.ValidationError('Only one administrator')
        else:
            instance.participant.add(validated_data.get('participant'))
        return instance


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
