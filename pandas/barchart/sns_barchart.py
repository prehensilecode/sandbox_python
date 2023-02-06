#!/usr/bin/env python3
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# simple data
speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ['snail', 'pig', 'elephant', 'rabbit', 'giraffe', 'coyote', 'horse']

df = pd.DataFrame({'animal': index, 'speed': speed, 'lifespan': lifespan})
print(df)

sns.barplot(data=df, x='animal', y='speed', hue='lifespan')
plt.savefig('sns_animals_barchart.png')
plt.clf()

# more complex data
# set seed
np.random.seed(41)

#create three different normally distributed datasets
score_array_A_m = np.random.normal(size = 100, loc = 85, scale = 3)
score_array_A_f = np.random.normal(size = 100, loc = 90, scale = 2)
score_array_B_m = np.random.normal(size = 100, loc = 83, scale = 4)
score_array_B_f = np.random.normal(size = 100, loc = 80, scale = 7)
score_array_C_m = np.random.normal(size = 100, loc = 73, scale = 7)
score_array_C_f = np.random.normal(size = 100, loc = 80, scale = 2)

speed_array_A_m = np.random.normal(size = 100, loc = 15, scale = 3)
speed_array_A_f = np.random.normal(size = 100, loc = 17, scale = 2)
speed_array_B_m = np.random.normal(size = 100, loc = 13, scale = 4)
speed_array_B_f = np.random.normal(size = 100, loc = 12, scale = 5)
speed_array_C_m = np.random.normal(size = 100, loc = 18, scale = 5)
speed_array_C_f = np.random.normal(size = 100, loc = 21, scale = 8)


#turn normal datasets into dataframes
score_df_A_m = pd.DataFrame({'score':score_array_A_m,'class':'Class A', 'gender':'Male'})
score_df_A_f = pd.DataFrame({'score':score_array_A_f,'class':'Class A', 'gender':'Female'})
score_df_B_m = pd.DataFrame({'score':score_array_B_m,'class':'Class B', 'gender':'Male'})
score_df_B_f = pd.DataFrame({'score':score_array_B_f,'class':'Class B', 'gender':'Female'})
score_df_C_m = pd.DataFrame({'score':score_array_C_m,'class':'Class C', 'gender':'Male'})
score_df_C_f = pd.DataFrame({'score':score_array_C_f,'class':'Class C', 'gender':'Female'})

speed_df_A_m = pd.DataFrame({'speed':speed_array_A_m,'class':'Class A', 'gender':'Male'})
speed_df_A_f = pd.DataFrame({'speed':speed_array_A_f,'class':'Class A', 'gender':'Female'})
speed_df_B_m = pd.DataFrame({'speed':speed_array_B_m,'class':'Class B', 'gender':'Male'})
speed_df_B_f = pd.DataFrame({'speed':speed_array_B_f,'class':'Class B', 'gender':'Female'})
speed_df_C_m = pd.DataFrame({'speed':speed_array_C_m,'class':'Class C', 'gender':'Male'})
speed_df_C_f = pd.DataFrame({'speed':speed_array_C_f,'class':'Class C', 'gender':'Female'})

#concat dataframes together
score_df = pd.concat([score_df_A_m
                        ,score_df_A_f
                        ,score_df_B_m
                        ,score_df_B_f
                        ,score_df_C_m
                        ,score_df_C_f
                        ])

speed_df = pd.concat([speed_df_A_m
                        ,speed_df_A_f
                        ,speed_df_B_m
                        ,speed_df_B_f
                        ,speed_df_C_m
                        ,speed_df_C_f
                        ])

combo_df = pd.merge(score_df, speed_df)

print(score_df.head(3))
print(speed_df.head(3))
print(combo_df.head(3))

sns.barplot(data=score_df, x='class', y='score', errorbar=None)
plt.savefig('score_chart_1.png')
plt.clf()

sns.barplot(data=score_df, x='score', y='class', errorbar=None)
plt.savefig('score_chart_2.png')
plt.clf()

sns.barplot(data=score_df, x='score', y='class', hue='gender', errorbar=None)
plt.savefig('score_chart_3.png')
plt.clf()

sns.barplot(data=speed_df, x='speed', y='class', hue='gender', errorbar=None)
plt.savefig('score_chart_4.png')
plt.clf()

# create 2 charts and stack them
# yes, it's meaningless to stack speed & score
pass

