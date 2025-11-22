import re
import urllib.request
import tiktoken
"""
Tokenizer Step
text ---> tokens ----> tokens ids
Byte Pair Encoding 
  break wods into subwords so that it is not needed to <|unk|> special token
"""
class Tokenizer:
    def __init__(self):
      self.tokenizer=tiktoken.get_encoding("gpt2")
    def encode(self,text):
     ids=self.tokenizer.encode(text,allowed_special={"<|endoftext|>"})
     return ids
    
def main(text):
    tokenizer=Tokenizer()
    ids=tokenizer.encode(text)
    print(ids)

   
if __name__:
   text="It's the last he painted , you know"
   main(text)