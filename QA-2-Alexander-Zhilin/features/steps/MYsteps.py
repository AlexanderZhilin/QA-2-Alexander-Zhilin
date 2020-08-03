from behave import given, when, then, step  # pylint: disable=no-name-in-module
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@given(u'я запускаю тест 002')
def step_impl(context):
    title = "Новый заголовок Т002.py"  # Переменная для разных заголовков
    task = "Задача №1 Т002.py"  # Переменная для разных задач
    heading_before = context.driver.find_elements_by_tag_name('h2')  # Ищем все заголовки до теста
    task_before = context.driver.find_elements_by_tag_name('label')  # Ищем все задачи до теста
    a = 0
    b = 0
    for i in heading_before:
        if i.text == title:  # Ищем все заголовки, соответствующие тому, что мы будем вводить и считаем сколько таких
            a += 1
    for x in task_before:
        if x.text == task:  # Ищем все задачи, соответствующие тому, что мы будем вводить и считаем сколько таких
            b += 1

    context.driver.find_element_by_css_selector("img").click()  # Кликаем на кнопку "Создать новое задание"
    context.driver.find_element_by_id('select2-select_category-container').click()  # Кликаем на выпадающий список
    select = Select(context.driver.find_element_by_id('select_category'))  # Выбираем выпадающий список
    select.select_by_visible_text("Создать новый список")  # Находим в выпавшем списке пункт соответствующий тексту
    context.driver.find_element_by_id('select2-select_category-container').click()  # Кликаем на контейнер, чтобы выйти
    context.driver.find_element_by_id('project_title').click()  # Кликаем на поле "Заголовок"
    context.driver.find_element_by_id('project_title').send_keys(title)  # Вставляем текст в поле "Заголовок"
    context.driver.find_element_by_id('project_text').click()  # Кликаем на поле "Новая задача" -
    context.driver.find_element_by_id('project_text').send_keys(task)  # - Вставляем в него текст
    context.driver.find_element_by_id('submit_add_todo').click()  # Жмем кнопку ОК

    heading_after = context.driver.find_elements_by_tag_name('h2')  # Ищем все заголовки после теста
    task_after = context.driver.find_elements_by_tag_name('label')  # Ищем все задачи после теста
    а2 = 0
    b2 = 0
    for i2 in heading_after:
        if i2.text == title:  # Ищем все заголовки, соответствующие тому, что мы ввели и считаем сколько таких
            а2 += 1
            # print(title + " после теста стало: " + str(а2))
    for x2 in task_after:
        if x2.text == task:  # Ищем все задачи, соответствующие тому, что мы ввели и считаем сколько таких
            b2 += 1

    log = 0  # Сюда собираем ошибки
    if a == 0:
        if (len(heading_before) + 1) != len(heading_after):  # Если не было заголовка, то должен появиться
            log += 1
    if a == 1:
        if len(heading_before) != len(heading_after):  # Если был заголовок, то число заголовков не изменится
            log += 1
    if a == 0 or a == 1:  # Если наших новых заголовков не было, то должен появится новый +1
        if (b + 1) != b2:  # Если были заголовки или был только 1 и не стало задач больше на +1
            log += 1
    if log != 0:
        print("T002.Ошибка!")
        raise NotImplementedError(u'STEP: Given я запускаю тест 002')
    else:
        print("T002.Всё хорошо!")

@given(u'я запускаю тест 003')
def step_impl(context):
    title = "Семья"  # Переменная для разных заголовков
    task = "Задача №2 Т003.py"  # Переменная для разных задач
    heading_before = context.driver.find_elements_by_tag_name('h2')  # Ищем все заголовки до теста
    task_before = context.driver.find_elements_by_tag_name('label')  # Ищем все задачи до теста
    my_task_before = context.driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[1]/div/form')
    a = 0
    b = 0
    for i in heading_before:
        if i.text == title:  # Ищем все заголовки, соответствующие тому, что мы будем вводить и считаем сколько таких
            a += 1
    for x in task_before:
        if x.text == task:  # Ищем все задачи, соответствующие тому, что мы будем вводить и считаем сколько таких
            b += 1

    context.driver.find_element_by_css_selector("img").click()  # Кликаем на кнопку "Создать новое задание"
    context.driver.find_element_by_id('select2-select_category-container').click()  # Кликаем на выпадающий список
    select = Select(context.driver.find_element_by_id('select_category'))  # Выбираем выпадающий список
    select.select_by_visible_text("Семья")  # Находим в выпавшем списке пункт соответствующий тексту
    context.driver.find_element_by_id('select2-select_category-container').click()  # Кликаем на контейнер, чтобы выйти
    # driver.find_element_by_id('project_title').click(), t()  # Кликаем на поле "Заголовок"
    # driver.find_element_by_id('project_title').send_keys(title), t()  # Вставляем текст в поле "Заголовок"
    context.driver.find_element_by_id('project_text').click()  # Кликаем на поле "Новая задача" -
    context.driver.find_element_by_id('project_text').send_keys(task)  # - Вставляем в него текст
    context.driver.find_element_by_id('submit_add_todo').click()  # Жмем кнопку ОК

    heading_after = context.driver.find_elements_by_tag_name('h2')  # Ищем все заголовки после теста
    task_after = context.driver.find_elements_by_tag_name('label')  # Ищем все задачи после теста
    my_task_after = context.driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[1]/div/form')
    а2 = 0
    b2 = 0
    for i2 in heading_after:
        if i2.text == title:  # Ищем все заголовки, соответствующие тому, что мы ввели и считаем сколько таких
            а2 += 1
            # print(title + " после теста стало: " + str(а2))
    for x2 in task_after:
        if x2.text == task:  # Ищем все задачи, соответствующие тому, что мы ввели и считаем сколько таких
            b2 += 1

    log = 0  # Сюда собираем ошибки
    if a == 0:
        if len(heading_before) + 1 != len(heading_after):  # Если не было заголовка, то должен появиться
            log += 1
    if a == 1:
        if len(heading_before) != len(heading_after):  # Если был заголовок, то число заголовков не изменится
            log += 1
    if a == 0 or a == 1:  # Если наших новых заголовков не было, то должен появится новый +1
        a = 1
        if a != а2 and (b + 1) != b2:  # Если были заголовки или был только 1 и не стало задач больше на +1
            log += 1
    if len(my_task_before) + 1 != len(my_task_after):  # Если не было заголовка, то должен появиться
        log += 1
    if log != 0:
        print("T003.Ошибка!")
        raise NotImplementedError(u'STEP: Given я запускаю тест 003')
    else:
        print("T003.Всё хорошо!")

@given(u'я запускаю тест 004')
def step_impl(context):
    title = "Семья"  # Переменная для разных заголовков
    task = "Задача №3 Т004.py"  # Переменная для разных задач
    heading_before = context.driver.find_elements_by_tag_name('h2')  # Ищем все заголовки до теста
    task_before = context.driver.find_elements_by_tag_name('label')  # Ищем все задачи до теста
    a = 0
    b = 0
    for i in heading_before:
        if i.text == title:  # Ищем все заголовки, соответствующие тому, что мы будем вводить и считаем сколько таких
            a += 1
    for x in task_before:
        if x.text == task:  # Ищем все задачи, соответствующие тому, что мы будем вводить и считаем сколько таких
            b += 1

    context.driver.find_element_by_css_selector("img").click()  # Кликаем на кнопку "Создать новое задание"
    context.driver.find_element_by_id('select2-select_category-container').click()  # Кликаем на выпадающий список
    select = Select(context.driver.find_element_by_id('select_category'))  # Выбираем выпадающий список
    select.select_by_visible_text("Создать новый список")  # Находим в выпавшем списке пункт соответствующий тексту
    context.driver.find_element_by_id('select2-select_category-container').click()  # Кликаем на контейнер, чтобы выйти
    context.driver.find_element_by_id('project_title').click()  # Кликаем на поле "Заголовок"
    context.driver.find_element_by_id('project_title').send_keys(title)  # Вставляем текст в поле "Заголовок"
    context.driver.find_element_by_id('project_text').click()  # Кликаем на поле "Новая задача" -
    context.driver.find_element_by_id('project_text').send_keys(task)  # - Вставляем в него текст
    context.driver.find_element_by_id('submit_add_todo').click()  # Жмем кнопку ОК

    heading_after = context.driver.find_elements_by_tag_name('h2')  # Ищем все заголовки после теста
    task_after = context.driver.find_elements_by_tag_name('label')  # Ищем все задачи после теста
    а2 = 0
    b2 = 0
    for i2 in heading_after:
        if i2.text == title:  # Ищем все заголовки, соответствующие тому, что мы ввели и считаем сколько таких
            а2 += 1
            # print(title + " после теста стало: " + str(а2))
    for x2 in task_after:
        if x2.text == task:  # Ищем все задачи, соответствующие тому, что мы ввели и считаем сколько таких
            b2 += 1

    log = 0  # Сюда собираем ошибки
    if a == 0:
        if len(heading_before) + 1 != len(heading_after):  # Если не было заголовка, то должен появиться
            log += 1
    if a == 1:
        if len(heading_before) != len(heading_after):  # Если был заголовок, то число заголовков не изменится
            log += 1
    if a == 0 or a == 1:  # Если наших новых заголовков не было, то должен появится новый +1
        a = 1
        if a != а2 and (b + 1) != b2:  # Если были заголовки или был только 1 и не стало задач больше на +1
            log += 1
    if log != 0:
        print("T004.Ошибка!")
        raise NotImplementedError(u'STEP: Given я запускаю тест 004')
    else:
        print("T004.Всё хорошо!")

@given(u'я запускаю тест 005')
def step_impl(context):
    title = "Работа"  # Переменная для разных заголовков
    task = "Задача №4 Т005.py"  # Переменная для разных задач
    heading_before = context.driver.find_elements_by_tag_name('h2')  # Ищем все заголовки до теста
    task_before = context.driver.find_elements_by_tag_name('label') # Ищем все задачи до теста
    a=0
    b=0
    for i in heading_before:
        if i.text == title:  # Ищем все заголовки, соответствующие тому, что мы будем вводить и считаем сколько таких
            a += 1
    for x in task_before:
        if x.text == task:  # Ищем все задачи, соответствующие тому, что мы будем вводить и считаем сколько таких
            b += 1

    context.driver.find_element_by_css_selector("img").click()  # Кликаем на кнопку "Создать новое задание"
    context.driver.find_element_by_id('select2-select_category-container').click()  # Кликаем на выпадающий список
    select = Select(context.driver.find_element_by_id('select_category'))  # Выбираем выпадающий список
    select.select_by_visible_text("Работа")  # Находим в выпавшем списке пункт соответствующий тексту
    context.driver.find_element_by_id('select2-select_category-container').click()  # Кликаем на контейнер, чтобы выйти
    # driver.find_element_by_id('project_title').click(), t()  # Кликаем на поле "Заголовок"
    # driver.find_element_by_id('project_title').send_keys(title), t()  # Вставляем текст в поле "Заголовок"
    context.driver.find_element_by_id('project_text').click()  # Кликаем на поле "Новая задача" -
    context.driver.find_element_by_id('project_text').send_keys(task)  # - Вставляем в него текст
    context.driver.find_element_by_id('submit_add_todo').click()  # Жмем кнопку ОК

    heading_after = context.driver.find_elements_by_tag_name('h2')  # Ищем все заголовки после теста
    task_after = context.driver.find_elements_by_tag_name('label') # Ищем все задачи после теста
    а2=0
    b2=0
    for i2 in heading_after:
        if i2.text == title:  # Ищем все заголовки, соответствующие тому, что мы ввели и считаем сколько таких
            а2 += 1
            # print(title + " после теста стало: " + str(а2))
    for x2 in task_after:
        if x2.text == task:  # Ищем все задачи, соответствующие тому, что мы ввели и считаем сколько таких
            b2 += 1

    log = 0 # Сюда собираем ошибки
    if a == 0:
        if len(heading_before)+1 != len(heading_after): # Если не было заголовка, то должен появиться
            log += 1
    if a == 1:
        if len(heading_before) != len(heading_after): # Если был заголовок, то число заголовков не изменится
            log += 1
    if a == 0 or a == 1: # Если наших новых заголовков не было, то должен появится новый +1
        a = 1
        if a != а2 and (b+1) != b2: # Если были заголовки или был только 1 и не стало задач больше на +1
            log += 1
    if log != 0:
        print("T005.Ошибка!")
        raise NotImplementedError(u'STEP: Given я запускаю тест 005')
    else:
        print("T005.Всё хорошо!")
    if log != 0:
        print("T004.Ошибка!")
        raise NotImplementedError(u'STEP: Given я запускаю тест 004')
    else:
        print("T004.Всё хорошо!")