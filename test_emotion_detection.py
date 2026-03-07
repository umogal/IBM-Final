import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        joy_text = 'I am glad this happened'
        result_joy = emotion_detector(joy_text)
        self.assertEqual(result_joy['dominant_emotion'], 'joy')

    def test_anger(self):
        anger_text = 'I am really mad about this'
        result_anger = emotion_detector(anger_text)
        self.assertEqual(result_anger['dominant_emotion'], 'anger')

    def test_disgust(self):
        disgust_text = 'I feel disgusted just hearing about this'
        result_disgust = emotion_detector(disgust_text)
        self.assertEqual(result_disgust['dominant_emotion'], 'disgust')

    def test_sadness(self):
        sadness_text = 'I am so sad about this'
        result_sadness = emotion_detector(sadness_text)
        self.assertEqual(result_sadness['dominant_emotion'], 'sadness')

    def test_fear(self):
        fear_text = 'I am really afraid that this will happen'
        result_fear = emotion_detector(fear_text)
        self.assertEqual(result_fear['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
