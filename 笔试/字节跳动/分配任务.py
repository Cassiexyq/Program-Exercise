# -*- coding: utf-8 -*-

# @Author: xyq

def getTask(time_ideas, n_cxy,n_idea):
    time = 0
    zx_idea = []
    finish_idea = []
    pm_idea_stack = {}
    n_x_idea = 0 # 表示可执行的idea数量
    while True:
        time += 1
        # if zx_idea == [] and n_idea == 0: break
        if n_idea == 0 and zx_idea == []: break
        if zx_idea != []:  # 到时间了的idea
            delete_idea = []
            for i in zx_idea:
                i[3] -= 1
                if i[3] == 0:
                    delete_idea.append(i)
            for i in delete_idea:
                zx_idea.remove(i)
                n_cxy += 1
                i.append(time)
                finish_idea.append(i)
        for t in time_ideas:  # 加入所有可执行的idea
            if t == time:
                for i in time_ideas[t]:
                    if i[0] not in pm_idea_stack:
                        pm_idea_stack[i[0]] = []
                    pm_idea_stack[i[0]].append(i) # 所有到时间的可执行的idea
                    n_x_idea += 1
                break
        while n_cxy > 0 and n_x_idea > 0: # 分配任务
            pm_want_idea = []
            for i in pm_idea_stack:
                if pm_idea_stack[i] !=[]: # 对到时间的可执行的排列优先
                    pm_want_idea.append(min(pm_idea_stack[i], key=lambda s: (-s[2], s[3], s[1])))
            if pm_want_idea!=[]:
                want_idea = min(pm_want_idea,key=lambda s:(s[3],s[0]))
                zx_idea.append(want_idea)
                pm_idea_stack[want_idea[0]].remove(want_idea)
                n_idea -= 1
                n_x_idea -= 1
                n_cxy -= 1
    finish_idea = sorted(finish_idea, key=lambda s: s[4])
    for i in finish_idea: print(i[5])

if __name__ == "__main__":
    all = list(map(int, input().strip().split(' ')))
    time_ideas = {}
    for i in range(all[2]):
        idea = list(map(int,input().strip().split(' ')))
        idea.append(i)
        if idea[1] not in time_ideas:
            time_ideas[idea[1]] = []
        time_ideas[idea[1]].append(idea)
    getTask(time_ideas,all[1],all[2])

