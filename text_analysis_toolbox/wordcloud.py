from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
 
def color_func(word, font_size, position, orientation, random_state, font_path):
    return 'darkturquoise'
    
def get_wordcloud(lda_model):
    fig, axs = plt.subplots(ncols=4, nrows=int(lda_model.num_topics/4), figsize=(15,7))
    axs = axs.flatten()
 
    for i, t in enumerate(range(lda_model.num_topics)):
 
        x = dict(lda_model.show_topic(t, 30))
        im = WordCloud(
            #font_path='./ipag.ttf',
            background_color='white',
            color_func=color_func,
            #mask=mask,
            random_state=0
        ).generate_from_frequencies(x)
        axs[i].imshow(im)
        axs[i].axis('off')
        axs[i].set_title('Topic '+str(t))
        
    plt.tight_layou