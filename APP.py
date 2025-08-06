from openai import OpenAI
import json
import MatplotlibInterface
import io
from pywebio.input import *
from pywebio.output import *

with open('config/configExample.json', 'r', encoding = 'utf-8') as jsExample:
    jsEx = json.load(jsExample)
OpenAiConfigExample = jsEx['OpenAiConfigExample']
DeepSeekConfigExample = jsEx['DeepSeekConfigExample']
OllamaConfigExample = jsEx['OllamaConfigExample']
LmStudioConfigExample = jsEx['LmStudioConfigExample']

with open('prompt/a/prompt1a.txt', 'r', encoding='utf-8') as file:
    prompt1a = file.read()
with open('prompt/b/prompt1b.txt', 'r', encoding='utf-8') as file:
    prompt1b = file.read()
with open('prompt/a/prompt2a0.txt', 'r', encoding='utf-8') as file:
    prompt2a0 = file.read()
with open('prompt/a/prompt2a1.txt', 'r', encoding='utf-8') as file:
    prompt2a1 = file.read()
with open('prompt/a/prompt2a2.txt', 'r', encoding='utf-8') as file:
    prompt2a2 = file.read()
with open('prompt/a/prompt2a3.txt', 'r', encoding='utf-8') as file:
    prompt2a3 = file.read()
with open('prompt/a/prompt2a4.txt', 'r', encoding='utf-8') as file:
    prompt2a4 = file.read()
with open('prompt/a/prompt2a5.txt', 'r', encoding='utf-8') as file:
    prompt2a5 = file.read()
with open('prompt/a/prompt2a6.txt', 'r', encoding='utf-8') as file:
    prompt2a6 = file.read()
with open('prompt/b/prompt2b0.txt', 'r', encoding='utf-8') as file:
    prompt2b0 = file.read()
with open('prompt/b/prompt2b1.txt', 'r', encoding='utf-8') as file:
    prompt2b1 = file.read()
with open('prompt/b/prompt2b2.txt', 'r', encoding='utf-8') as file:
    prompt2b2 = file.read()
with open('prompt/b/prompt2b3.txt', 'r', encoding='utf-8') as file:
    prompt2b3 = file.read()
with open('prompt/b/prompt2b4.txt', 'r', encoding='utf-8') as file:
    prompt2b4 = file.read()
with open('prompt/b/prompt2b5.txt', 'r', encoding='utf-8') as file:
    prompt2b5 = file.read()
with open('prompt/b/prompt2b6.txt', 'r', encoding='utf-8') as file:
    prompt2b6 = file.read()
with open('prompt/a/prompt3a0.txt', 'r', encoding='utf-8') as file:
    prompt3a0 = file.read()
with open('prompt/a/prompt3a1.txt', 'r', encoding='utf-8') as file:
    prompt3a1 = file.read()
with open('prompt/a/prompt3a2.txt', 'r', encoding='utf-8') as file:
    prompt3a2 = file.read()
with open('prompt/a/prompt3a3.txt', 'r', encoding='utf-8') as file:
    prompt3a3 = file.read()
with open('prompt/a/prompt3a4.txt', 'r', encoding='utf-8') as file:
    prompt3a4 = file.read()
with open('prompt/a/prompt3a5.txt', 'r', encoding='utf-8') as file:
    prompt3a5 = file.read()
with open('prompt/a/prompt3a6.txt', 'r', encoding='utf-8') as file:
    prompt3a6 = file.read()
with open('prompt/b/prompt3b0.txt', 'r', encoding='utf-8') as file:
    prompt3b0 = file.read()
with open('prompt/b/prompt3b1.txt', 'r', encoding='utf-8') as file:
    prompt3b1 = file.read()
with open('prompt/b/prompt3b2.txt', 'r', encoding='utf-8') as file:
    prompt3b2 = file.read()
with open('prompt/b/prompt3b3.txt', 'r', encoding='utf-8') as file:
    prompt3b3 = file.read()
with open('prompt/b/prompt3b4.txt', 'r', encoding='utf-8') as file:
    prompt3b4 = file.read()
with open('prompt/b/prompt3b5.txt', 'r', encoding='utf-8') as file:
    prompt3b5 = file.read()
with open('prompt/b/prompt3b6.txt', 'r', encoding='utf-8') as file:
    prompt3b6 = file.read()
with open('prompt/a/prompt4a.txt', 'r', encoding='utf-8') as file:
    prompt4a = file.read()
with open('prompt/b/prompt4b.txt', 'r', encoding='utf-8') as file:
    prompt4b = file.read()
with open('prompt/a/prompt5a.txt', 'r', encoding='utf-8') as file:
    prompt5a = file.read()
with open('prompt/b/prompt5b.txt', 'r', encoding='utf-8') as file:
    prompt5b = file.read()
with open('prompt/a/prompt_newa1.txt', 'r', encoding='utf-8') as file:
    prompt_newa1 = file.read()
with open('prompt/a/prompt_newa2.txt', 'r', encoding='utf-8') as file:
    prompt_newa2 = file.read()
with open('prompt/b/prompt_newb1.txt', 'r', encoding='utf-8') as file:
    prompt_newb1 = file.read()
with open('prompt/b/prompt_newb2.txt', 'r', encoding='utf-8') as file:
    prompt_newb2 = file.read()
    
"""
根据用户的需求分析需要画出哪种图表，给出你的选择，根据提供的格式和要求返回成json格式

### 格式：
包含1个字段id，其中id为int类型

### 要求：
id为选择的图表类型的编号
如果用户选择了图表类型则按照用户选择的图表类型对应的id返回，否则请你选择你认为合适的图表类型
参照下面的对应表来选择，返回对应类型的id

#### type：
id | 函数 | 生成的图形 | 特点 |
--- |---|---|---|---|
0 | plot(x, y) | 线形图 | 展示数据的变化趋势或连续的数据 |
1 | scatter(x, y) | 散点图 | 展示变量间的关系，适合发现离群点和相关性 |
2 | bar(x, height) | 条形图 | 比较不同类别的数据量，适合分类数据展示 |
3 | stem(x, y) | 茎叶图（垂直线和数据点的结合）| 展示离散数据点，结构清晰，适合波动展示 |
4 | fill_between(x, y1, y2) | 填充区域图 | 填充曲线间的区域，展示数据区间和不确定性 |
5 | stackplot(x, y) | 堆叠区域图 | 展示多个数据序列随时间或其他变量的变化 |
6 | stairs(values) | 阶梯图 | 显示数据的跳跃变化，常用于步进或分段数据 |

### 用户需求：
"""

"""
根据用户的需求分析需要画出哪种图表，给出你的选择，想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段id，thought和reason，id为int类型，thought和reason为string类型

### 要求：
id为选择的图表类型的编号，thought为你的分析思路，reason为你的选择原因
如果用户选择了图表类型则按照用户选择的图表类型对应的id返回，否则请你选择你认为合适的图表类型
参照下面的对应表来选择，返回对应类型的id
先给出thought和reason，再给出id

#### type：
id | 函数 | 生成的图形 | 特点 |
--- |---|---|---|---|
0 | plot(x, y) | 线形图 | 展示数据的变化趋势或连续的数据 |
1 | scatter(x, y) | 散点图 | 展示变量间的关系，适合发现离群点和相关性 |
2 | bar(x, height) | 条形图 | 比较不同类别的数据量，适合分类数据展示 |
3 | stem(x, y) | 茎叶图（垂直线和数据点的结合）| 展示离散数据点，结构清晰，适合波动展示 |
4 | fill_between(x, y1, y2) | 填充区域图 | 填充曲线间的区域，展示数据区间和不确定性 |
5 | stackplot(x, y) | 堆叠区域图 | 展示多个数据序列随时间或其他变量的变化 |
6 | stairs(values) | 阶梯图 | 显示数据的跳跃变化，常用于步进或分段数据 |

### 用户需求：
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段x，y和ylabel，其中x为一维数组，y为二维数组，ylabel为一维数组
x和y均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据，根据提供的格式和要求返回成json格式

### 格式：
包含2个字段x和y，其中x和y均为一维数组
x和y均为int或float类型
json数据中不要添加注释

### 要求：
x和y的各自的第n项表示第n个点的x轴坐标和y轴坐标
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段x，y和ylabel，其中x为一维数组，y为二维数组，ylabel为一维数组
x和y均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段x，y和ylabel，其中x为一维数组，y为二维数组，ylabel为一维数组
x和y均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段x，y1，y2和ylabel，其中x，y1和y2为一维数组，ylabel为单个字符串
x，y1和y2均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
x为自变量，y1和y2为两个不同的因变量，ylabel为数据对象的标签，x，y1和y2的大小均为n
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段x，y和ylabel，其中x为一维数组，y为二维数组，ylabel为一维数组
x和y均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段position，value和label，其中position为一维数组，value为二维数组，label为一维数组
value为int或float类型，position为int类型且为连续递增的整数，label为string类型
json数据中不要添加注释

### 要求：
position为自变量，value为因变量，label为数据对象的标签，position的大小为n，value的大小为m行n列，label的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段x，y，ylabel，thought和reason，其中x为一维数组，y为二维数组，ylabel为一维数组
x和y均为int或float类型，ylabel，thought和reason为string类型
json数据中不要添加注释

### 要求：
x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数，thought为你的分析思路，reason为你的选择原因
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段x，y，thought和reason，其中x和y为一维数组
x和y为int或float类型，thought和reason为string类型
json数据中不要添加注释

### 要求：
x和y的各自的第n项表示第n个点的x轴坐标和y轴坐标，thought为你的分析思路，reason为你的选择原因
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段x，y，ylabel，thought和reason，其中x为一维数组，y为二维数组，ylabel为一维数组
x和y均为int或float类型，ylabel，thought和reason为string类型
json数据中不要添加注释

### 要求：
x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数，thought为你的分析思路，reason为你的选择原因
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段x，y，ylabel，thought和reason，其中x为一维数组，y为二维数组，ylabel为一维数组
x和y均为int或float类型，ylabel，thought和reason为string类型
json数据中不要添加注释

### 要求：
x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数，thought为你的分析思路，reason为你的选择原因
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含6个字段x，y1，y2，ylabel，thought和reason，其中x，y1和y2为一维数组，ylabel为单个字符串
x，y1和y2均为int或float类型，ylabel，thought和reason为string类型
json数据中不要添加注释

### 要求：
x为自变量，y1和y2为两个不同的因变量，ylabel为数据对象的标签，x，y1和y2的大小均为n，thought为你的分析思路，reason为你的选择原因
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段x，y和ylabel，thought和reason，其中x为一维数组，y为二维数组，ylabel为一维数组
x和y均为int或float类型，ylabel，thought和reason为string类型
json数据中不要添加注释

### 要求：
x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数，thought为你的分析思路，reason为你的选择原因
如果数据缺失则设置为空 
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段position，value，label，thought和reason，其中position为一维数组，value为二维数组，label为一维数组
value为int或float类型，position为int类型且为连续递增的整数，label，thought和reason为string类型
json数据中不要添加注释

### 要求：
position为自变量，value为因变量，label为数据对象的标签，position的大小为n，value的大小为m行n列，label的大小为m，m为数据对象的个数，thought为你的分析思路，reason为你的选择原因
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的需求设计图表样式，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段marker，linestyle，mcolor和lcolor，这4个字段均为一维int数组
json数据中不要添加注释

### 要求：
marker，linestyle，mcolor和lcolor的大小都为m，m为数据对象的个数
marker为点的形状，linestyle为线的形状，mcolor为点的颜色，lcolor为线的颜色
参考下面这个对应表来设计，返回对应的形状和颜色的id，如果用户没有提出形状和颜色，则选择一个你认为合适的形状和颜色，使图表整洁美观，如无特殊说明同一数据对象的mcolor和lcolor相同，不同数据对象的marker和linestyle相同

#### marker：
id | marker | name |
---|---|---|
0 | . | point |
1 | , | pixel |
2 | o | circle |
3 | v | triangle_down |
4 | ^ | triangle_up |
5 | < | triangle_left |
6 | > | triangle_right |
7 | 1 | tri_down |
8 | 2 | tri_up |
9 | 3 | tri_left |
10 | 4 | tri_right |
11 | 8 | octagon |
12 | s | square |
13 | p | pentagon |
14 | * | star |
15 | h | hexagon1 |
16 | H | hexagon2 |
17 | + | plus |
18 | x | x |
19 | D | diamond |
20 | d | thin_diamond |
21 | | | |
22 | _ | |
23 | P | plus_filled |
24 | X | x_filled |
25 | 0(int) | tickleft |
26 | 1(int) | tickright |
27 | 2(int) | tickup |
28 | 3(int) | tickdown |
29 | 4(int) | caretleft |
30 | 5(int) | caretright |
31 | 6(int) | caretup |
32 | 7(int) | caretdown |
33 | 8(int) | caretleftbase |
34 | 9(int) | caretrightbase |
35 | 10(int) | caretupbase |
36 | 11(int) | caretdownbase |
37 | | nothing |

#### linestyle：
id | linestyle | name |
---|---|---|
0 | - | solid |
1 | : | dotted |
2 | -- | dashed |
3 | -. | dashdot |
4 | None | |

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段mcolor，msize和malpha，其中mcolor和msize为一维int数组，malpha为一维float数组，falpha取值范围[0,1]
json数据中不要添加注释

### 要求：
mcolor，msize和malpha大小都为m，m为数据对象的个数
mcolor为散点图点的颜色，msize为散点图点的大小，malpha为散点图点的透明度
参考下面这个对应表来设计，返回对应颜色的id，大小和透明度，如果用户没有提出颜色，大小或透明度，则选择一个你认为合适的颜色，大小和透明度，使图表整洁美观，如无特殊说明不同的使用相同的颜色和大小，使用不同的透明度做区分

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，根据提供的格式和要求返回成json格式

### 格式：
包含2个字段bcolor和hatch，这2个字段均为一维int数组
json数据中不要添加注释

### 要求：
bcolor和hatch的大小都为m，m为数据对象的个数
bcolor为填充颜色，hatch为填充样式
参考下面这个对应表来设计，返回对应的形状和颜色的id，如果用户没有提出形状和颜色，则选择一个你认为合适的形状和颜色，使图表整洁美观，如无特殊说明，不同数据对象的hatch相同

### hatch：
id | hatch | name |
---|---|---|
0 | / | Diagonal Line (Forward) |
1 | \ | Diagonal Line (Backward) |
2 | | | Vertical Line |
3 | - | Horizontal Line |
4 | + | Cross (Vertical + Horizontal) |
5 | x | Crossed Diagonal Lines |
6 | o | Small Circles |
7 | O | Large Circles |
8 | . | Dots |
9 | * | Stars |
10 | | nothing |

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，根据提供的格式和要求返回成json格式

### 格式：
包含6个字段marker，linelinestyle，baselinestyle，mcolor，lcolor和bcolor，这6个字段均为一维int数组
json数据中不要添加注释

### 要求：
marker，linelinestyle，baselinestyle，mcolor，lcolor和bcolor的大小都为m，m为数据对象的个数
marker为数据点的形状，linelinestyle为主线的形状，baselinestyle为基准线线的形状，mcolor为数据点的颜色，lcolor为主线的颜色，bcolor为基准线的颜色
参考下面这个对应表来设计，返回对应的形状和颜色的id，如果用户没有提出形状和颜色，则选择一个你认为合适的形状和颜色，使图表整洁美观，如无特殊说明同一数据对象的mcolor和lcolor相同，不同数据对象的marker和linelinestyle相同

#### marker：
id | marker | name |
---|---|---|
0 | . | point |
1 | , | pixel |
2 | o | circle |
3 | v | triangle_down |
4 | ^ | triangle_up |
5 | < | triangle_left |
6 | > | triangle_right |
7 | 1 | tri_down |
8 | 2 | tri_up |
9 | 3 | tri_left |
10 | 4 | tri_right |
11 | 8 | octagon |
12 | s | square |
13 | p | pentagon |
14 | * | star |
15 | h | hexagon1 |
16 | H | hexagon2 |
17 | + | plus |
18 | x | x |
19 | D | diamond |
20 | d | thin_diamond |
21 | | | |
22 | _ | |
23 | P | plus_filled |
24 | X | x_filled |
37 | | nothing |

#### linestyle：
id | linestyle | name |
---|---|---|
0 | - | solid |
1 | : | dotted |
2 | -- | dashed |
3 | -. | dashdot |
4 | None | |

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，根据提供的格式和要求返回成json格式

### 格式：
包含2个字段fcolor和falpha，其中fcolor为int类型，falpha为float类型，falpha取值范围[0,1]
json数据中不要添加注释

### 要求：
fcolor为填充的颜色，falpha为填充的透明度
参考下面这个对应表来设计，返回对应颜色的id和透明度，如果用户没有提出颜色或透明度，则选择一个你认为合适的颜色和透明度，使图表整洁美观

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，根据提供的格式和要求返回成json格式

### 格式：
包含2个字段fcolor和falpha，其中fcolor为一维int数组，falpha为一维float数组，falpha取值范围[0,1]
json数据中不要添加注释

### 要求：
fcolor和falpha大小都为m，m为数据对象的个数
fcolor为填充的颜色，falpha为填充的透明度
参考下面这个对应表来设计，返回对应颜色的id和透明度，如果用户没有提出颜色或透明度，则选择一个你认为合适的颜色和透明度，使图表整洁美观，如无特殊说明使用相同的颜色，使用不同的透明度来区分不同的数据，透明度递进设置且小于0.5

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，根据提供的格式和要求返回成json格式

### 格式：
包含1个字段color，其中color为一维int数组
json数据中不要添加注释

### 要求：
color的大小为m，m为数据对象的个数
color为阶梯线的颜色
参考下面这个对应表来设计，返回对应颜色的id，如果用户没有提出颜色，则选择一个你认为合适的颜色，使图表整洁美观

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含6个字段marker，linestyle，mcolor，lcolor，thought和reason，其中marker，linestyle，mcolor和lcolor为一维int数组，thought和reason为string类型
json数据中不要添加注释

### 要求：
marker，linestyle，mcolor和lcolor的大小都为m，m为数据对象的个数
marker为点的形状，linestyle为线的形状，mcolor为点的颜色，lcolor为线的颜色，thought为你的分析思路，reason为你的选择原因
参考下面这个对应表来设计，返回对应的形状和颜色的id，如果用户没有提出形状和颜色，则选择一个你认为合适的形状和颜色，使图表整洁美观，如无特殊说明同一数据对象的mcolor和lcolor相同，不同数据对象的marker和linestyle相同
先给出thought和reason，再给出别的数据

#### marker：
id | marker | name |
---|---|---|
0 | . | point |
1 | , | pixel |
2 | o | circle |
3 | v | triangle_down |
4 | ^ | triangle_up |
5 | < | triangle_left |
6 | > | triangle_right |
7 | 1 | tri_down |
8 | 2 | tri_up |
9 | 3 | tri_left |
10 | 4 | tri_right |
11 | 8 | octagon |
12 | s | square |
13 | p | pentagon |
14 | * | star |
15 | h | hexagon1 |
16 | H | hexagon2 |
17 | + | plus |
18 | x | x |
19 | D | diamond |
20 | d | thin_diamond |
21 | | | |
22 | _ | |
23 | P | plus_filled |
24 | X | x_filled |
25 | 0(int) | tickleft |
26 | 1(int) | tickright |
27 | 2(int) | tickup |
28 | 3(int) | tickdown |
29 | 4(int) | caretleft |
30 | 5(int) | caretright |
31 | 6(int) | caretup |
32 | 7(int) | caretdown |
33 | 8(int) | caretleftbase |
34 | 9(int) | caretrightbase |
35 | 10(int) | caretupbase |
36 | 11(int) | caretdownbase |
37 | | nothing |

#### linestyle：
id | linestyle | name |
---|---|---|
0 | - | solid |
1 | : | dotted |
2 | -- | dashed |
3 | -. | dashdot |
4 | None | |

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段mcolor，msize，malpha，thought和reason，其中mcolor和msize为一维int数组，malpha为一维float数组，falpha取值范围[0,1]，thought和reason为string类型
json数据中不要添加注释

### 要求：
mcolor，msize和malpha大小都为m，m为数据对象的个数
mcolor为散点图点的颜色，msize为散点图点的大小，malpha为散点图点的透明度，thought为你的分析思路，reason为你的选择原因
参考下面这个对应表来设计，返回对应颜色的id，大小和透明度，如果用户没有提出颜色，大小或透明度，则选择一个你认为合适的颜色，大小和透明度，使图表整洁美观，如无特殊说明不同的使用相同的颜色和大小，使用不同的透明度做区分
先给出thought和reason，再给出别的数据

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段bcolor，hatch，thought和reason，其中bcolor和hatch为一维int数组，thought和reason为string类型
json数据中不要添加注释

### 要求：
bcolor和hatch的大小都为m，m为数据对象的个数
bcolor为填充颜色，hatch为填充样式，thought为你的分析思路，reason为你的选择原因
参考下面这个对应表来设计，返回对应的形状和颜色的id，如果用户没有提出形状和颜色，则选择一个你认为合适的形状和颜色，使图表整洁美观，如无特殊说明，不同数据对象的hatch相同
先给出thought和reason，再给出别的数据

### hatch：
id | hatch | name |
---|---|---|
0 | / | Diagonal Line (Forward) |
1 | \ | Diagonal Line (Backward) |
2 | | | Vertical Line |
3 | - | Horizontal Line |
4 | + | Cross (Vertical + Horizontal) |
5 | x | Crossed Diagonal Lines |
6 | o | Small Circles |
7 | O | Large Circles |
8 | . | Dots |
9 | * | Stars |
10 | | nothing |

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含8个字段marker，linelinestyle，baselinestyle，mcolor，lcolor，bcolor，thought和reason，其中marker，linelinestyle，baselinestyle，mcolor，lcolor，bcolor为一维int数组，thought和reason为string类型
json数据中不要添加注释

### 要求：
marker，linelinestyle，baselinestyle，mcolor，lcolor和bcolor的大小都为m，m为数据对象的个数
marker为数据点的形状，linelinestyle为主线的形状，baselinestyle为基准线线的形状，mcolor为数据点的颜色，lcolor为主线的颜色，bcolor为基准线的颜色，thought为你的分析思路，reason为你的选择原因
参考下面这个对应表来设计，返回对应的形状和颜色的id，如果用户没有提出形状和颜色，则选择一个你认为合适的形状和颜色，使图表整洁美观，如无特殊说明同一数据对象的mcolor和lcolor相同，不同数据对象的marker和linelinestyle相同
先给出thought和reason，再给出别的数据

#### marker：
id | marker | name |
---|---|---|
0 | . | point |
1 | , | pixel |
2 | o | circle |
3 | v | triangle_down |
4 | ^ | triangle_up |
5 | < | triangle_left |
6 | > | triangle_right |
7 | 1 | tri_down |
8 | 2 | tri_up |
9 | 3 | tri_left |
10 | 4 | tri_right |
11 | 8 | octagon |
12 | s | square |
13 | p | pentagon |
14 | * | star |
15 | h | hexagon1 |
16 | H | hexagon2 |
17 | + | plus |
18 | x | x |
19 | D | diamond |
20 | d | thin_diamond |
21 | | | |
22 | _ | |
23 | P | plus_filled |
24 | X | x_filled |
37 | | nothing |

#### linestyle：
id | linestyle | name |
---|---|---|
0 | - | solid |
1 | : | dotted |
2 | -- | dashed |
3 | -. | dashdot |
4 | None | |

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段fcolor，falpha，thought和reason，其中fcolor为int类型，falpha为float类型，falpha取值范围[0,1]，thought和reason为string类型
json数据中不要添加注释

### 要求：
fcolor为填充的颜色，falpha为填充的透明度，thought为你的分析思路，reason为你的选择原因
参考下面这个对应表来设计，返回对应颜色的id和透明度，如果用户没有提出颜色或透明度，则选择一个你认为合适的颜色和透明度，使图表整洁美观
先给出thought和reason，再给出别的数据

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段fcolor，falpha，thought和reason，其中fcolor为一维int数组，falpha为一维float数组，falpha取值范围[0,1]，thought和reason为string类型
json数据中不要添加注释

### 要求：
fcolor和falpha大小都为m，m为数据对象的个数
fcolor为填充的颜色，falpha为填充的透明度，thought为你的分析思路，reason为你的选择原因
参考下面这个对应表来设计，返回对应颜色的id和透明度，如果用户没有提出颜色或透明度，则选择一个你认为合适的颜色和透明度，使图表整洁美观，如无特殊说明使用相同的颜色，使用不同的透明度来区分不同的数据，透明度递进设置且小于0.5
先给出thought和reason，再给出别的数据

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段color，thought和reason，其中color为一维int数组，thought和reason为string类型
json数据中不要添加注释

### 要求：
color的大小为m，m为数据对象的个数
color为阶梯线的颜色，thought为你的分析思路，reason为你的选择原因
参考下面这个对应表来设计，返回对应颜色的id，如果用户没有提出颜色，则选择一个你认为合适的颜色，使图表整洁美观
先给出thought和reason，再给出别的数据

#### color：
id | color |
0 | blue |
1 | green |
2 | red |
3 | cyan |
4 | magenta |
5 | yellow |
6 | black |
7 | white |

### 用户需求:
"""

"""
根据用户的需求和之前提取的数据设计图表坐标轴范围和刻度，根据提供的格式和要求返回成json格式

### 格式：
包含6个字段xmin，xmax，xstep，ymin，ymax和ystep，这6个字段均为int或float类型
json数据中不要添加注释

### 要求：
xmin为x轴的最小值，xmax为x轴的最大值，xstep为x轴的刻度间隔，ymin为y轴的最小值，ymax为y轴的最大值，ystep为y轴的刻度间隔
根据用户的要求来设置坐标轴范围和刻度，如果用户没有提出范围，则选择一个你认为合适的范围，使图表整洁美观

### 用户需求:
"""

"""
根据用户的需求和之前提取的数据设计图表坐标轴范围和刻度，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含6个字段xmin，xmax，xstep，ymin，ymax，ystep，thought和reason其中xmin，xmax，xstep，ymin，ymax和ystep为int或float类型，thought和reason为string类型
json数据中不要添加注释

### 要求：
xmin为x轴的最小值，xmax为x轴的最大值，xstep为x轴的刻度间隔，ymin为y轴的最小值，ymax为y轴的最大值，ystep为y轴的刻度间隔，thought为你的分析思路，reason为你的选择原因
根据用户的要求来设置坐标轴范围和刻度，如果用户没有提出范围，则选择一个你认为合适的范围，使图表整洁美观
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的需求和之前提取的数据设计图表的标题和坐标轴的标签，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段xlabel，ylabel和title和，这3个字段均为string类型
json数据中不要添加注释

### 要求：
title为图表的标题，xlabel为x轴的标签，ylabel为y轴的标签
根据用户的要求来设置标题和标签，如果用户没有提出标题和标签，则选择一个你认为合适的标题和标签，如无特殊说明使用与用户需求同样的语言，使图表通俗易懂

### 用户需求:
"""

"""
根据用户的需求和之前提取的数据设计图表的标题和坐标轴的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段xlabel，ylabel，title和，thought和reason，这5个字段均为string类型
json数据中不要添加注释

### 要求：
title为图表的标题，xlabel为x轴的标签，ylabel为y轴的标签，thought为你的分析思路，reason为你的选择原因
根据用户的要求来设置标题和标签，如果用户没有提出标题和标签，则选择一个你认为合适的标题和标签，如无特殊说明使用与用户需求同样的语言，使图表通俗易懂
先给出thought和reason，再给出别的数据

### 用户需求:
"""

"""
根据用户的要求，参考之前提供的设计格式，继续修改图表，根据当前设计参数，生成新的设计参数，返回成json格式，json的字段数量与字段名与当前设计参数相同，注意修改的参数前后维数要一致
json数据中不要添加注释

### 用户的要求：
{}

### 当前设计参数：
{}
"""

"""
根据用户的要求，继续修改之前的数据，返回成json格式，json的字段数量与字段名与之前的数据相同，注意修改的参数前后维数要一致
json数据中不要添加注释

### 用户的要求：
{}

### 之前的数据：
{}
"""

"""
根据用户的要求，参考之前提供的设计格式，继续修改图表，根据当前设计参数，生成新的设计参数，返回成json格式，json的字段数量与字段名与当前设计参数相同，注意修改的参数前后维数要一致
再额外加上thought和reason两个字段，thought为你的分析思路，reason为你的选择原因
json数据中不要添加注释，先给出thought和reason，再给出别的数据

### 用户的要求：
{}

### 当前设计参数：
{}
"""

"""
根据用户的要求，继续修改之前的数据，并给出你的想法和原因，返回成json格式，json的字段数量与字段名与之前的数据相同，注意修改的参数前后维数要一致
再额外加上thought和reason两个字段，thought为你的分析思路，reason为你的选择原因
json数据中不要添加注释，先给出thought和reason，再给出别的数据

### 用户的要求：
{}

### 之前的数据：
{}
"""

def main():
    
    while True:
        # 导入大模型
        with open('config/config.json', 'r', encoding = 'utf-8') as jsfile:
            js = json.load(jsfile)
            client = OpenAI(api_key = js['key'], base_url = js['base'])
            llmmodel = js['model']

        # 初始菜单
        input = input_group(
            "AI visualisation data analysis",
            [
                textarea("Please describe what you want to analyse:", rows = 20, placeholder="Elements analysed", name="demand"),
                select("Whether or not it forces thinking:", options=["Yes", "No"], value="No", name="flag"),
                actions(buttons=[{'label': 'Make the figure', 'value': 0},
                                 {'label': "Modify the configuration file", 'value': -1, 'color': 'warning'}], name="act")
            ]
        )

        if input['act'] == -1:
            while True:
                with open('config/config.json', 'r', encoding='utf-8') as file:
                    text = file.read()
                
                config = input_group(
                    "Modify the configuration file",
                    [
                        textarea(value = text, rows = 10, name = "text"),
                        actions(buttons = [{'label': 'Save', 'value': 1},
                                           {'label': 'OpenAi standard format', 'value': 2},
                                           {'label': 'DeepSeek standard format', 'value': 3},
                                           {'label': 'Ollama standard format', 'value': 4},
                                           {'label': 'LmStudio standard format', 'value': 5},
                                           {'label': 'Back', 'value': 0, 'color': 'warning'}], name='action')
                    ]
                )

                match config['action']:
                    case 0:
                        break

                    case 1:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            file.write(config['text'])
                        break

                    case 2:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            json.dump(OpenAiConfigExample, file, ensure_ascii=False, indent=4)

                    case 3:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            json.dump(DeepSeekConfigExample, file, ensure_ascii=False, indent=4)
                    
                    case 4:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            json.dump(OllamaConfigExample, file, ensure_ascii=False, indent=4)

                    case 5:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            json.dump(LmStudioConfigExample, file, ensure_ascii=False, indent=4)

            continue

        # 选择是否强制思考
        match input['flag']:

            # 不强制思考
            case 'No':
                text_in = input['demand']

                # 第1阶段：选择图表类型
                messages1 = [{"role": "user", "content": prompt1a + text_in}]

                openai_out = client.chat.completions.create(model = llmmodel, messages = messages1).choices[0].message.content
                print(openai_out)
                type = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                messages1.append({"role": "assistant", "content": openai_out})

                match type["id"]:
                    # 线型图
                    case 0:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a0
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a0
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                                                style["marker"], style["linestyle"], style["mcolor"], style["lcolor"],
                                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                label["xlabel"], label["ylabel"], label["title"])
                    
                    # 散点图
                    case 1:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a1
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a1
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.ScatterInterface(data["x"], data["y"],
                                                                   style["mcolor"], style["msize"], style["malpha"],
                                                                   range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                   label["xlabel"], label["ylabel"], label["title"])
                    
                    # 条形图
                    case 2:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a2
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a2
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.BarInterface(data["x"], data["y"], data["ylabel"],
                                                               style["bcolor"], style["hatch"],
                                                               range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                               label["xlabel"], label["ylabel"], label["title"])

                    # 茎叶图
                    case 3:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a3
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a3
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                                                style["marker"], style["linelinestyle"], style["baselinestyle"], style["mcolor"], style["lcolor"], style["bcolor"],
                                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                label["xlabel"], label["ylabel"], label["title"])

                    # 填充区域图
                    case 4:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a4
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a4
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.FillBetweenInterface(data["x"], data["y1"], data["y2"], data["ylabel"],
                                                                       style["fcolor"], style["falpha"],
                                                                       range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                       label["title"], label["xlabel"], label["ylabel"])

                    # 堆叠区域图
                    case 5:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a5
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a5
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StackplotInterface(data["x"], data["y"], data["ylabel"],
                                                                     style["fcolor"], style["falpha"],
                                                                     range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                     label["title"], label["xlabel"], label["ylabel"])

                    # 阶梯图
                    case 6:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a6
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a6
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5a + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                                                  style["color"],
                                                                  range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                  label["title"], label["xlabel"], label["ylabel"])

                # 组装数据
                config_now = style | range | label
                message_new = [{"role": "user", "content": prompt3.split("### 用户需求:")[0]},
                               {"role": "user", "content": prompt4a.split("### 用户需求:")[0]},
                               {"role": "user", "content": prompt5a.split("### 用户需求:")[0]},
                               {"role": "user", "content": "### 用户需求:\n"+text_in}]

                img_stream = io.BytesIO()
                fig.savefig(img_stream, format='png')
                img_stream.seek(0)
                put_text("Preview image:")
                put_image(img_stream.read())
                
                # 继续修改
                while True:
                    next = input_group(
                        "Continuing modifications",
                        [
                            textarea("Please describe the request you are modifying:", rows = 5, placeholder="Your request", name="demand"),
                            actions(buttons=[{'label': 'Edit the format', 'value': 1},
                                             {'label': 'Edit the data', 'value': 2},
                                             {'label': 'Show the figure', 'value': 0},
                                             {'label': "Reconstruct", 'value': -1, 'color': 'warning'}
                                             ], name="act")
                        ]
                    )

                    match next['act']:
                        case -1:
                            fig.close()
                            clear()
                            break

                        case 0:
                            fig.show()
                        
                        case 1:
                            fig.close()

                            prompt_new = prompt_newa1.format(next['demand'], config_now)

                            openai_out = client.chat.completions.create(model = llmmodel, messages = message_new + [{"role": "user", "content": prompt_new}]).choices[0].message.content
                            print(openai_out)
                            config_now = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        case 2:
                            fig.close()

                            prompt_new = prompt_newa2.format(next['demand'], data)

                            openai_out = client.chat.completions.create(model = llmmodel, messages = [{"role": "user", "content": prompt_new}]).choices[0].message.content
                            print(openai_out)
                            data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")



                    match type["id"]:
                        case 0:
                            fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                                                    config_now["marker"], config_now["linestyle"], config_now["mcolor"], config_now["lcolor"],
                                                                    config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                    config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 1:
                            fig = MatplotlibInterface.ScatterInterface(data["x"], data["y"],
                                                                       config_now["mcolor"], config_now["msize"], config_now["malpha"],
                                                                       config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                       config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 2:
                            fig = MatplotlibInterface.BarInterface(data["x"], data["y"], data["ylabel"],
                                                                   config_now["bcolor"], config_now["hatch"],
                                                                   config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                   config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 3:
                            fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                                                    config_now["marker"], config_now["linelinestyle"], config_now["baselinestyle"], config_now["mcolor"], config_now["lcolor"], config_now["bcolor"],
                                                                    config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                    config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 4:
                            fig = MatplotlibInterface.FillBetweenInterface(data["x"], data["y1"], data["y2"], data["ylabel"],
                                                                           config_now["fcolor"], config_now["falpha"],
                                                                           config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                           config_now["title"], config_now["xlabel"], config_now["ylabel"])
                        
                        case 5:
                            fig = MatplotlibInterface.StackplotInterface(data["x"], data["y"], data["ylabel"],
                                                                         config_now["fcolor"], config_now["falpha"],
                                                                         config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                         config_now["title"], config_now["xlabel"], config_now["ylabel"])
                        
                        case 6:
                            fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                                                      config_now["color"],
                                                                      config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                      config_now["title"], config_now["xlabel"], config_now["ylabel"])
                            
                    img_stream = io.BytesIO()
                    fig.savefig(img_stream, format='png')
                    img_stream.seek(0)
                    clear()
                    put_text("Preview image:")
                    put_image(img_stream.read())

            # 强制思考
            case 'Yes':
                text_in = input['demand']

                # 第1阶段：选择图表类型
                messages1 = [{"role": "user", "content": prompt1b + text_in}]

                openai_out = client.chat.completions.create(model = llmmodel, messages = messages1).choices[0].message.content
                print(openai_out)
                type = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                messages1.append({"role": "assistant", "content": openai_out})

                match type["id"]:
                    # 线型图
                    case 0:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b0
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b0
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                                                style["marker"], style["linestyle"], style["mcolor"], style["lcolor"],
                                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                label["xlabel"], label["ylabel"], label["title"])
                    
                    # 散点图
                    case 1:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b1
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b1
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.ScatterInterface(data["x"], data["y"],
                                                                   style["mcolor"], style["msize"], style["malpha"],
                                                                   range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                   label["xlabel"], label["ylabel"], label["title"])

                    # 条形图
                    case 2:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b2
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b2
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.BarInterface(data["x"], data["y"], data["ylabel"],
                                                               style["bcolor"], style["hatch"],
                                                               range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                               label["xlabel"], label["ylabel"], label["title"])

                    # 茎叶图
                    case 3:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b3
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b3
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                                                style["marker"], style["linelinestyle"], style["baselinestyle"], style["mcolor"], style["lcolor"], style["bcolor"],
                                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                label["xlabel"], label["ylabel"], label["title"])

                    # 填充区域图
                    case 4:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b4
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b4
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.FillBetweenInterface(data["x"], data["y1"], data["y2"], data["ylabel"],
                                                                       style["fcolor"], style["falpha"],
                                                                       range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                       label["title"], label["xlabel"], label["ylabel"])

                    # 堆叠区域图
                    case 5:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b5
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b5
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StackplotInterface(data["x"], data["y"], data["ylabel"],
                                                                     style["fcolor"], style["falpha"],
                                                                     range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                     label["title"], label["xlabel"], label["ylabel"])

                    # 阶梯图
                    case 6:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b6
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b6
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                                                  style["color"],
                                                                  range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                  label["title"], label["xlabel"], label["ylabel"])
                        
                # 组装数据
                config_now = style | range | label
                message_new = [{"role": "user", "content": prompt3.split("### 用户需求:")[0]},
                               {"role": "user", "content": prompt4b.split("### 用户需求:")[0]},
                               {"role": "user", "content": prompt5b.split("### 用户需求:")[0]},
                               {"role": "user", "content": "### 用户需求:\n"+text_in}]

                img_stream = io.BytesIO()
                fig.savefig(img_stream, format='png')
                img_stream.seek(0)
                put_text("Preview image:")
                put_image(img_stream.read())
                
                # 继续修改
                while True:
                    next = input_group(
                        "Continuing modifications",
                        [
                            textarea("Please describe the request you are modifying:", rows = 5, placeholder="请描述您的要求：", name="demand"),
                            actions(buttons=[{'label': 'Edit the format', 'value': 1},
                                             {'label': 'Edit the data', 'value': 2},
                                             {'label': 'Show the figure', 'value': 0},
                                             {'label': "Reconstruct", 'value': -1, 'color': 'warning'}
                                             ], name="act")
                        ]
                    )

                    match next['act']:
                        case -1:
                            fig.close()
                            clear()
                            break

                        case 0:
                            fig.show()
                        
                        case 1:
                            fig.close()

                            prompt_new = prompt_newb1.format(next['demand'], config_now)

                            openai_out = client.chat.completions.create(model = llmmodel, messages = message_new + [{"role": "user", "content": prompt_new}]).choices[0].message.content
                            print(openai_out)
                            config_now = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        case 2:
                            fig.close()

                            prompt_new = prompt_newb2.format(next['demand'], data)

                            openai_out = client.chat.completions.create(model = llmmodel, messages = [{"role": "user", "content": prompt_new}]).choices[0].message.content
                            print(openai_out)
                            data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")



                    match type["id"]:
                        case 0:
                            fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                                                    config_now["marker"], config_now["linestyle"], config_now["mcolor"], config_now["lcolor"],
                                                                    config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                    config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 1:
                            fig = MatplotlibInterface.ScatterInterface(data["x"], data["y"],
                                                                       config_now["mcolor"], config_now["msize"], config_now["malpha"],
                                                                       config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                       config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 2:
                            fig = MatplotlibInterface.BarInterface(data["x"], data["y"], data["ylabel"],
                                                                   config_now["bcolor"], config_now["hatch"],
                                                                   config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                   config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 3:
                            fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                                                    config_now["marker"], config_now["linelinestyle"], config_now["baselinestyle"], config_now["mcolor"], config_now["lcolor"], config_now["bcolor"],
                                                                    config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                    config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 4:
                            fig = MatplotlibInterface.FillBetweenInterface(data["x"], data["y1"], data["y2"], data["ylabel"],
                                                                           config_now["fcolor"], config_now["falpha"],
                                                                           config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                           config_now["title"], config_now["xlabel"], config_now["ylabel"])
                        
                        case 5:
                            fig = MatplotlibInterface.StackplotInterface(data["x"], data["y"], data["ylabel"],
                                                                         config_now["fcolor"], config_now["falpha"],
                                                                         config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                         config_now["title"], config_now["xlabel"], config_now["ylabel"])
                        
                        case 6:
                            fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                                                      config_now["color"],
                                                                      config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                      config_now["title"], config_now["xlabel"], config_now["ylabel"])
                            
                    img_stream = io.BytesIO()
                    fig.savefig(img_stream, format='png')
                    img_stream.seek(0)
                    clear()
                    put_text("Preview image:")
                    put_image(img_stream.read())

