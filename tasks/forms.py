from django import forms
from tasks.models import Task
# class TaskForm(forms.Form):
#     title = forms.CharField(max_length=250)
#     description = forms.CharField(widget=forms.Textarea,label="Description")
#     due_date = forms.DateField(widget=forms.SelectDateWidget,label="Due date")
#     assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[],label="Assined to:")

#     def __init__(self,*arg,**kwargs):
#         # print(arg,kwargs)
#         employees = kwargs.pop("employees",[])
#         # print("pop korar pore",employees)
#         super().__init__(*arg,**kwargs)
#         # print(self.fields)
#         self.fields['assigned_to'].choices= [(emp.id,emp.name) for emp in employees ]

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','assigned_to']
        widgets = {
            'due_date':forms.SelectDateWidget,
            'assigned_to':forms.CheckboxSelectMultiple
        }
        
      
    