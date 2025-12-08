import pandas as adu
# we have to ad one more \ to path because there will be 1 \ in the initail then path we be like below with \\
# dataframe = adu.read_csv('C:\\Users\\A plus\\Desktop\\1.B.tech\\AI ML\\toyota.csv',index_col='model')
# Index_col parameter
# this will set model column as a starting column

# Header parameter
# if there is no header there we give first rows as a header using either 0 or 1 
# dataframe = adu.read_csv('C:\\Users\\A plus\\Desktop\\1.B.tech\\AI ML\\toyota.csv', header=0)

dataframe = adu.read_csv('C:\\Users\\A plus\\Desktop\\1.B.tech\\AI ML\\toyota.csv',usecols=['model'])
print(dataframe)

# squeeze parameter 
# when we need only one columns , do squeeze = True
#  