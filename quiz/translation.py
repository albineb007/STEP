from modeltranslation.translator import translator, TranslationOptions
from .models import Quiz, Question, MCQuestion

class QuizTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class QuestionTranslationOptions(TranslationOptions):
    fields = ('content', 'explanation',)

class MCQuestionTranslationOptions(TranslationOptions):
    fields = ()

translator.register(Quiz, QuizTranslationOptions)
translator.register(Question, QuestionTranslationOptions)
translator.register(MCQuestion, MCQuestionTranslationOptions)
