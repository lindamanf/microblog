from django.db import models

class Blog(models.Model):
    # 文字列型フィールド
    content = models.CharField(max_length=140)
    # 日付型フィールド
    post_date = models.DateTimeField(auto_now_add=True)
