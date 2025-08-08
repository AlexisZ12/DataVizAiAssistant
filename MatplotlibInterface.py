import matplotlib.pyplot as plt
import matplotlib
import numpy as np

MARKER = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_', 'P', 'X', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ' ']
LINESTYLE = ['-', ':', '--', '-.', ' ']
HATCHSTYLE = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*', ' ']
# COLOR = ['black', 'silver', 'gray', 'white', 'maroon', 'red', 'purple', 'fuchsia', 'green', 'lime', 'olive', 'yellow', 'navy', 'blue', 'teal', 'aqua']
COLOR = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'orange', 'pink']

matplotlib.rcParams['font.sans-serif']=['SimHei','Songti SC','STFangsong']
matplotlib.rcParams['axes.unicode_minus'] = False

def PlotInterface(X_value, Y_value, Y_value_label,
                  M_style, L_style, M_color, L_color,
                  X_min, X_max, X_step, Y_min, Y_max, Y_step,
                  X_label, Y_label, Title):
    n = len(Y_value)
    
    for i in range(n):
        plt.plot(
            X_value, Y_value[i],
            marker=MARKER[M_style[i]],
            markerfacecolor=COLOR[M_color[i]],
            linestyle=LINESTYLE[L_style[i]],
            color=COLOR[L_color[i]],
            label = Y_value_label[i]
        )
    
    plt.xticks(ticks=np.arange(X_min, X_max+1, X_step))
    plt.yticks(ticks=np.arange(Y_min, Y_max+1, Y_step))

    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)
    plt.legend()

    return plt

def ScatterInterface(X_value, Y_value,
                     color, size, alpha,
                     X_min, X_max, X_step, Y_min, Y_max, Y_step,
                     X_label, Y_label, Title):
    plt.scatter(X_value, Y_value, c=[COLOR[i] for i in color], s=size, alpha=alpha)

    plt.xticks(ticks=np.arange(X_min, X_max + 1, X_step))
    plt.yticks(ticks=np.arange(Y_min, Y_max + 1, Y_step))

    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)

    return plt

def BarInterface(X_value, Y_value, Y_value_label,
                 B_color, H_style,
                 X_min, X_max, X_step, Y_min, Y_max, Y_step,
                 X_label, Y_label, Title):
    n = len(Y_value)
    X_value = np.array(X_value)
    bar_width = 0.8 / n

    for i in range(n):
        plt.bar(
            X_value + ( i - ( n - 1 ) / 2 ) * bar_width, Y_value[i],
            width=bar_width,
            color=COLOR[B_color[i]],
            hatch=HATCHSTYLE[H_style[i]],
            label=Y_value_label[i]
        )

    plt.xticks(ticks=np.arange(X_min, X_max + 1, X_step))
    plt.yticks(ticks=np.arange(Y_min, Y_max + 1, Y_step))

    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)
    plt.legend()

    return plt

def StemInterface(X_value, Y_value, Y_value_label,
                  M_style, L_style, B_style, M_color, L_color, B_color,
                  X_min, X_max, X_step, Y_min, Y_max, Y_step,
                  X_label, Y_label, Title):
    n = len(Y_value)
    X_value = np.array(X_value)
    stem_width = 0.5 / n
    
    for i in range(n):
        plt.stem(
            X_value + ( i - ( n - 1 ) / 2 ) * stem_width, Y_value[i],
            markerfmt=MARKER[M_style[i]] + COLOR[M_color[i]],
            linefmt=LINESTYLE[L_style[i]] + COLOR[L_color[i]],
            basefmt=LINESTYLE[B_style[i]] + COLOR[B_color[i]],
            bottom=Y_min,
            label=Y_value_label[i]
        )
        
    plt.xticks(ticks=np.arange(X_min, X_max+1, X_step))
    plt.yticks(ticks=np.arange(Y_min, Y_max+1, Y_step))

    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)
    plt.legend()
    
    return plt

def FillBetweenInterface(X_value, Y_value_1, Y_value_2, Y_value_label,
                         Fill_color, Fill_alpha,
                         X_min, X_max, X_step, Y_min, Y_max, Y_step,
                         Title, X_label, Y_label,):
    plt.fill_between(
        X_value, Y_value_1, Y_value_2,
        color = COLOR[Fill_color],
        alpha = Fill_alpha,
        label = Y_value_label
    )

    plt.xticks(ticks=np.arange(X_min, X_max+1, X_step))
    plt.yticks(ticks=np.arange(Y_min, Y_max+1, Y_step))

    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)
    plt.legend()
    
    return plt

def StackplotInterface(X_value, Y_value, Y_value_label,
                       Fill_color, Fill_alpha,
                       X_min, X_max, X_step, Y_min, Y_max, Y_step,
                       Title, X_label, Y_label,):
    n = len(Y_value)

    for i in range(n):
        plt.stackplot(
            X_value, Y_value[i],
            colors = COLOR[Fill_color[i]],
            alpha = Fill_alpha[i],
            labels = Y_value_label[i],
        )

    plt.xticks(ticks=np.arange(X_min, X_max+1, X_step))
    plt.yticks(ticks=np.arange(Y_min, Y_max+1, Y_step))

    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)
    plt.legend()
    
    return plt

def StairsInterface(value, position, value_label,
                    color,
                    X_min, X_max, X_step, Y_min, Y_max, Y_step,
                    Title, X_label, Y_label,):
    n = len(value)

    for i in range(n):
        plt.stairs(
            value[i], position + [position[-1] + 1],
            color=COLOR[color[i]],
            label=value_label[i])
    
    plt.xticks(ticks=np.arange(X_min, X_max+1, X_step))
    plt.yticks(ticks=np.arange(Y_min, Y_max+1, Y_step))
    
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.title(Title)
    plt.legend()

    return plt