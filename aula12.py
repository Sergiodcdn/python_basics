##  LOOP FOR, associado como for it em outras linguagens

carros=["HRV", "Golf", "Argo", "Focus", "Fit", "Fusion", "Polo"]

##for x in ["HRV", "Golf", "Argo", "Focus"]:
##for x in "TETECO filhote":
##for x in carros:
for x in carros:
    print(x) ## se o print estiver depois não imprimiria o "Fit"
    if(x=="Fit"):
        break