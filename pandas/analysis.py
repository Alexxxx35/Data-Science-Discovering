import pandas as pd
#----- pandas settings -----
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
#----- format -----
pokecsv = pd.read_csv('pokemon_data.csv')
pokexls = pd.read_excel('pokemon_data.xlsx')
poketxt = pd.read_csv('pokemon_data.txt', delimiter='\t')
# print(pokecsv)
# print(pokexls)
# print(pokecsv.head(10))
# print(pokecsv.tail(5))

#----- access to columns -----
col=pokecsv.columns
# print(col)
first_10_names=pokecsv['Name'][0:10]
# print(first_10_names)
pokestats=pokecsv[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']]
# print(pokestats)

#----- access to rows and specific data -----
####3 data_acess methods :loc iloc ix
####df.loc[row,column]
ten_first_rows=pokecsv.iloc[0:10]
# print(ten_first_rows)
n_data_of_n_poke=pokecsv.iloc[2,2]
# print(n_data_of_n_poke)
specific_data_of_one_poke=pokecsv.loc[10,'HP']
# print(specific_data_of_one_poke)
all_stats_one_pokemon=pokecsv.iloc[0,:]
# print(all_stats_one_pokemon)
n_row_n_columns_data=pokecsv.iloc[1:10,1:10]
# print(n_row_n_columns_data)

#----- access to all data -----
# for index, row in pokecsv.iterrows():
		# print(index, row)
# for index, row in pokecsv.iterrows():
		# print(index, row['Name'])

#----- conditionnal access to data -----
#conditions must be separated with ()
#str method can contains regex
new_pokecsv=pokecsv.loc[(pokecsv['Type 1'] == "Grass") & (pokecsv['Type 2'] == "Poison") & (pokecsv['HP'] >= 100)]
new_pokecsv2=pokecsv.loc[pokecsv['Name'].str.contains('Mega')]
new_pokecsv3=pokecsv.loc[~pokecsv['Name'].str.contains('Mega')]
import re
find_Golem=pokecsv.loc[(pokecsv['Name'].str.contains('^Go[a-z]*', regex=True)) & (pokecsv['Type 2'] == 'Ground')]
# print(new_pokecsv)
# print(new_pokecsv2)
# print(new_pokecsv3)
# print(find_Golem)

#----- data modifications -----
#df.loc[df['col']== 'value', 'new col value modified'] = 'new value modified'
super_golem=pokecsv.loc[pokecsv['Name'] == 'Golem', 'Name'] = 'GreatGolem'
new_pokecsv4=pokecsv.loc[pokecsv['Name'].str.startswith('Gr')]
# print(super_golem)
# print(new_pokecsv4)

# ----- conditionnal data modifications -----
pokecsv.loc[pokecsv['HP']>=150, 'Legendary'] = 'Half True'
# print(conditionnal_pokecsv)
pokecsv.to_csv('test_data.csv',index=False)

#----- general stats on data -----
# print(pokecsv.describe())

#----- sort data -----
# sorted_data=pokecsv.sort_values(['HP'],ascending=False)
sorted_data2=pokecsv.sort_values(['Name','Speed'],ascending=[1,0])
# print(sorted_data)
# print(sorted_data2)

#----- create data -----
pokecsv['full_attack']=pokecsv['Attack']+pokecsv['Sp. Atk']
# print(pokecsv.head(5))

#=> : alone means all the rows
pokecsv['total_stats']=pokecsv.iloc[:,4:10].sum(axis=1)
# print(pokecsv.head(5))

#----- remove data -----
pokecsv=pokecsv.drop(columns=['full_attack'])
# print(pokecsv.head(5))

#----- move data -----
cols=list(pokecsv.columns.values)
#=>save the header
pokecsv=pokecsv[cols[0:2]+[cols[-1]]+cols[2:12]]
#=>convert the single col to insert into a list because if 1 column=>str
# print(pokecsv.head(5))


# pokecsv.to_csv('modified_data.csv',index=False)
# new_pokecsv.to_csv('filtered_data.csv',index=False)
# pokecsv.to_excel('modified_data.xlsx',index=False)

#----- reset data index -----
#drop remove the previous index as a new col
# pokecsv=pokecsv.reset_index(drop=True)
# print(pokecsv)

# ----- reset file data -----
pokecsv=pd.read_csv('pokemon_data.csv')
# ----- advanced search stats -----
average_per_type=pokecsv.groupby(['Type 1','Type 2']).mean()
sorted_stat_per_type=pokecsv.groupby(['Type 1']).mean().sort_values('HP',ascending=True)
# number_of_data=pokecsv.groupby(['Type 1']).count()
# print(average_per_type)
# print(sorted_stat_per_type)
# print(number_of_data)
sorted_stat_per_type.to_csv('stat_per_type.csv')
average_per_type.to_csv('average.csv')

pokecsv['count']=1
number_of_types=pokecsv.groupby(['Type 1']).count()['count']
print(number_of_types)
number_of_types.to_csv('number_of_types.csv')