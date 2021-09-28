from rest_framework import serializers
from trener.models import *



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'firstName', 'lastName', 'birthDate',
                  'sex']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'firstName', 'lastName', 'isClient', 'birthDate',
                  'sex', 'height', 'activity', 'goal']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = "__all__"


class ChestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chest
        fields = "__all__"


class BicepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biceps
        fields = "__all__"


class BenchPressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchPress
        fields = "__all__"


class SquatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squat
        fields = "__all__"


class DeadliftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deadlift
        fields = "__all__"