from modeltranslation.translator import translator, TranslationOptions
from .models import (
    ProductModel
)

class ProductmodelTranslationOptions(TranslationOptions):
    fields = ('title', 'about',)

translator.register(ProductModel, ProductmodelTranslationOptions)
