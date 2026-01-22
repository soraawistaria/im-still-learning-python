#tugas dari pacarku

tugass = []
nomor = 1
while True:
    tugas = input(f"Tugas {nomor} : ").lower()
    if tugas == "q" :
        break
    else:
        tugass.append(tugas)
        nomor+=1

print("----------TO DO LIST----------")
for i in tugass:
    print(f"😉. {i}")
    

print("=========================")
for x in tugass:
    done = input(f"{x} selesai y/n? ").lower()
    if done == "n" :
        print("Kerjain ya sayang!")
    elif done == "y":
        continue