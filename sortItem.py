list = [{'views':10}, {'views':12}, {'views':8}, {'views':16}]
temp = 0
for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        if list[i]['views'] < list[j]['views']:
            temp = list[i]['views']
            list[i]['views'] = list[j]['views']
            list[j]['views'] = temp
    print(list[i]['views'])

for i in [0, 1, 2, 3]


   1st:  i = 0; j -> (1,2,3)
    #  j = 1;
    #     list[i=0]['views'] = 10
    #    list[j=1]['views'] = 12
    #    10 < 12 -> temp = 10; list[i=0]['views'] = list[j=1]['views'] =  12; list[j=1]['views'] = 10   list [j][views]
    #    end; list[i=0]['views'] = 12
    # j = 2;
    #     list[i=0]['views'] = 12
    #    list[j=2]['views'] = 8
    #
    #    end; list[i=0]['views'] = 12; temp = 10
    # j = 3;
    #     list[i = 0]['views'] = 12
    #     list[j = 3]['views'] = 16
    #     temp = list[i = 0]['views'] = 12
    #     list[i = 0]['views'] = list[j = 3]['views'] = 16
    #     list[j = 3]['views'] = 12
    #     end;  list[i = 0]['views'] = 16
    list[0]['views'] = 16
