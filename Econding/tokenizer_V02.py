import re
import urllib.request

"""
Tokenizer Step
text ---> tokens ----> tokens ids
<|unk|>  ---> refer to words that is not vocab
<|endoftext|> separate between inrelated text sources
"""
class Tokenizer:
    def __init__(self,vocab):
        self.str_to_int=vocab
        self.int_to_str={i:s for s,i in vocab.items()}

    def encode(self,text):
      preprocessed=re.split(r'([,.?_!"()\']|--|/s)',text)
      preprocessed=[
         item.strip() for item in preprocessed if item.strip()
      ]
      preprocessed=[ item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
      
      ids = [self.str_to_int[s] for s in preprocessed]
      return ids

def main(text):
    url = (
    "https://raw.githubusercontent.com/rasbt/"
    "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
    "the-verdict.txt"
)
    file_path="the-verdict.txt"
    urllib.request.urlretrieve(url,file_path)
    with open("the-verdict.txt","r",encoding="utf-8") as f:
        raw_text=f.read()
    preprocessed=re.split(r'([,.?_!"()\']|--|/s)',raw_text)
    preprocessed=[item.strip() for item in preprocessed if item.strip()]
    all_words=sorted(list(set(preprocessed)))
    all_words.extend(["<|endoftext|>","<|unk|>"])
    vocab={token:id for id,token in enumerate(all_words)}
    tokenizer=Tokenizer(vocab)
    ids=tokenizer.encode(text)
    print(ids)

   
if __name__:
   text1="Hello , do you like tea?"
   text2="In the sunlit terraces of the palace."
   text="<|endoftext|>".join((text1,text2))
   main(text)