from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    #############################################
    def validate(self, attrs):
        print(attrs)
        title = attrs.get('title')
        title = title.upper()
        attrs['title'] = title
        return attrs

    def validate_description(self, d):
        if len(d) < 20:
            raise serializers.ValidationError('Описание слишком короткое! Напишите 20+ символов')
        return d
    ##############################################
