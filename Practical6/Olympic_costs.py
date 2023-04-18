costs=[1,8,15,7,5,14,43,40] # create a list
costs=sorted(costs) # returns sorted costs
print(costs)
# make a bar plot
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

Olympic_Games = ['Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 1996','Athens 2003','Beijing 2008','London 2012']
ax.set_ylabel('costs')
ax.set_title('Olympic Costs') # make a title
plt.tick_params(axis='x',labelsize=8) #  change fontsize
plt.xticks(rotation=15) # rotate labels to show all of them
bar_container=ax.bar(Olympic_Games,costs)
ax.bar_label(bar_container,fmt='{:,.0f} $ billions')
plt.show()
