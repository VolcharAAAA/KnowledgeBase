from django.db import models

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    body = models.TextField("Текст")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    author = models.CharField("Автор", max_length=100, default="Аноним")
    is_published = models.BooleanField("Опубликовать", default=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name="comments", 
        verbose_name="Пост", 
    )
    author = models.CharField("Автор", max_length=100)
    txt = models.TextField("Текс комментария")
    created_at = models.DateTimeField("Создано", auto_now_add=True) 

    def __str__(self):
        return f"Комментарий от {self.author}"
