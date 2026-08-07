"""提示词：思考模式（由原 prompt/b/ 目录生成，勿手改）。"""

# Phase 1：选择图表类型
CHART_TYPE_SELECT = r"""根据用户的需求分析需要画出哪种图表，给出你的选择，想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段thought，reason和id，thought和reason为string类型，id为int类型

### 要求：
thought为你的分析思路，reason为你的选择原因，id为选择的图表类型的编号
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

# Phase 2：按图表类型(0-6)提取数据
DATA_EXTRACT = {
    0: r"""根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段，thought，reason，x，y和ylabel，其中thought和reason为string类型，x为一维数组，y为二维数组，ylabel为一维数组，x和y均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
""",
    1: r"""根据用户的需求提取出你作图表需要的数据以及数据，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段thought，reason，x和y，其中x和y为一维数组，thought和reason为string类型，x和y为int或float类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，x和y的各自的第n项表示第n个点的x轴坐标和y轴坐标
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
""",
    2: r"""根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段thought，reason，x，y和ylabel，其中thought和reason为string类型，x为一维数组，y为二维数组，ylabel为一维数组，x和y均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
""",
    3: r"""根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段thought，reason，x，y和ylabel，其中thought和reason为string类型，x为一维数组，y为二维数组，ylabel为一维数组，x和y均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
""",
    4: r"""根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含6个字段thought，reason，x，y1，y2和ylabel，其中thought和reason为string类型，x，y1和y2为一维数组，ylabel为单个字符串，x，y1和y2均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，x为自变量，y1和y2为两个不同的因变量，ylabel为数据对象的标签，x，y1和y2的大小均为n
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
""",
    5: r"""根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段thought，reason，x，y和ylabel，其中thought和reason为string类型，x为一维数组，y为二维数组，ylabel为一维数组，x和y均为int或float类型，ylabel为string类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，x为自变量，y为因变量，ylabel为数据对象的标签，x的大小为n，y的大小为m行n列，ylabel的大小为m，m为数据对象的个数
如果数据缺失则设置为空 
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
""",
    6: r"""根据用户的需求提取出你作图表需要的数据以及数据对应的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段thought，reason，position，value和label，其中thought和reason为string类型，position为一维数组，value为二维数组，label为一维数组，value为int或float类型，position为int类型且为连续递增的整数，label为string类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，position为自变量，value为因变量，label为数据对象的标签，position的大小为n，value的大小为m行n列，label的大小为m，m为数据对象的个数
如果数据缺失则设置为空
根据用户的要求来提取数据对象的标签，如无特殊说明则为该对象选择一个你认为合适的标签并使用与用户需求同样的语言
先给出thought和reason，再给出别的数据

### 用户需求:
""",
}

# Phase 3：按图表类型(0-6)设计样式
STYLE = {
    0: r"""根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含6个字段thought，reason，marker，linestyle，mcolor和lcolor，其中thought和reason为string类型，marker，linestyle，mcolor和lcolor为一维int数组
json数据中不要添加注释

### 要求：
marker，linestyle，mcolor和lcolor的大小都为m，m为数据对象的个数
thought为你的分析思路，reason为你的选择原因，marker为点的形状，linestyle为线的形状，mcolor为点的颜色，lcolor为线的颜色
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
""",
    1: r"""根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段thought，reason，mcolor，msize和malpha，其中thought和reason为string类型，mcolor和msize为一维int数组，malpha为一维float数组，falpha取值范围[0,1]
json数据中不要添加注释

### 要求：
mcolor，msize和malpha大小都为m，m为数据对象的个数
thought为你的分析思路，reason为你的选择原因，mcolor为散点图点的颜色，msize为散点图点的大小，malpha为散点图点的透明度
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
""",
    2: r"""根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段thought，reason，bcolor和hatch，其中thought和reason为string类型，bcolor和hatch为一维int数组
json数据中不要添加注释

### 要求：
bcolor和hatch的大小都为m，m为数据对象的个数
thought为你的分析思路，reason为你的选择原因，bcolor为填充颜色，hatch为填充样式
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
""",
    3: r"""根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含8个字段thought，reason，marker，linelinestyle，baselinestyle，mcolor，lcolor和bcolor，其中thought和reason为string类型，marker，linelinestyle，baselinestyle，mcolor，lcolor，bcolor为一维int数组
json数据中不要添加注释

### 要求：
marker，linelinestyle，baselinestyle，mcolor，lcolor和bcolor的大小都为m，m为数据对象的个数
thought为你的分析思路，reason为你的选择原因，marker为数据点的形状，linelinestyle为主线的形状，baselinestyle为基准线线的形状，mcolor为数据点的颜色，lcolor为主线的颜色，bcolor为基准线的颜色
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
""",
    4: r"""根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段thought，reason，fcolor和falpha，其中thought和reason为string类型，fcolor为int类型，falpha为float类型，falpha取值范围[0,1]
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，fcolor为填充的颜色，falpha为填充的透明度
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
""",
    5: r"""根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含4个字段thought，reason，fcolor和falpha，其中thought和reason为string类型，fcolor为一维int数组，falpha为一维float数组，falpha取值范围[0,1]
json数据中不要添加注释

### 要求：
fcolor和falpha大小都为m，m为数据对象的个数
thought为你的分析思路，reason为你的选择原因，fcolor为填充的颜色，falpha为填充的透明度
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
""",
    6: r"""根据用户的需求设计图表样式，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含3个字段thought，reason和color，其中thought和reason为string类型，color为一维int数组
json数据中不要添加注释

### 要求：
color的大小为m，m为数据对象的个数
thought为你的分析思路，reason为你的选择原因，color为阶梯线的颜色
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
""",
}

# Phase 4：坐标范围
RANGE = r"""根据用户的需求和之前提取的数据设计图表坐标轴范围和刻度，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含6个字段thought，reason，xmin，xmax，xstep，ymin，ymax和ystep，其中thought和reason为string类型，xmin，xmax，xstep，ymin，ymax和ystep为int或float类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，xmin为x轴的最小值，xmax为x轴的最大值，xstep为x轴的刻度间隔，ymin为y轴的最小值，ymax为y轴的最大值，ystep为y轴的刻度间隔
根据用户的要求来设置坐标轴范围和刻度，如果用户没有提出范围，则选择一个你认为合适的范围，使图表整洁美观
先给出thought和reason，再给出别的数据

### 用户需求:
"""

# Phase 5：标签
LABELS = r"""根据用户的需求和之前提取的数据设计图表的标题和坐标轴的标签，并给出你的想法和原因，根据提供的格式和要求返回成json格式

### 格式：
包含5个字段thought，reason，xlabel，ylabel和title，这5个字段均为string类型
json数据中不要添加注释

### 要求：
thought为你的分析思路，reason为你的选择原因，title为图表的标题，xlabel为x轴的标签，ylabel为y轴的标签
根据用户的要求来设置标题和标签，如果用户没有提出标题和标签，则选择一个你认为合适的标题和标签，如无特殊说明使用与用户需求同样的语言，使图表通俗易懂
先给出thought和reason，再给出别的数据

### 用户需求:
"""

# 修改链路
MODIFY_STYLE = r"""根据用户的要求，参考之前提供的设计格式，继续修改图表，根据当前设计参数，生成新的设计参数，返回成json格式，json的字段数量与字段名与当前设计参数相同，注意修改的参数前后维数要一致
再额外加上thought和reason两个字段，thought为你的分析思路，reason为你的选择原因
json数据中不要添加注释，先给出thought和reason，再给出别的数据

### 用户的要求：
{}

### 当前设计参数：
{}"""
MODIFY_DATA = r"""根据用户的要求，继续修改之前的数据，并给出你的想法和原因，返回成json格式，json的字段数量与字段名与之前的数据相同，注意修改的参数前后维数要一致
再额外加上thought和reason两个字段，thought为你的分析思路，reason为你的选择原因
json数据中不要添加注释，先给出thought和reason，再给出别的数据

### 用户的要求：
{}

### 之前的数据：
{}"""
