from django import forms
from main_app.models import Job, Resume, Skill

class JobForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Використовує чекбокси для вибору
        required=False  # Робить поле необов'язковим
    )
    class Meta:
        model = Job
        fields = ['title', 'description', 'name_company', 'location', 'min_salary', 'max_salary', 'user', 'skills']
    
    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'skills':  # Не додаємо form-control до чекбоксів
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label,
                    'style': 'margin-bottom: 15px;',
                })

class JobUpdateForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Використовує чекбокси для вибору
        required=False  # Робить поле необов'язковим
    )
    class Meta:
        model = Job
        fields = ['title', 'description', 'name_company', 'location', 'min_salary', 'max_salary', 'skills']
    
    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'skills':  # Не додаємо form-control до чекбоксів
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label,
                    'style': 'margin-bottom: 15px;',
                })


class ResumeForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Використовує чекбокси для вибору
        required=False
    )

    class Meta:
        model = Resume
        fields = ['full_name', 'summary', 'experience', 'education', 'user', 'skills']
    
    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'skills':  # Не додаємо form-control до чекбоксів
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label,
                    'style': 'margin-bottom: 15px;',
                })


class ResumeUpdateForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Resume
        fields = ['full_name', 'summary', 'experience', 'education', 'skills']
    
    def __init__(self, *args, **kwargs):
        super(ResumeUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'skills':  # Не додаємо form-control до чекбоксів
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label,
                    'style': 'margin-bottom: 15px;',
                })


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'required_level']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })
            field.widget.attrs['style'] = 'margin-bottom: 15px;'
