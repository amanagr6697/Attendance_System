
def remove(name):
  yo=""
  for i in range(len(name)):
      if (name[i]=='-' or name[i]==' ' or name[i]==':'):
       pass
      else:
       yo+=str(name[i])
  return yo
   

name="2021-11-13 23:30:38.419951"
yo=remove(name)
print(yo)