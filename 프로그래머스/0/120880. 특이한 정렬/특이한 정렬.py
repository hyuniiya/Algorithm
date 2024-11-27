def solution(numlist, n):
   distance_list = []
   for x in numlist:
       distance = abs(x - n)
       distance_list.append((distance, x))
   
   distance_list.sort(key=lambda x: (x[0], -x[1]))
   
   result = []
   for _, num in distance_list:
       result.append(num)
   
   return result
