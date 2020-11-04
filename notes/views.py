from django.shortcuts import render, redirect
from .models import Notes
# Create your views here.
def editor(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = Notes.objects.all()

    if request.method == 'POST':
        noteid =int( request.POST.get('noteid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if noteid > 0:
            note = Notes.objects.get(pk=noteid)
            note.title = title
            note.content = content
            note.save()

            return redirect('/?noteid=%i' %  noteid) 
        else:
            note = Notes.objects.create(title=title, content=content)

            return redirect('/?noteid=%i' % note.id) 

    if noteid > 0:
        note = Notes.objects.get(pk=noteid)
    else:
        note = ''    

    context = {
        'noteid': noteid,
        'notes': notes,
        'note': note
    }
    return render(request, 'editor.html', context)

def delete_note(request, noteid):
    note = Notes.objects.get(pk=noteid)
    note.delete()

    return redirect('/?noteid=0')