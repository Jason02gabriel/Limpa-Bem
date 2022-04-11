import tempfile
from crispy_forms.layout import HTML
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from xhtml2pdf import pisa

import users.apps
from .forms import TaskForm
from .models import Task
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime

def relatorioPedido(request):
    search = request.GET.get('search')
    tasksDoneRecently = Task.objects.filter(done='concluido',
                                            updated__gt=datetime.datetime.now() - datetime.timedelta(days=30)).count()
    tasksDone = Task.objects.filter(done='concluido').count()
    tasksDoing = Task.objects.filter(done='pendente').count()
    if search:
        tasks = Task.objects.filter(id__icontains=search)

    else:

        tasks_list = Task.objects.all().order_by('-created_at')

        paginator = Paginator(tasks_list, 3)

        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/relatorio.html',
                  {'tasks': tasks, ' tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone,
                   'tasksdoing': tasksDoing})


def helloworld(request):
    return HttpResponse('Hello World!')

@login_required()
def tasklist(request):
    search = request.GET.get('search')
    tasksDoneRecently = Task.objects.filter(done='concluido' , updated__gt= datetime.datetime.now() - datetime.timedelta(days=30)).count()
    tasksDone = Task.objects.filter(done = 'concluido').count()
    tasksDoing = Task.objects.filter(done = 'pendente').count()
    if search:
        tasks = Task.objects.filter(id__icontains = search)

    else:

        tasks_list = Task.objects.all().order_by('-created_at')

        paginator = Paginator(tasks_list, 3)

        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html',
                  {'tasks': tasks , ' tasksrecently': tasksDoneRecently , 'tasksdone':tasksDone, 'tasksdoing':tasksDoing} )

@login_required()
def taskView(request , id):
    task = get_object_or_404(Task, pk = id)
    return render(request, 'tasks/pedido.html' , {'task':task})

@login_required()
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.atendente = ';'
            task.data_atendimento = datetime.date.today()
            task.done = 'pendente'
            if task.Serviço == 'limpeza profunda':
                task.preço = 'R$250,00'
            else:
                task.preço = 'R$150,00'

            task.save()
            messages.info(request, 'Pedido Cadastrado com sucesso.')
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form':form})

@login_required()
def editTask(request, id, false=None):
    task = get_object_or_404(Task , pk = id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request,'tasks/edittask.html', {'form':form,'task':task})
    else:
        return render(request,'tasks/edittask.html', {'form':form,'task':task})

@login_required()
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request,'Pedido deletado com sucesso.')
    return redirect('/')

@login_required()
def changeStatus(request, id):
    task = get_object_or_404(Task , pk = id)

    if (task.done == 'pendente'):
        task.done = 'concluido'
    else:
        task.done = 'pendente'
    task.save()
    return redirect('/')


def some_view(request):
    tasks = Task.objects.all()
    template_path = 'tasks/relatorio.html'

    context = {'tasks': tasks}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



