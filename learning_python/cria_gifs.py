# %%

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as fx
import matplotlib.animation as animation

# %%

flights = sns.load_dataset('flights')

# %%

# Criamos uma função que retorna os "plots" ou "frames" que queremos
def make_plot(year):

    # Filtramos os dados
    df = flights.loc[flights.year == year]

    # Geramos o plot
    fig, ax = plt.subplots(1, 1, sharey=True)
    # ax1.invert_xaxis()
    # fig.subplots_adjust(wspace=0)

    ax.barh(df.month, df.passengers, label='Passageiros')

    ax.set_xlim([0, 800])

    # Adicionamos os textos correspondentes
    fig.suptitle(f'Passageiros em voos ano {year}')
    # fig.supxlabel('Percentage of Population (%)')
    fig.legend(bbox_to_anchor=(0.9, 0.88), loc='upper right')
    ax.set_ylabel('Mês')

    # Add text to plot
    text = ax1.text(3.8, 18, str(year), fontsize=24, va='center', ha='left')
    text.set_path_effects([ fx.Stroke(linewidth=5, foreground='1.0'), fx.Normal()])

    return fig


# %%

years = [i for i in set(flights.year)]
years.sort()


for year in years:
    fig = make_plot(year)
    fig.savefig(f'figuras_para_gif/{year}.jpeg',bbox_inches = 'tight')

# %%

# Create new figure for GIF
fig, ax = plt.subplots()

# Adjust figure so GIF does not have extra whitespace
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
ax.axis('off')
ims = []

for year in years:
    im = ax.imshow(plt.imread(f'{year}.jpeg'), animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=600)
ani.save('us_population.gif')

# %%

# Sem salvar frames:
#Without saving frames

years = [i for i in set(data.Year) if i < 2022]
years.sort()

# Initialize plot
# Will be overwritten by run function
fig, (ax1, ax2) = plt.subplots(1, 2, sharey = True)

df = data[data.Year == 1955]

y_pos = [i for i in range(len(df[df.Sex == 'Male']))]
male = ax1.barh(y_pos, df[df.Sex == 'Male'].percent, label = 'Male',
               tick_label = df[df.Sex == 'Male'].AgeGrp)
female = ax2.barh(y_pos, df[df.Sex == 'Female'].percent, label = 'Female', 
                  color = 'C1', tick_label = df[df.Sex == 'Male'].AgeGrp)

ax1.invert_xaxis()

# Set limits so all plots have the same scales
ax1.set_xlim([6, 0])
ax2.set_xlim([0, 6])
ax1.set_ylim([-1, 21])

fig.suptitle('US Population Distribution')
fig.supxlabel('Percentage of Population (%)')
fig.legend(bbox_to_anchor = (0.9, 0.88), loc = 'upper right')
ax1.set_ylabel('Age Groups')

fig.subplots_adjust(wspace = 0)

# Add text to plot
text = ax1.text(3.8, 18, '', fontsize = 24, 
                va = 'center', ha = 'left')
text.set_path_effects([
    fx.Stroke(linewidth= 5, foreground = '1.0'),
    fx.Normal()])
    
def run(year):

    # Filter data
    df = data[data.Year == year]

    # Find percentage of population for each age group
    total_pop = df.Value.sum()
    df['percent'] = df.Value / total_pop * 100

    if len(male.patches) != len(df[df.Sex == 'Male']):
        male.remove()
        y_pos = [i for i in range(len(df[df.Sex == 'Male']))]
        male.patches = ax1.barh(y_pos, df[df.Sex == 'Male'].percent, label = 'Male', 
                         color = 'C0', tick_label = df[df.Sex == 'Male'].AgeGrp)

        female.remove()
        female.patches = ax2.barh(y_pos, df[df.Sex == 'Female'].percent, label = 'Female',
                          color = 'C1', tick_label = df[df.Sex == 'Female'].AgeGrp)

    else:
        for count, rect in zip(df[df.Sex == 'Male'].percent, male.patches):
            rect.set_width(count)

        for count, rect in zip(df[df.Sex == 'Female'].percent, female.patches):
            rect.set_width(count)

    text.set_text(year)

    return male#, female
    
ani = animation.FuncAnimation(fig, run, years, blit = True, repeat = True, 
                              interval = 600)
ani.save('us_population_from_funct.gif')