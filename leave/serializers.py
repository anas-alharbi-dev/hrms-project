from rest_framework import serializers
from .models import LeaveRequest


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'
        read_only_fields = ['employee',]  # الموظف ما يغيرها

    def update(self, instance, validated_data):
        user = self.context['request'].user

        # إذا المستخدم admin يقدر يغير status
        if user.is_staff:
            instance.status = validated_data.get('status', instance.status)

        # باقي التحديثات عادي
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.reason = validated_data.get('reason', instance.reason)

        instance.save()
        return instance