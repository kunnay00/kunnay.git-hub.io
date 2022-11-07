# Tugas 1 Algoritma dan Pemrograman
# Membuat program python untuk menghitung Body Mass Index (BMI) seseorang
# Oleh: Kunny Masrukhati (222410102047)


print('      ')
print('=============================')
print('====== PERHITUNGAN BMI ======')
print('=============================')
print('      ')

a = float(input('Masukkan berat badan (kg) anda-!'))
b = float(input('Masukkan tinggi badan (m) anda-!'))
print('      ')

print('Apakah anda yakin data yang anda masukkan sudah benar-?')
print('1. Ya')
print('2. Tidak')
Operator = int(input('Tuliskan angkanya saja-!'))

opsi = [1, 2]
if Operator not in opsi:
    print('      ')
    print('Input hanya berupa angka yang tersedia di opsi-!')
    exit(1)

BMI = a/b**2
x = BMI

print('      ')
if Operator == 1:
    print('Hasil BMI anda:')
    print(BMI)

    x = BMI
    if x < 18.5:
        print('Underweight')
    elif x > 18.5 and x < 24.9:
        print('Normal weight')
    elif x > 24.9 and x < 30.0:
        print('Overweight')
    elif x > 30.0 and x < 34.9:
        print('Obesity class I')
    elif x > 34.9 and x < 39.9:
        print('Obesity class II')
    elif x > 40.0:
        print('Obesity class III')

elif Operator == 2:
    exit(1)

print('      ')
print('Terimakasih telah menggunakan program saya >.<')
print('      ')
    