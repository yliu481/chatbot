from django.template.response import TemplateResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from langid import classify

# Create your views here.
print('start trainning')
chatbot=ChatBot('Ron Obvious')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

chatbot_ch=ChatBot('Tang')
trainer_ch = ChatterBotCorpusTrainer(chatbot_ch)
trainer_ch.train("chatterbot.corpus.chinese")
print('trainning over')


def index(request):
	return TemplateResponse(request,'chatbot.html',{})
@csrf_exempt
def post_message(request) :
	message = request.POST.get('message','')
	try:
		if(classify(message)[0]=='zh'):
			result = chatbot_ch.get_response(message)
		else:
			result = chatbot.get_response(message)
	except:
		result = chatbot.get_response(message)
	return HttpResponse(result)