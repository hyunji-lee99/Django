from rest_framework import generics
from .models import Post, Sep
from .serializers import PostSerializer, SepSerializer

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#연구노트 정리 필요함.
class SeperatePost(generics.ListCreateAPIView):
    #loop 돌려서 Post의 데이터들을 분리해줘야 함.
    item = list(Post.objects.all().values())
    for i in item:
        for j in i["data"]:
            ele=Sep(title=j["title"], content=j["content"])
            ele.save()
    queryset = Sep.objects.all() #Sep 모델에 저장된 데이터 모두 가져와서 ListCreateAPIView로 출력함
    serializer_class = SepSerializer