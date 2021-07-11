import os

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from .models import Post
from django.views import generic
from .apps import AppConfig, ApiConfig


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class IndexView(generic.ListView):
    model = Post
    template_name = 'api/index_post.html'

class ReadView(generic.ListView):
    model = Post
    template_name = 'api/read_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


from .forms import CreatePost
def CreatePostView(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)

        if form.is_valid():
            data = ApiConfig.model.predict(request.sentence)

            instance = form.save(commit=False)
            instance.subtitle = data
            instance.user_id = None;
            instance.save()

            return redirect('/api/diary/read')
        else:
            return redirect('/api/diary/create')
    else:
        form = CreatePost()
        return render(request, 'api/create_post.html', {'form': form})



# import pickle
# import os
# from django.conf import settings
# import MeCab
# from keras_preprocessing.sequence import pad_sequences
# from keras.preprocessing.text import Tokenizer
#
# def CreatePostView(request):
#     maxlen = 10
#     max_words = 3000
#     tokenizer = Tokenizer(num_words=max_words)
#     m = MeCab.Tagger()
#     path = os.path.join(os.path.dirname(os.path.realpath(__file__)), settings.MODEL_ROOT)
#     def getSequences(sentence):
#         sentence = [x.split("\t")[0] for x in m.parse(sentence).split("\n") if not x == "EOS" and not x == ""]
#         return pad_sequences(tokenizer.texts_to_sequences([sentence]), maxlen=maxlen)
#     model = pickle.load(open(path, 'rb'))
#
#     if request.method == 'POST':
#         form = CreatePost(request.POST)
#
#         if form.is_valid():
#             instance = form.save(commit=False)
#             sentence = form.cleaned_data['content']
#             data = model.predict_classes(getSequences(sentence))
#             instance.subtitle = data
#             instance.save()
#
#             return redirect('/api/diary/read')
#         else:
#             return redirect('/api/diary/create')
#     else:
#         form = CreatePost()
#         return render(request, 'api/create_post.html', {'form': form})

