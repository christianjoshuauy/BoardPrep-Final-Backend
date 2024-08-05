from rest_framework import serializers
from .models import DailyChallenge, DailyChallengeQuestion, DailyChallengeLeaderboard


class DailyChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyChallenge
        fields = '__all__'


class DailyChallengeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyChallengeQuestion
        fields = '__all__'


class DailyChallengeLeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyChallengeLeaderboard
        fields = '__all__'
