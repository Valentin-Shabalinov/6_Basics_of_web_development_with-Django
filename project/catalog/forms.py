from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "title",
            "description",
            "preview",
            "category",
            "purchase_price",
            "date_creation",
            "date_modified",
        )

    def clean_title(self):
        cleaned_data = self.cleaned_data["title"]
        for i in [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]:
            if i in cleaned_data:
                raise forms.ValidationError(
                    "Название содержит запрещенные слова"
                )

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        for i in [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]:
            if i in cleaned_data:
                raise forms.ValidationError(
                    "Описание содержит запрещенные слова"
                )

        return cleaned_data


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
