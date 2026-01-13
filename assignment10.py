opening_stock=[100,40,50,400]
closing_stock=[150,400,560,300]
products=["product A","product B","product C","product D"]
print("inventory stock comparison")
for i in range(len(opening_stock)):
      if opening_stock[i]>closing_stock[i]:
         product="incresed"
      elif opening_stock[i]<closing_stock[i]:
         product="reduced"
      else:
         product="no change"
print(f"{products[i]}:opening={opening_stock[i]},closing={closing_stock[i]}->{product}")
             
    
