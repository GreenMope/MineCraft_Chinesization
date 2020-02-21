import json
import difflib
import re

with open('D:\Desktop\新建文本文档 (4).txt', 'r',encoding='UTF-8') as f:
    dict = json.load(f)

# matches = difflib.get_close_matches('block.minecraft',dict.keys(),1000, cutoff=0.4)

# for index in range(len(dict.keys())):
#     enchantment = re.match('enchantment.minecraft.', list(dict.keys())[index])
#     if (enchantment!=None):
#         with open('D:\Desktop\新建文本文档 (5).txt', 'a') as f:
#             f.write('map.put(' + '\"' + list(dict.keys())[index].replace('enchantment.minecraft.', '').replace('_',' ').title() + '\",\"' + dict[list(dict.keys())[index]] + '\");'+'\n')
#         print('map.put(' + '\"' + list(dict.keys())[index].replace('enchantment.minecraft.', '').replace('_',' ').title() + '\",\"' + dict[list(dict.keys())[index]] + '\");')
#

for index in range(len(dict.keys())):
    block = re.match('block.minecraft.', list(dict.keys())[index])
    banner = re.match('block.minecraft.banner.', list(dict.keys())[index])
    bed = re.match('block.minecraft.bed.', list(dict.keys())[index])
    if (block!=None and banner==None and bed==None):
        with open('D:\Desktop\新建文本文档 (8).txt', 'a') as f:
            f.write('map.put(' + '\"' + list(dict.keys())[index].replace('block.minecraft.', '') + '\",\"' + dict[list(dict.keys())[index]] + '\");'+'\n')
        print('map.put(' + '\"' + list(dict.keys())[index].replace('block.minecraft.', '') + '\",\"' + dict[list(dict.keys())[index]] + '\");')

for index in range(len(dict.keys())):
    item = re.match('item.minecraft.', list(dict.keys())[index])
    tippedArrow = re.match('item.minecraft.tipped', list(dict.keys())[index])
    firework = re.match('item.minecraft.firework', list(dict.keys())[index])
    debug = re.match('item.minecraft.debug', list(dict.keys())[index])
    potion = re.match('item.minecraft.potion', list(dict.keys())[index])
    splashPotion = re.match('item.minecraft.splash', list(dict.keys())[index])
    lingeringPotion = re.match('item.minecraft.lingering', list(dict.keys())[index])
    # if (potion!=None or splashPotion!=None or lingeringPotion!=None or tippedArrow!=None):
    #     temp = list(dict.keys())[index].replace('item.minecraft.', '').replace('_',' ').title()
    #     num = temp.rfind('.')
    #     if (num!=-1):
    #         temp = temp.split('.',2)[2] + ' ' + temp.split('.',2)[0]
    #         with open('D:\Desktop\新建文本文档 (5).txt', 'a') as f:
    #             f.write('map.put(' + '\"' +
    #               temp.rstrip() + '\",\"'
    #               + dict[list(dict.keys())[index]] + '\");'+'\n')
    #         print('map.put(' + '\"' +
    #           temp.rstrip() + '\",\"'
    #           + dict[list(dict.keys())[index]] + '\");')
    #     else:
    #         with open('D:\Desktop\新建文本文档 (5).txt', 'a') as f:
    #             f.write('map.put(' + '\"' +
    #               list(dict.keys())[index].replace('item.minecraft.', '').replace('_',' ').title() + '\",\"'
    #               + dict[list(dict.keys())[index]] + '\");'+'\n')
    #         print('map.put(' + '\"' +
    #               list(dict.keys())[index].replace('item.minecraft.', '').replace('_',' ').title() + '\",\"'
    #               + dict[list(dict.keys())[index]] + '\");')

    if (item!=None and firework==None and debug==None and potion==None and splashPotion==None and lingeringPotion==None and tippedArrow==None):
        with open('D:\Desktop\新建文本文档 (8).txt', 'a') as f:
            f.write('map.put(' + '\"' + list(dict.keys())[index].replace('item.minecraft.', '') + '\",\"' + dict[list(dict.keys())[index]] + '\");'+'\n')
        print('map.put(' + '\"' + list(dict.keys())[index].replace('item.minecraft.', '') + '\",\"' + dict[list(dict.keys())[index]] + '\");')


# for index in range(len(dict.keys())):
#     tippedArrow = re.match('item.minecraft.tipped', list(dict.keys())[index])
#     potion = re.match('item.minecraft.potion', list(dict.keys())[index])
#     splashPotion = re.match('item.minecraft.splash', list(dict.keys())[index])
#     lingeringPotion = re.match('item.minecraft.lingering', list(dict.keys())[index])
#     if (potion!=None or splashPotion!=None or lingeringPotion!=None or tippedArrow!=None):
#         temp = list(dict.keys())[index].replace('item.minecraft.', '')
#         num = temp.rfind('.')
#         if (num!=-1):
#             temp = temp.split('.',2)[2] + ' ' + temp.split('.',2)[0]
#             with open('D:\Desktop\新建文本文档 (7).txt', 'a') as f:
#                 f.write('map.put(' + '\"' +
#                   temp.rstrip() + '\",\"'
#                   + dict[list(dict.keys())[index]] + '\");'+'\n')
#             print('map.put(' + '\"' +
#               temp.rstrip() + '\",\"'
#               + dict[list(dict.keys())[index]] + '\");')



