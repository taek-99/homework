pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject, day, title = None):
    global pro_num
    pro_num += 1
    
    data = {}   
    data['과목'] = subject
    data['일차'] = day
    data['제목'] = title
    data['문제번호'] = pro_num

    return data


result_1 = create_data('python', 3)
result_2 = create_data('web', 1, 'web 엽습하기')
result_3 = create_data(**global_data)

print (result_1)
print (result_2)
print (result_3)