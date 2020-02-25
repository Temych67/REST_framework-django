from chat.models import Chat
from chat.api.serializers import ChatSenderSerializer,MessageDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q
from chat.api.pagination import PostPageNumberPagination
from rest_framework import generics

@api_view(['POST', ])
def api_send_message_view(request):
	if request.method == 'POST':
		data = request.data
		serializer = ChatSenderSerializer(data=data)
		data = {}
		if serializer.is_valid():
			mesenger = serializer.save()
			data['email'] = mesenger.email
			data['message'] = mesenger.message
			data['date_published'] = mesenger.date_published
			data['date_updated'] = mesenger.date_updated
			return Response(data=data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiMessageListView(ListAPIView):
	queryset = Chat.objects.all()
	serializer_class = MessageDetailSerializer
	pagination_class = PostPageNumberPagination



class ApiMessageSingleView(generics.ListAPIView):
	serializer_class = MessageDetailSerializer
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('email', 'message', 'date_published')
	def get_queryset(self,*args,**kwargs):
		queryset_list = Chat.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(email=query)|
					Q(message=query)|
					Q(date_published=query)).distinct()
		return queryset_list