''' Tale of Two Cities '''

    # Import the required packages
from textblob import TextBlob
    # Create a textblob object
blob_two_cities = TextBlob(two_cities)
    # Print out the sentiment
print(blob_two_cities.sentiment)

from wordcloud import WordCloud
    # Generate the word cloud from the east_of_eden string
cloud_east_of_eden = WordCloud(background_color="white").generate(east_of_eden)
    # Create a figure of the generated cloud
plt.imshow(cloud_east_of_eden, interpolation='bilinear')
plt.axis('off')
    # Display the figure
plt.show()

my_cloud = WordCloud(background_color='white', stopwords=my_stopwords).generate(descriptions)
    # my_stopwords: string set
    # Display the generated wordcloud image
plt.imshow(my_cloud, interpolation='bilinear')
plt.axis("off")
    # Don't forget to show the final image
plt.show()
