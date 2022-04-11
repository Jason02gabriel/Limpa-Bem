
from django.urls import path
from . import views
urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.tasklist, name= 'task-list'),
    path('task/<int:id>', views.taskView, name = "task-view"),
    path('newtask/',views.newTask, name= 'new-task'),
    path('edit/<int:id>', views.editTask, name = 'edit-task'),
    path('changestatus/<int:id>', views.changeStatus, name = 'change-status'),
    path('delete/<int:id>', views.deleteTask, name = 'delete-task'),
    path('relatorio/',views.relatorioPedido,name = 'relatorio-pedido'),
    path('pdf/', views.some_view, name='pdf')
]

