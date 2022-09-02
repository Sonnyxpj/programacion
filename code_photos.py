def tamaño(immagen):
    l =immagen.readline().rstrip("\n")
    print(l)


if __name__ == "__main_":
    immagen = open("auto.pgm","r")
    tamaño(immagen)
    immagen.close()