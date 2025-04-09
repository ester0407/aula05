dintervalo=0
fintervalo=0
for n in range(10):
    num=int(input("digite o numero"))
    if num>=10 and num<=20:
        dintervalo= dintervalo+1
    else:
        fintervalo= fintervalo+1
print(f"dintervalo: {dintervalo}")
print(f"fintervalo: {fintervalo}")