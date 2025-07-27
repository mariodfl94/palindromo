a='lool'
cont=len(a)
b=[]
for i in range(cont - 1, -1, -1):
    b.append(a[i])
revertido = "".join(b)
print(a + " es: ", end="")
if a == revertido:
    print("Es palindromo:"+revertido)
else:
    print("No es palindromo:"+revertido)