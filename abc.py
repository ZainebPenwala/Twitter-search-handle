from wordcloud import WordCloud
import matplotlib.pyplot as pPlot
import numpy as np
from PIL import Image

text=("pizza burger icecream chocolate pasta cheese mousse cake nuts fruits tea veggies rice tasty sandwhich noodles")

maskArray=np.array(Image.open("cloud.png"))

wordcloud=WordCloud(mask=maskArray,background_color='yellow').generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis('off')
plt.margins()
plt.show()
