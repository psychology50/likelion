from django.db import models
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    '''
    모델 관리자 PostObject
    DB에서 데이터를 전송해주고 모두 출력한다고 가정하면,
    처음에는 해당 데이터를 필터링하여 게시된 게시물을 표시하여 
    여기에 이 사용자 지정 관리자를 생성하므로 기본적으로 쿼리를 생성할 때
    데이터에서 모든 개체를 실행하는 대신 게시물 객체를 실행할 수 있다.
    => 그니까 '게시된(published)' 게시물만 쏙쏙 골라먹겠다는 뜻. 나중에 따로 filtering 안 해줘도 됨.
    '''
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1
    )
    title = models.CharField(max_length=250) # 제목
    excerpt = models.TextField(null = True) # 발췌문
    content = models.TextField()
    # 슬러그는 지금 단계에선 사실 필요없지만, 슬러그는 본질적으로 URL이므로
    # 제목을 슬러그화하여 각 게시물의 고유 식별자를 사용하지 않는 방법.
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    # 사용자가 새 게시물을 작성하면 해당 게시물과 현재 유저가 서로 종속됨
    # CASCADE 속성을 줌으로써 유저가 삭제되면 게시물도 DB 상에서 모두 제거한다.
    author = models.ForeignKey( 
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts'
    )
    # 때론 바로 게시가 되는 걸 원치 않을 수도 있으므로 options을 준다.
    status = models.CharField(
        max_length=10, choices=options, default='published'
    )

    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager
 
    class Meta:
        ordering = ('-published', )
    
    def __str__(self):
        return self.title
