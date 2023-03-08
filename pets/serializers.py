from rest_framework import serializers
from pets.models import Pets, animals


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ['id', 
                  'image', 
                  'name',
                  'description',
                  'animal',
                  'breed',
                  'state',
                  'city',
                  'intake']

# ModelSerializer: automatically determines set of fields, 
# and default implementations for create() and update() methods
