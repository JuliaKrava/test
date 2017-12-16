# s=input("Vvedite: ")
# try:
#     s=int(s)
# except:
#     print("Error")

# try:
#     [1,2]/0
# except Exception as e:
#     print(e)

try:
    print(10/0)
except ZeroDivisionError:
    print(var)
finally:
    print('Ok')