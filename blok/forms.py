

from django import forms
from blok.models import Article


class ArtForm(forms.Form):
    title = forms.CharField(max_length=20,
                            required=True,

                            error_messages={
                                'required': '标题不能为空',
                                'min_length': '最少两个字符',
                                'max_length': '最多20个字符'
                            })
    keywords = forms.CharField(max_length=10,

                               required=True,
                               error_messages={
                                   'required': '关键字不能为空',
                                   'min_length': '最少两个字符',
                                   'max_length': '最多10个字符'
                               })
    imgs = forms.ImageField(required=True,
                            error_messages={
                                'required': '头像必填'
                            })
    describe = forms.CharField(required=True,
                               error_messages={
                                   'required': '不能为空'
                               })
    content = forms.CharField(required=True,
                              error_messages={
                                   'required': '关键字不能为空',
                               })
    label = forms.CharField(required=True,
                            error_messages={
                                   'required': '关键字不能为空',
                               })

    def clean(self):
        title = self.cleaned_data['title']
        tit = Article.objects.filter(title=title).first()
        if tit:
            raise forms.ValidationError({'title': '标题不能重复'})
        return self.cleaned_data['title']