from django.db import models

# Create your models here.

class Blog(models.Model): # Primary Key를 지정하지 않으면 Django가 자동으로 만들어준다. (id)
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # 올려도 그만, 안 올려도 그만 // upload_to로 지정한 폴더에 img 파일을 저장해준다.
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title # db에 저장되는 테이블 명을 타이틀 명으로 설정한다.

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시물에 작성된 댓글인가?
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) # CASCADE : 종속된 테이블이 삭제될 때, 테이블을 참조하는 커맨드도 삭제된다.

    def __str__(self):
        return self.comment