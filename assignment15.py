feedback={"positive":50,"Neutral":18,"Negative":7}
total=0
for value in feedback.values():
    total=total+value
highest=max(feedback,key=feedback.get)
print("Total Feedback:",total)
print("Highest feedback Type:",highest)
