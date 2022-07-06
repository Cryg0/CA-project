from rest_framework import serializers
from users.models import User,Profile


from app_api.serializers import WorkoutSerializer


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','username','password')
        extra_kwargs={'password':{'write_only':True}}


    def create(self,validated_data):
        
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        

        return instance


class UserSerializer(serializers.ModelSerializer):
    total_workouts = serializers.SerializerMethodField()

    def get_total_workouts(self, obj):
        workouts = obj.workout_set.all().filter(status='finished').count()
        return workouts
    class Meta:
        model = User
        fields = ('id','username','first_name','email','about','total_workouts')

class ProfileSerializer(serializers.ModelSerializer):
   
    user=UserSerializer()
    class Meta:
        model=Profile
        

        fields=('user','picture')
        depth=1