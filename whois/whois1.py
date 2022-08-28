import whois
dominio = raw_input("ALVO: ")
consulta_whois = whois.whois(dominio)

#print consulta whois.name
print consulta_whois.dayfirst


#https://pypi.org/project/python-whois/#files


