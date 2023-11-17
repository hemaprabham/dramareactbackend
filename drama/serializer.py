from rest_framework import serializers
from .models import *

class DramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drama
        fields = ('title',
            'genre',
            'director',
            'writer',
            'language',
            'country'
        )
            