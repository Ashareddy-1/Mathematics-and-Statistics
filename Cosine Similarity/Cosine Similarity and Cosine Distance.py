import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances
similarity = cosine_similarity([[3,1]],[[6,2]])
print(similarity)
distance = cosine_distances([[3,1]], [[6,2]])
print(distance)

doc1 = """
iphone sales contributed to 70% of revenue. iphone demand is increasing by 20% yoy. 
the main competitor phone galaxy recorded 5% less growth compared to iphone"
"""

doc2 = """
The upside pressure on volumes for the iPhone 12 series, historical outperformance 
in the July-September time period heading into launch event, and further catalysts in relation
to outperformance for iPhone 13 volumes relative to lowered investor expectations implies a 
very attractive set up for the shares.
"""

doc3 = """
samsung's flagship product galaxy is able to penetrate more into asian markets compared to
iphone. galaxy is redesigned with new look that appeals young demographics. 60% of samsung revenues
are coming from galaxy phone sales
"""

doc4 = """
Samsung Electronics unveils its Galaxy S21 flagship, with modest spec improvements 
and a significantly lower price point. Galaxy S21 price is lower by ~20% (much like the iPhone 12A), 
which highlights Samsung's focus on boosting shipments and regaining market share.
"""

df = pd.DataFrame([
        {'iPhone': 3,'galaxy': 1},
        {'iPhone': 2,'galaxy': 0},
        {'iPhone': 1,'galaxy': 3},
        {'iPhone': 1,'galaxy': 2},
    ],
    index=[
        "doc1",
        "doc2",
        "doc3",
        "doc4"
    ])

print(df)

comparision_case_1=cosine_similarity(df.loc["doc1":"doc1"],df.loc["doc2":"doc2"])
print(comparision_case_1)
comparision_case_2=cosine_similarity(df.loc["doc1":"doc1"],df.loc["doc3":"doc3"])
print(comparision_case_2)
comparision_case_3=cosine_similarity(df.loc["doc3":"doc3"],df.loc["doc4":"doc4"])
print(comparision_case_3)
comparision_case_4=cosine_similarity(df.loc["doc1":"doc1"],df.loc["doc4":"doc4"])
print(comparision_case_4)
comparision_case_5=cosine_distances(df.loc["doc1":"doc1"],df.loc["doc4":"doc4"])
print(comparision_case_5)
