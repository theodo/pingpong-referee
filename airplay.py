from gtts import gTTS

if __name__ == '__main__':

    for i in range(0, 22):
        for j in range(0, 22):
            if i == j:
                text = "{} all".format(i)
            else:
                text = "{} to {}".format(i, j)

            tts = gTTS(text=text, lang='en')
            tts.save("/home/thomas/airplay/sounds_en/{}_{}.mp3".format(i, j))
