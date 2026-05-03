def tareas_sobre_k(t,k):
   if len(t) == 0:
      return []
   est = t[0]
   promedio = sum(est[2])/len(est[2]) > k
   if promedio:
      return [est[0]] + tareas_sobre_k(t[1:],k)
   else:
      return tareas_sobre_k(t[1:],k)