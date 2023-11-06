address = "192.168.01"
groups = address.split(".") #Divide la stringa basandosi sui punti
groups = [int(group) for group in groups] #Mi converte la lista in interi 
#groups = [group for group in groups] In questo caso non fa niente, perché ricopierebbe la lista nella lista stessa, quindi mettendo int li trasforma in interi avendo così la lista in interi.