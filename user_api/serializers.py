from rest_framework import serializers

from user_api.models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'image', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            image=validated_data.get('image', None),
            password=validated_data['password']
        )
        
        return user


    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        password = validated_data.get('password', None)
        
        if password is not None:
            instance.set_password(password)

        instance.save()
        
        return instance
    