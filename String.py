s = 'abcdef'
print(s[0::2])
print(s * 2)

t = ['s', 'i', 'l', 'y']
print(t[2])

print(9 // 2)

'''
print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
'''


def reverseWords(inpuT):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = inpuT.split(" ")                    # 分隔字符串

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]  # 将数组逆向储存

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    inpuT = 'I like runoob'
    rw = reverseWords(inpuT)
    print(rw)
