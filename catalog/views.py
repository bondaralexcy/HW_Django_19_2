from django.shortcuts import render
import csv

# Create your views here.
def home(request):
    """ Основной контроллер
    """
    return render(request, 'catalog/home.html')


def contacts(request):
    """ Обработка обратной связи
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Вывод на консоль
        print(f'You have a new message from user {name} ({phone}): {message}')

        # Запись в файл
        with open('messages.csv', 'a', newline='') as csvfile:
            fieldnames = ['first_name', 'phone', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow({'first_name': name, 'phone': phone, 'message': message})

    return render(request, 'catalog/contacts.html')

