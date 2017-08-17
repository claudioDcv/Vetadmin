from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = ['pk']

    def save(self, commit=False):
        try:
            if self.data['photo_first-clear'] == 'on':
                self.instance.photo_first.delete()
            if self.data['photo_second-clear'] == 'on':
                self.instance.photo_first.delete()
            if self.data['photo_third-clear'] == 'on':
                self.instance.photo_first.delete()
        except Exception as e:
            pass
        m = super(PatientForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.save()
        return m
