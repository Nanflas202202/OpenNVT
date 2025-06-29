#coding:UTF-8
'''
.KVTI(KWY Virus Trainer Ini File)文件格式：Var1=[Value]，用换行分格
#该文件由AI生成（文心一言 V3.5），不能确保可靠性
#kvtiWriter()默认读写Settings.kvti，kvtiWriter2()可以读写自定义名称的kvti文件
#Copyleft CE2B Studio 2022-2024
'''

def ReadKVTIFiles(filename, specified_x):  
    """  
    读取.kvti文件，返回指定x值对应的y值。  
  
    :param filename: 字符串，.kvti文件的路径。  
    :param specified_x: 字符串，指定的x值。  
    :return: 字符串，如果找到对应的x值，则返回其y值；否则返回None。  
    """  
    # 尝试打开文件  
    try:  
        with open(filename, 'r') as file:  
            # 逐行读取文件  
            for line in file:  
                # 去除每行两端的空白字符，如空格、换行符等  
                stripped_line = line.strip()  
                # 检查行是否为空或注释（这里假设不以#开头的行不是注释）  
                if stripped_line and not stripped_line.startswith('#'):  
                    # 尝试分割x和y，这里假设格式为'x=[y]'  
                    parts = stripped_line.split('=')  
                    if len(parts) == 2:  
                        x, y_with_brackets = parts  
                        # 去除y值两端的方括号  
                        y = y_with_brackets.strip('[]')  
                        # 检查是否匹配指定的x值  
                        if x.strip() == specified_x:  
                            return y  
            # 如果没有找到匹配的x值，则返回None  
            return None  
    except FileNotFoundError:  
        # 如果文件不存在，则抛出异常  
        print(f"Error: The file '{filename}' does not exist.")  
        raise  
    except Exception as e:  
        # 处理其他可能的异常  
        print(f"An error occurred: {e}")  
        raise  
  
# 示例用法  
# 假设有一个名为'example.kvti'的文件，内容如下：  
# a=[1]  
# b=[2]  
# c=[3]
"""  
result = ReadKVTIFiles('Settings.kvti', "Output")  
print(result)  # 应该输出: 2
"""
def kvtiWriter(x, y):  
    """  
    将x值与对应的y值写入当前目录下的Settings.kvti文件中。  
    如果已存在要写入的x值，则覆盖原有的x值；如果Settings.kvti不存在，则自动创建。  
  
    :param x: 字符串，x值。  
    :param y: 字符串，与x值对应的y值。  
    """  
    filename = 'Settings.kvti'  
    lines = []  
    x_found = False  
  
    # 尝试以读模式打开文件，如果文件不存在则捕获异常  
    try:  
        with open(filename, 'r') as file:  
            lines = file.readlines()  
    except FileNotFoundError:  
        # 文件不存在，无需处理，因为稍后我们将以写模式打开它  
        pass  
  
    # 遍历现有行，查找并替换x值（如果存在）  
    for i, line in enumerate(lines):  
        stripped_line = line.strip()  
        if stripped_line and not stripped_line.startswith('#') and stripped_line.split('=')[0].strip() == x:  
            # 找到了匹配的x值，替换为新的y值  
            lines[i] = f"{x}=[{y}]\n"  
            x_found = True  
  
    # 如果没有找到匹配的x值，将新的键值对添加到列表末尾  
    if not x_found:  
        lines.append(f"{x}=[{y}]\n")  
  
    # 将更新后的内容写回文件  
    with open(filename, 'w') as file:  
        file.writelines(lines)  
""" 
# 示例用法  
kvtiWriter('name', 'Jane Doe')  
kvtiWriter('age', '25')  
# 假设Settings.kvti之前不存在，现在它应该包含两行：'name=[Jane Doe]' 和 'age=[25]'
"""

def kvtiWriter2(x, y, Filename):  
    """  
    将x值与对应的y值写入到Filename.kvti文件中。  
    如果文件不存在，则创建文件；如果x值已存在，则覆盖原有的x值。  
  
    :param x: 字符串，x值。  
    :param y: 字符串，与x对应的y值。  
    :param Filename: 字符串，不含扩展名的文件名，实际文件名为Filename.kvti。  
    """  
    # 构建完整的文件名  
    filename = f"{Filename}.kvti"  
  
    # 尝试以追加模式打开文件，但实际上我们会根据x值的存在性来覆盖或添加内容  
    with open(filename, 'a+') as file:  
        # 将文件指针移动到文件开头  
        file.seek(0)  
        # 读取现有内容到内存中  
        lines = file.readlines()  
  
        # 初始化一个列表来存储将要写回文件的新内容  
        new_lines = []  
  
        # 遍历现有内容，寻找匹配的x值并替换，或者如果没有找到就添加新行  
        found = False  
        for line in lines:  
            stripped_line = line.strip()  
            if stripped_line and not stripped_line.startswith('#') and stripped_line.split('=')[0].strip() == x:  
                # 找到匹配的x值，写入新的x=y对（替换原有行）  
                new_lines.append(f"{x}=[{y}]\n")  
                found = True  
            else:  
                # 不是我们要替换的行，保留原样  
                new_lines.append(line)  
  
        # 如果没有找到匹配的x值，添加到文件末尾  
        if not found:  
            new_lines.append(f"{x}=[{y}]\n")  
  
        # 如果文件指针不在文件开头，移动到开头准备写入新内容  
        if file.tell() != 0:  
            file.seek(0)  
  
        # 清空文件内容（如果需要）  
        file.truncate(0)  
  
        # 写回新内容  
        file.writelines(new_lines)  

""" 
# 示例用法  
kvtiWriter2('name', 'Jane Doe', 'Test')  
kvtiWriter2('age', '25', 'Settings')  
# 现在Settings.kvti应该包含两行：name=[Jane Doe] 和 age=[25]

#难以置信，这里我最开始居然忘了注释掉了！
"""