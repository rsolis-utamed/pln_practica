import re
import spacy
import nltk
from nltk.corpus import stopwords

class Preprocessor():
  """
  Esta clase realiza el preprocesamiento de un texto, aplicando los siguientes pasos en orden:
  1. Pasar a minúsculas.
  2. Eliminar caracteres especiales, números y URLs.
  3. Tokenizar el texto.
  4. Lematizar el texto.
  5. Eliminar stop words.
  """
  def __init__(self,nlp,manual_stop_words=[]):
    self.manual_stop_words=manual_stop_words
    self.nlp=nlp
    
  
  def __step1_toLowerParse(self,text):
        print("   Parsing to lower...")
        self.text=str(self.text).lower()
        return self.text
         
  def __step2_applyRegExpressions(self,text):
      print("   Applying regular expresions...") 
      self.text = re.sub(r'http\S+|www\S+|https\S+', '', self.text, flags=re.MULTILINE)
      self.text = re.sub(r'\@\w+|\#', '', self.text)
      self.text = re.sub(r'[^\w\s]', '', self.text)
      self.text = re.sub(r'\d+', '', self.text)
      return self.text
    
  def __step_3_toTokenize(self,text):
      print("   Tokenizing text...")
      self.tokens = self.nlp(self.text)
      return self.tokens
  
  def __step4_toLemmantize(self,tokens):
      print("   Lemmantizing text...")
      self.lemmantized_tokens = [token.lemma_ for token in self.tokens]
      return self.lemmantized_tokens
         
  def __step_5_delStopWords(self,lemmantized_tokens, manual_stop_words=[]):
      print("   Deleting stop words in text...")
      stop_words_es = set(stopwords.words('spanish')).union(set(manual_stop_words))
      self.clean_tokens = [t for t in self.lemmantized_tokens if t not in stop_words_es and len(t) > 2]
      return " ".join(self.clean_tokens)
        
  def toPreprocessText(self,text):
      self.text=text
      self.text=self.__step1_toLowerParse(self.text)
      self.text=self.__step2_applyRegExpressions(self.text)
      self.tokens=self.__step_3_toTokenize(self.text)
      self.lemmantized_tokens=self.__step4_toLemmantize(self.tokens)
      self.clean_tokens=self.__step_5_delStopWords(self.lemmantized_tokens)
      return self.clean_tokens
      




