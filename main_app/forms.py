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

class JobUpdateForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Використовує чекбокси для вибору
        required=False  # Робить поле необов'язковим
    )
    class Meta:
        model = Job
        fields = ['title', 'description', 'name_company', 'location', 'min_salary', 'max_salary', 'skills']


class ResumeForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Використовує чекбокси для вибору
        required=False  # Робить поле необов'язковим
    )

    class Meta:
        model = Resume
        fields = ['full_name', 'summary', 'experience', 'education', 'user', 'skills']


class ResumeUpdateForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Resume
        fields = ['full_name', 'summary', 'experience', 'education', 'skills']
