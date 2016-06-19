from gtts import gTTS

if __name__ == '__main__':

    for i in range(0, 22):
        for j in range(0, 22):
            if i == j:
                text = "{} partout".format(i)
            else:
                text = "{} à {}".format(i, j)

            tts = gTTS(text=text, lang='fr')
            tts.save("/home/thomas/sounds/{}_{}.mp3".format(i, j))


