from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer 
from rest_framework.permissions import SAFE_METHODS, BasePermission, DjangoModelPermissions

class PostUserWritePermission(BasePermission): # BsePermission OverRiding
    # 게시물에 대한 권한이 있는 User가 잠재적으로 작성, 편집, 삭제할 수 있는 유일한 객체이다.
    message = 'Editing posts is restricted to the author only.'
    def has_object_permission(self, request, view, obj): # 객체와 뷰도 받는다.
        if request.method in SAFE_METHODS: # 모든 정보가 이 함수 내에서 액세스할 수 있도록 한다.
            # http method인 get put 등을 확인하여 안전한 메소드인지 확인한다.
            return True # user는 ReadOnly 권한을 부여받을 수 있게된다. 쓰기 권한이 있는지는 obj를 리턴시켜서 작성자가 일치하는지 확인한다.
        return obj.author == request.user # PostList에서 user에 대한 정보를 가지고 있기 때문에 로그인 시에 일치 여부 판단이 가능해진다.
                                          # DB에 분명히 author 필드가 존재하므로 일치시키면 된다.  

# 게시물 목록 뷰가 될 첫 번째 뷰 빌드 (본질적 우리에게 보여줄 항목)
# 어지간한 건 알아서 다 해주는데, 정상 작동을 위해 몇 가지 정보를 우리가 좀 알려줄 필요가 있음
class PostList(generics.ListCreateAPIView): 
    permission_classes = [ DjangoModelPermissions ]
    queryset = Post.postobjects.all() # 해당 데이터를 여기서 사용하겠다.
    serializer_class = PostSerializer # 직렬 변환기 (프론트에서 사용할 수 있는 형식으로 모두 변환)

# 게시물 세부 정보 뷰. (검색과 삭제)
class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission): 
    permission_classes = [ PostUserWritePermission ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer