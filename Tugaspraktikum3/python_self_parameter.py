# ==========================================
# PYTHON SELF PARAMETER
# ==========================================

# Parameter 'self' adalah referensi ke *instance* (wujud/objek) dari class itu sendiri.
# Parameter ini digunakan untuk mengakses variabel yang menjadi milik class tersebut.
# Parameter ini TIDAK harus bernama 'self', Anda bisa menamainya apa saja sesuka Anda.
# TETAPI, ia harus selalu menjadi parameter PERTAMA dari fungsi apa pun di dalam class.

class Person:
  # Di sini kita menggunakan kata 'mysillyobject' dan 'abc' sebagai pengganti 'self'
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Halo, nama saya adalah " + abc.name)

p1 = Person("Fasbir", 25)
p1.myfunc() 
# Output: Halo, nama saya adalah Fasbir