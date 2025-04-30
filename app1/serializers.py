from rest_framework import serializers
from . import models


class StudentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = [
            'id', 'full_name','phone','status', 'OTM','contract'
        ]


    def validate(self, data):

        if 'full_name' in data and not data['full_name'].replace(" ", "").isalpha():
            raise serializers.ValidationError({"full_name": "Ism faqat harflardan iborat bo'lishi kerak."})

        if 'contract' in data:
            if data['contract'] < 0:
                raise serializers.ValidationError({"contract": "Contract amount cannot be negative."})

        return data


class StudentListSerializer(serializers.ModelSerializer):
    contract = serializers.SerializerMethodField()
    separated_amount = serializers.SerializerMethodField()

    class Meta:
        model = models.Student
        exclude = ['phone', 'updated_at', 'created_at']

    def get_contract(self, obj):
        return obj.formatted_contract()

    def get_separated_amount(self, obj):
        return obj.formatted_separated_amount()


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = [
            'id', 'full_name', 'phone', 'sponsor_amount', 'spent_amount', 'date', 'position', 'student', 'payment'
        ]


class SponsorListSerializer(serializers.ModelSerializer):
    position_name = serializers.CharField(source='position.name', read_only=True)
    sponsor_amount = serializers.SerializerMethodField()
    spent_amount = serializers.SerializerMethodField()

    class Meta:
        model = models.Sponsor
        fields = [
            'id', 'full_name', 'phone', 'sponsor_amount','spent_amount', 'date','position_name'
        ]

    def get_sponsor_amount(self, obj):
        return obj.formatted_sponsor_amount()

    def get_spent_amount(self, obj):
        return obj.formatted_spent_amount()


class SponsorRetrieveSerializer(serializers.ModelSerializer):
    position_name = serializers.CharField(source='position.name', read_only=True)

    class Meta:
        model = models.Sponsor
        fields = [
            'full_name', 'phone', 'sponsor_amount', 'position_name'
        ]


class SponsorUpdateSerializer(serializers.ModelSerializer):
    workplace = serializers.CharField(max_length=200, required=False, allow_null=True, allow_blank=True)
    position_name = serializers.CharField(source='position.name', read_only=True)

    class Meta:
        model = models.Sponsor
        fields = [
            'full_name', 'phone', 'sponsor_amount', 'position_name' ,'payment', 'user_type', 'workplace'
        ]

    def validate(self, data):
        user_type = data.get('user_type')

        if 'full_name' in data and not data['full_name'].replace(" ", "").isalpha():
            raise serializers.ValidationError({"full_name": "Ism faqat harflardan iborat bo'lishi kerak."})

        if 'sponsor_amount' in data:
            if data['sponsor_amount'] < 0:
                raise serializers.ValidationError({"sponsor_amount": "Sponsor amount cannot be negative."})

        if user_type == 'legal' and 'workplace' not in data:
            raise serializers.ValidationError({"workplace": "Workplace is required for legal sponsors."})

        return data


class SponsorCreateSerializer(serializers.ModelSerializer):
    separated_amount = serializers.ReadOnlyField(source='student.separated_amount')

    class Meta:
        model = models.Sponsor
        fields = ['id', 'full_name', 'separated_amount']
