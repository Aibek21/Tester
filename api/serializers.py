# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

        
class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField()


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField()
    isAnswer = serializers.BooleanField(default=False)



class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = QuestionSerializer()
    options = AnswerSerializer(many=True)


class VariantListSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=140, default="Вариант")


class VariantDetailSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=140, default="Вариант")
    tasks = TaskSerializer(many=True, required=False)
