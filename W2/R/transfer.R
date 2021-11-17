data = read.csv("test.tsv",header=T,sep="\t")
ens = data$ENSEMBL
ens
# enssemble to gene symbol

library('org.Hs.eg.db')

symbol <- select(org.Hs.eg.db, keys=ens, columns = 'SYMBOL', keytype = 'ENSEMBL')

symbol = symbol$SYMBOL