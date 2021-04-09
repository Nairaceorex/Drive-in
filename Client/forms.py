from django import forms



class RegForm(forms.Form):
    Surname = forms.CharField(label='Фамилия',
                              max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Фамилия',
                                                            'class': 'form-control',
                                                            'pattern': '^[А-Яа-яЁё]+$'}),
                              required=True)
    Firstname = forms.CharField(label='Имя',
                                max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Имя',
                                                              'class': 'form-control',
                                                              'pattern': '^[А-Яа-яЁё]+$'}),
                                required=True)

    DateBirth = forms.DateField(label="Дата рождения",
                                widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Введите дату рождения',
                                                              'type': "date"}),
                                required=True)
    Email = forms.EmailField(label="Эл. почта",
                             widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com',
                                                            'class': 'form-control'}),
                             required=True)
    Password = forms.CharField(label="Пароль",
                               max_length=16, min_length=8,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль','class': 'form-control'}),
                               help_text = "Пароль должен состоять из 8-16 символов",
                               required=True)

    Phone = forms.CharField(label="Номер телефона",
                                  max_length=10, min_length=10,
                                  widget=forms.TextInput(attrs={'placeholder': 'Номер телефона','class': 'form-control'}),
                                  required=True)
    isPosting = forms.BooleanField(label="Подписываюсь на получение новостей на свой Email", required=False)
    isAgree = forms.BooleanField(label="Прочитал(-а) и принимаю пользовательское соглашение", required=True)


class LogForm(forms.Form):
    EmailLogin = forms.EmailField(label="Эл. почта",
                                  widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com',
                                                                 'class': 'form-control'}),
                                  required=True)
    PasswordLogin = forms.CharField(label="Пароль",
                                    max_length=16, min_length=8,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control PassHidden'}),
                                    required=True)