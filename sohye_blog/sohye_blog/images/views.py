# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
"""
class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all() # 파이썬 Object, 시리얼라이저로 json으로 변환해야함

        serializer = serializers.ImageSerializer(all_images, many=True)
        # imageSerializer는 한개의 이미지씩 serialize 하기 때문에 여러 이미지를 serialize 할 수 있도록 many=True.
        # serializer는 클래스. serialize가 끝나면 해당 데이터들을 serializer.data에 저장

        return Response(data=serializer.data)
"""


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user
        following_users = user.following.all()

        image_list = []

        for following_user in following_users:
            user_image = following_user.image.all()[:2]

            for image in user_image:
                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)
