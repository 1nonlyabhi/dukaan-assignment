from rest_framework import serializers

from account.models import Account

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['mobile_num', 'password']

    def save(self):
        account = Account(
            mobile_num=self.validated_data['mobile_num']
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account


# class ValidationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Account
#         fields = ['mobile_num', 'otp']