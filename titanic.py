import pandas as pd


def get_name(value, world_delimiter=' '):
    sep_index = value.find('(')
    if sep_index >= 0:
        start_index = sep_index + 1
        end_index = value.find(world_delimiter, start_index)

        return value[start_index:end_index]

    sep_index = value.find('.')
    start_index = sep_index + 2
    end_index = value.find(world_delimiter, start_index)

    if end_index < 0:
        end_index = len(value) + 1

    return value[start_index:end_index]


def get_most_freq_name(df):
    return df['Name'].apply(get_name).value_counts().idxmax()


if __name__ == '__main__':
    data = pd.read_csv('train.csv')

    alive = data.loc[data['Survived'] == 1]
    alive_man = alive.loc[data['Sex'] == 'male']
    alive_woman = alive.loc[data['Sex'] == 'female']
    dead = data.loc[data['Survived'] == 0]
    dead_man = dead.loc[data['Sex'] == 'male']
    dead_woman = dead.loc[data['Sex'] == 'female']

    most_freq_alive_woman_name = get_most_freq_name(alive_woman)
    most_freq_dead_woman_name = get_most_freq_name(dead_woman)
    most_freq_alive_man_name = get_most_freq_name(alive_man)
    most_freq_dead_man_name = get_most_freq_name(dead_man)

    print('Most freq alive woman name: {}'.format(most_freq_alive_woman_name))
    print('Most freq dead woman name: {}'.format(most_freq_dead_woman_name))
    print('Most freq alive man name: {}'.format(most_freq_alive_man_name))
    print('Most freq dead man name: {}'.format(most_freq_dead_man_name))
