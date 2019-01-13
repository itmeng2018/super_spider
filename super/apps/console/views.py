from django.shortcuts import render
from django.views import View


class ProgressView(View):
    def get(self, request):
        return render(request, 'test_show.html')


class SpiderConfigView(View):
    def get(self, request):
        return render(request, 'spider_config.html')


# visualization
class VisualizationView(View):
    def get(self, request):
        print(request.session.__dict__)
        return render(request, 'index.html')