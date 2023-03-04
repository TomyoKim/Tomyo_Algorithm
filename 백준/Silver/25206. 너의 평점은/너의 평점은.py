grade = {'A+' : 4.5,
         'A0' : 4.0,
         'B+' : 3.5,
         'B0' : 3.0,
         'C+' : 2.5,
         'C0' : 2.0,
         'D+' : 1.5,
         'D0' : 1.0, 
         'F' : 0.0
         }

result = 0
total = 0

for _ in range(0, 20, 1):
    input_data = input().split()
    if input_data[2] == 'P':
        continue
        
    total += float(input_data[1])
    result += float(input_data[1])*grade[input_data[2]]
    
gpa = result / total
conversion = format(gpa, '.6f')

print(conversion)