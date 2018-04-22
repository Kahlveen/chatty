from django.shortcuts import render
from .models import ChatMsg
from .forms import MsgForm
from django.utils import timezone

def index(request):
	#chat_msgs = ChatMsg.objects.order_by('send_date')[:5]
	#context = {'chat_msgs': chat_msgs}
	#return render(request, 'comms/index.html', context)
	return render(request, 'comms/index.html', get_chat_msg())

def get_msg(request):
	# if its a POST request, need to process the form data
	if request.method == 'POST':
		form = MsgForm(request.POST)

		if form.is_valid():
			msg = ChatMsg(
					send_date = timezone.now(),
					msg = form.cleaned_date['send_msg'],
					sender = 'megatron',
					recipient = 'optimus'
				)
			msg.save()

	# TODO: Handle case where it is not POST

	return render(request, 'comms/index.html', get_chat_msg())

def get_chat_msg():
	return {'chat_msgs': ChatMsg.objects.order_by('send_date')[:5]}
