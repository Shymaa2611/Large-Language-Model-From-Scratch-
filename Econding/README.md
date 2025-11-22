# ENCODING
Convert data into vector format

## Steps :
1- Tokenizer : split text into tokens
2- convert tokens into tokens ids
3- embedding 

## Tokenizer_V01
 1- Simple Tokenizer split txet into tokens 
 2- convert tokens into tokens ids using encoding function

## Tokenizer_V02
 - Solve problem of out of vocablary in Tokenizer_V01 using special tokens ["<|unk|>","<|endoftext|>"] 
  <|unk|>   ---> refer to unknow token or token is not in vocab
  <|endoftext|>  ---> separate between unrelated text sources

## Byte Bair Encoding
Break words into subwords units