def AnaliseAnagram(s):
      
    # Retorna o número totral de anagramas
    # substrings in s
    n = len(s)
    mp = dict()
      
    #loop para o tamanho total da substring
    for i in range(n):
        sb = ''
        for j in range(i, n):
            sb = ''.join(sorted(sb + s[j]))
            mp[sb] = mp.get(sb, 0)
              
            #incrementa no dict
            mp[sb] += 1
  
    anas = 0
      
    # loop em todos os dic diferentes
    # items e count das substring 
    for k, v in mp.items():
        anas += (v*(v-1))//2
    return anas
  

