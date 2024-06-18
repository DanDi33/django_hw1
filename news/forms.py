from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, ButtonHolder, HTML
import os

class NewsForm(forms.ModelForm):
    class Meta(object):
        model = Post
        fields = ['title', 'imagefile', 'category', 'description', 'post']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-newForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'

        self.fields['title'].label = "Заголовок"
        self.fields['category'].label = "Категория"
        self.fields['imagefile'].label = ""
        self.fields['description'].label = "Краткое описание новости"
        self.fields['post'].label = "Текст новости"
        self.helper.layout = Layout(
            Div(
                Div(Field('title'),
                    Field('category'),
                    Field('imagefile', onchange='previewFile()', style='display:none;', css_class='mb-0'),                   
                    Field('description', rows=4),
                    css_class='col-6'),
                Div(Field('post', rows=27),
                    css_class='col-6'), 
                css_class='row mt-2'),
                ButtonHolder(
                    HTML('<a href="{% url "posts" %}" class="btn btn-secondary">Отмена</a>'),
                    Submit('submit', 'Сохранить'),
                    css_class='d-grid gap-2 d-md-flex justify-content-md-end'),
                    HTML('''<script> 
                        function previewFile() {
                            var preview = document.querySelector('img');
                            let temp_src = preview.src;
                            var file = document.querySelector('#id_imagefile').files[0];
                         console.log(preview)
                         console.log(file)
                            var reader = new FileReader();

                        reader.onloadend = function () {
                            preview.src = reader.result;
                        }

                        if (file) {
                            reader.readAsDataURL(file);
                        }
                        else if (!temp_src) {
                            preview.src = 'default_news.jpg';
                        } 
                        else {
                            preview.src = temp_src;
                        }
                        }
                        </script>''')
            )

        self.helper.layout[0][0][1].append(HTML('<div id="div_id_image"><p class="mb-2">Картинка новости</p><img src="{% if post %} {{ post.imagefile.url }} {% else %} /media/default_news.jpg {% endif %}" class="card-img-top edit-img" style="cursor:pointer;" onclick="id_imagefile.click()" alt="..." accept=".jpg,.jpeg,.png"></div>'))

            