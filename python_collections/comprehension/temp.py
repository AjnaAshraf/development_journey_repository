"""
Label numbers Input:[50,120,80,200,95]
Output:[“Low”,“High”,“Low”,“High”,“Low”]
"""

temp = [50,120,80,200,95]

new = ["low" if t<100 else "high" for t in temp]
print(new)