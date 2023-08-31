var1 = "hello world"
var2 = "hello planet"
var3 = ""
even = " is even"
odd = " is odd"

if len(var1) % 2 == 0:
    var1 += even
elif len(var1) % 2 != 0:
    var1 += odd
if len(var2) % 2 == 0:
    var2 += even
elif len(var2) % 2 != 0:
    var2 += odd
if len(var3) % 2 == 0:
    var3 += even
elif len(var3) % 2 != 0:
    var3 += odd

print(var1, var2, var3, sep='\f')