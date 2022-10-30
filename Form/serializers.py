from Form.models import Form
from .models import Form
from article.models import Artikel
from rest_framework import serializers


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['nama_lengkap', 'user_email', 'no_hp', 'subject', 'user_msg']
