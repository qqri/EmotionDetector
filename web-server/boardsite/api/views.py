import os

from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


# api/views.py
from rest_framework import viewsets, status
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions
import pickle
import os
from django.conf import settings

import MeCab
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
maxlen=10
max_words = 3000
tokenizer = Tokenizer(num_words=max_words)
m = MeCab.Tagger()

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), settings.MODEL_ROOT)

        def getSequences(sentence):
            sentence = [x.split("\t")[0] for x in m.parse(sentence).split("\n") if not x == "EOS" and not x == ""]
            return pad_sequences(tokenizer.texts_to_sequences([sentence]), maxlen=maxlen)

        model = pickle.load(open(path, 'rb'))
        sentence = serializer.data['content']

        test = "날씨가 좋다"
        test = [x.split("\t")[0] for x in m.parse(test).split("\n") if not x == "EOS" and not x == ""]
        print(pad_sequences(tokenizer.texts_to_sequences([test]), maxlen=maxlen))

        data = model.predict_classes(getSequences(sentence))
        #return Response(model.predict_classes( getSequences(sentence)),status=status.HTTP_200_OK)
        return HttpResponse(data)

