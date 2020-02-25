from django.urls import path

from chat.api.views import(
	api_send_message_view,
	ApiMessageListView,
	ApiMessageSingleView,

)

app_name = 'message'

urlpatterns = [
	path('send', api_send_message_view, name="send"),
	path('list/<int:page>', ApiMessageListView.as_view(), name="list"),
	path('single', ApiMessageSingleView.as_view(),name="single"),
	]