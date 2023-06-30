import math
import funcs as *


global_choice = input('Вычисления чего вы хотите? ч - числа/ гф - геометр. фигуры: ')

try:
    if global_choice == 'ч':
        user_action = (input(
            'Округление до ближаешего большего числа: ceil, \n Факториал числа: factorial, \n Округление вниз: floor, \n Является ли x числом: isfinite, \n Степень: exp, \n Квадатный корень: sqrt, \n Сложение: +, \n Вычитание: -, \n Умножение: *, \n Деление: /, \n Что вы выберете? '))
        if user_action == 'ceil':
            ceil_num = float(
            input('Введите число с ДЕСЯТИЧНОЙ точкой которое хотите округлить вверх: '))
            print(math.ceil(ceil_num))

        elif user_action == 'factorial':
            factorial_num = int(
                input('Введите число для нахождения его факториала: '))
            print(math.factorial(factorial_num))

        elif user_action == 'floor':
            floor_num = float(
            input('Введите число с ДЕСЯТИЧНОЙ точкой которое хотите округлить вниз: '))
            print(math.floor(floor_num))

        elif user_action == 'isfinite':
            isfinite_num = int(
                input('Введите число которое хотите проверить: '))
            print(math.isfinite(isfinite_num))

        elif user_action == 'exp':
            exp_num1 = int(
                input('Введите первое число: '))
            exp_num2 = int(
                input('Введите второе число: '))
            print(exp_num1 ** exp_num2)

        elif user_action == 'sqrt':
            sqrt_num = int(
                input('Введите число квадратный корень которого вы хотите проверить: '))
            print(math.sqrt(sqrt_num))

        elif user_action == '+':
            plus_num1 = int(input('Введите первое число: '))
            plus_num2 = int(input('Введите второе число: '))
            print(plus_num1 + plus_num2)

        elif user_action == '-':
            minus_num1 = int(input('Введите первое число: '))
            minus_num2 = int(input('Введите второе число: '))
            print(minus_num1 - minus_num2)

        elif user_action == '*':
            times_num1 = int(input('Введите первое число: '))
            times_num2 = int(input('Введите второе число: '))
            print(times_num1 * times_num2)

        elif user_action == '/':
            minustimes_num1 = int(input('Введите первое число: '))
            minustimes_num2 = int(input('Введите второе число: '))
        else:
            print('Error')
            
    if global_choice == 'гф':
        choice = input(
        "Введите фигуру для вычисления (сантиметры); к - квадрат/ п - прямоуголник/ т - треугольник/ пара - параллелепипед(прямоугольный): \n")
        if choice == 'п':
            choice_for_type = input("Периметр или площадь?; площадь/периметр: ")
            a = int(input('Введите длину: '))
            b = int(input('Введите ширину: '))
            if choice_for_type == 'периметр':
                perimetr_rectangle(a, b)
            if choice_for_type == 'площадь':
                area_rectangle(a, b)
        
        if choice == 'к':
            choice_for_type = input("Периметр или площадь?; периметр/площадь: ")
            a = int(input('Введите длину стороны: '))
            if choice_for_type == 'периметр':
                perimetr_square(a)
            if choice_for_type == 'площадь':
                area_square(a)

        if choice == 'т':
            a = int(input('Введите a (периметр): '))
            b = int(input('Введите b: '))
            c = int(input('Введите c: '))
            periment_triangle(a, b, c)

        if choice == 'пара':
            choice_for_type = input('Периметр или площадь?; периметр/площадь: ')
            print("Введите три ребра: ")
            a = int(input('Введите a: '))
            b = int(input('Введите b: '))
            c = int(input('Введите c: '))
            if choice_for_type == 'площадь':
                surface_area_parallelepiped(a, b, c)
            if choice_for_type == 'периметр':
                perimetr_parallelepiped(a, b, c)
 
except Exception as e:
    print(f'ERROR! ERROR! ERROR!! ERROR!! ERROR!!!{e}')
