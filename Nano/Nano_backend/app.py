from flask import Flask, request, render_template, redirect, url_for, session, flash, make_response,send_file

app = Flask(__name__)
@app.route('/')
def index():
    return {'message': 'Success!', 'data': 'no data!'}, 200

@app.route('/api/calseq', methods=['POST'])
def calseq():
    try:
        data=request.get_json()

        output = ""
        n=data['seqNum']
        ol=data['overLapLen']
        num_cm=data['num_cm']

        # n=int(data['seqNum'])
        # ol=int(data['overLapLen'])
        # num_cm=int(data['numOfCm'])
        guiv=list(data['eachSeq'])
        v1=[[] for i in range(n)]
        guin=0
        for i in range(len(guiv)):
            if(guiv[i]!='\n'):
                v1[guin].append(guiv[i].upper())
            else:
                guin=guin+1

        print(n,v1,ol,num_cm)
        output=control(n,v1,ol,num_cm)
        print(output)
        # contenate the list output to a string
        output = ''.join(output)
        
        return {'message': 'Success!', 'data': output}, 200
    except:
        return {'message': 'Fail!', 'data': 'no data!'}, 400

@app.route('/api/download', methods=['POST'])
def download_csv():
    try:
        data=request.get_json()
        num_cm=data['num_cm']
        import csv
        with open('data.csv','w') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(['Primer Name', 'Sequence', 'Length'])
            #writer.writerow([num_cm, 2, 2])
            for ki in range(len(csv_seq)):
                t1="F"+str(int((ki+2)/2))+"-F"
                t2="F"+str(int((ki+2)/2))+"-R"
                if((ki+1)%2==1):
                    writer.writerow([t1, csv_seq[ki], len(csv_seq[ki])-num_cm])
                else:
                    writer.writerow([t2, csv_seq[ki], len(csv_seq[ki])-num_cm])
            # csvfile.close()
        response = make_response(open('data.csv', 'r').read()) # 创建一个响应对象
        response.headers['Content-Disposition'] = 'attachment; filename=data.csv' # 设置响应头
        return {'message': 'Success!'}, 200
    except:
        return {'message': 'Fail!'}, 400


import sys
sys.setrecursionlimit(100000)
import copy
csv_seq=[]

def reverse(r):
    fr=[]
    for i in range(len(r)-1,-1,-1):
        if(r[i]=='A'):
            fr.append('T')
        if(r[i]=='T'):
            fr.append('A')
        if(r[i]=='C'):
            fr.append('G')
        if(r[i]=='G'):
            fr.append('C')
        if(r[i]=='*'):
            fr.append('*')
    return fr


def same(m1,v1,ol):
    samel=[]
    samem=1

    for i in range(0,len(m1)-1):
        samel.append(v1[i][len(v1[i])-m1[i][0]:len(v1[i])]+v1[i+1][0:m1[i][1]])

    samel.append(v1[len(m1)-1][len(v1[len(m1)-1])-m1[len(m1)-1][0]:len(v1[len(m1)-1])]+v1[0][0:m1[len(m1)-1][1]])
    for i in range(0,len(m1)-1):
        for j in range(i+1, len(m1)):
            samen=0
            for k in range(ol):
                if(samel[i][k]!=samel[j][k]):
                    samen=samen+1
            if(samen/ol<0.3):
                samem=0

    return samem




def delta_G_Calculation1(x):    # for the calculation of primers
    nstar=0
    marker=0
    for i in range(0,len(x)):
        if (x[i]=='*'):
            marker=1
            nstar=nstar+1
    if(marker==1):
        for kcm in range(nstar):
            x.remove('*')

    nn=0
    for i in range(len(x)-1):
        if(x[i]=='A' and x[i+1]=='A'):
            nn=nn-1.00
        if(x[i]=='A' and x[i+1]=='T'):
            nn=nn-0.88
        if(x[i]=='A' and x[i+1]=='C'):
            nn=nn-1.44
        if(x[i]=='A' and x[i+1]=='G'):
            nn=nn-1.28
        if(x[i]=='T' and x[i+1]=='A'):
            nn=nn-0.58
        if(x[i]=='T' and x[i+1]=='T'):
            nn=nn-1.00
        if(x[i]=='T' and x[i+1]=='C'):
            nn=nn-1.30
        if(x[i]=='T' and x[i+1]=='G'):
            nn=nn-1.45
        if(x[i]=='C' and x[i+1]=='A'):
            nn=nn-1.45
        if(x[i]=='C' and x[i+1]=='T'):
            nn=nn-1.28
        if(x[i]=='C' and x[i+1]=='C'):
            nn=nn-1.84
        if(x[i]=='C' and x[i+1]=='G'):
            nn=nn-2.17
        if(x[i]=='G' and x[i+1]=='A'):
            nn=nn-1.30
        if(x[i]=='G' and x[i+1]=='T'):
            nn=nn-1.44
        if(x[i]=='G' and x[i+1]=='C'):
            nn=nn-2.24
        if(x[i]=='G' and x[i+1]=='G'):
            nn=nn-1.42
    if(x[0]=='G' or x[0]=='C'):
        nn=nn+0.98
    else:
        nn=nn+1.03
    if(x[len(x)-1]=='G' or x[len(x)-1]=='C'):
        nn=nn+0.98
    else:
        nn=nn+1.03
        
    return nn

def delta_G_Calculation2(x):     # for the calculation of overlapping zones
    nn=0
    for i in range(len(x)-1):
        if(x[i]=='A' and x[i+1]=='A'):
            nn=nn-1.00
        if(x[i]=='A' and x[i+1]=='T'):
            nn=nn-0.88
        if(x[i]=='A' and x[i+1]=='C'):
            nn=nn-1.44
        if(x[i]=='A' and x[i+1]=='G'):
            nn=nn-1.28
        if(x[i]=='T' and x[i+1]=='A'):
            nn=nn-0.58
        if(x[i]=='T' and x[i+1]=='T'):
            nn=nn-1.00
        if(x[i]=='T' and x[i+1]=='C'):
            nn=nn-1.30
        if(x[i]=='T' and x[i+1]=='G'):
            nn=nn-1.45
        if(x[i]=='C' and x[i+1]=='A'):
            nn=nn-1.45
        if(x[i]=='C' and x[i+1]=='T'):
            nn=nn-1.28
        if(x[i]=='C' and x[i+1]=='C'):
            nn=nn-1.84
        if(x[i]=='C' and x[i+1]=='G'):
            nn=nn-2.17
        if(x[i]=='G' and x[i+1]=='A'):
            nn=nn-1.30
        if(x[i]=='G' and x[i+1]=='T'):
            nn=nn-1.44
        if(x[i]=='G' and x[i+1]=='C'):
            nn=nn-2.24
        if(x[i]=='G' and x[i+1]=='G'):
            nn=nn-1.42
        
    return nn


def Tm_Calculation_easy(x):      # 进行Tm值的计算(简单版本)
    nn=0
    for i in range(len(x)):
        if (x[i]=='A' or x[i]=='T'):
            nn=nn+2
        if (x[i]=='G' or x[i]=='C'):
            nn=nn+4
    return nn

def Tm_Calculation_final1(x):      # 进行Tm值的计算（最终版本）for primers
    nn=0
    for i in range(len(x)):
        if (x[i]=='A' or x[i]=='T'):
            nn=nn+2
        if (x[i]=='G' or x[i]=='C'):
            nn=nn+4
    return nn


def Tm_Calculation_final2(x):      # 进行Tm值的计算（最终版本）for overlapping zones
    nn=0
    for i in range(len(x)):
        if (x[i]=='A' or x[i]=='T'):
            nn=nn+2
        if (x[i]=='G' or x[i]=='C'):
            nn=nn+4
    return nn


re=[]      #存储符合条件的重叠区域的结果
re2=[]     #存储所有判断过的重叠区域的结果

def deep_search(m1, v1, ol, t, n):
    tk=copy.deepcopy(m1)
    re2.append(tk)

    tm=[]
    for i in range(n-1):
        tem_seq=v1[i][len(v1[i])-m1[i][0]-1:len(v1[i])]+v1[i+1][0:m1[i][1]+1] # 得到重叠序列区域(两端各延伸一个，方便计算delta_G)
        tem_Tm=delta_G_Calculation2(tem_seq) # 得到重叠区域对应的delta_G值
        tm.append(tem_Tm)
    tem_seq=v1[n-1][len(v1[n-1])-m1[n-1][0]-1:len(v1[n-1])]+v1[0][0:m1[n-1][1]+1]
    tem_Tm=delta_G_Calculation2(tem_seq)
    tm.append(tem_Tm)

    max=tm[0]
    max_index=0
    min=tm[0]
    min_index=0
    for i in range(n):
        if (tm[i]>max):
            max=tm[i]
            max_index=i
        if (tm[i]<min):
            min=tm[i]
            min_index=i

    if (max-min<=t):
        mark=1
        #print(len(re))
        #print(m1)
        for i in range(len(re)):
            if (m1==re[i]):
                mark=0
        #print(re)
        #print(mark)
        if(mark==1 and same(m1,v1,ol)==1 ):
        #if(mark==1):
            t1=copy.deepcopy(m1)
            re.append(t1)
            '''
            for i in range(n-1):
                print("".join(v1[i][len(v1[i])-m1[i][0]:len(v1[i])]+v1[i+1][0:m1[i][1]]))
                print(delta_G_Calculation2(v1[i][len(v1[i])-m1[i][0]-1:len(v1[i])]+v1[i+1][0:m1[i][1]+1]))
            print("\n")
            '''

    for i in range(int(ol/2-4), int(ol/2+5)):
        #tm_now=Tm_Calculation(v1[max_index][len(v1[max_index])-i:len(v1[max_index])]+v1[max_index+1][0:16-i])
        #if (tm_now<max):
        m1[max_index][0]=i
        m1[max_index][1]=ol-i
        mark2=1
        for i in range(len(re2)):
            if (m1==re2[i]):
                mark2=0
        if(mark2==1):
            deep_search(m1, v1, ol, t, n)

    for i in range(int(ol/2-4), int(ol/2+5)):
        #tm_now=Tm_Calculation(v1[min_index][len(v1[min_index])-i:len(v1[min_index])]+v1[min_index+1][0:16-i])
        #if (tm_now>min):
        m1[min_index][0]=i
        m1[min_index][1]=ol-i
        mark2=1
        for i in range(len(re2)):
            if (m1==re2[i]):
                mark2=0
        if(mark2==1):
            deep_search(m1, v1, ol, t, n)
        



    '''
    if ((max-min)<=t and depth<=100):
        
        for i in range(n-1):
            print("".join(v1[i][len(v1[i])-m1[i][0]:len(v1[i])]+v1[i+1][0:m1[i][1]]))
            print(Tm_Calculation(v1[i][len(v1[i])-m1[i][0]:len(v1[i])]+v1[i+1][0:m1[i][1]]))
        print("\n")
         
    if (depth>100):
        return 
    else:
        for i in range(-4,5):
            if(i!=0):
                m1[max_index][0]=m1[max_index][0]+i
                m1[max_index][1]=m1[max_index][1]-i
                if(m1[max_index][0]>=4 and m1[max_index][0]<=12 and m1[max_index][1]>=4 and m1[max_index][1]<=12):
                    depth=depth+1
                    deep_search(m1, v1, ol, t, n, depth)
        for i in range(-4,5):
            if(i!=0):
                m1[min_index][0]=m1[min_index][0]+i
                m1[min_index][1]=m1[min_index][1]-i
                if(m1[min_index][0]>=4 and m1[min_index][0]<=12 and m1[min_index][1]>=4 and m1[min_index][1]<=12):
                    depth=depth+1
                    deep_search(m1, v1, ol, t, n, depth)
    '''

def primer_design(v1,mp,num_cm):
    
    primer=[[] for i in range(len(v1))]
    for i in range(len(v1)):
        if(i==0):       #最左端序列的引物设计
            tstar=['*']
            p4=v1[i][len(v1[i])-mp[i][0]-14:len(v1[i])-mp[i][0]]
            for kcm in range(num_cm):
                p4=p4+tstar
            p4=p4+v1[i][len(v1[i])-mp[i][0]:len(v1[i])]+v1[i+1][0:mp[i][1]]
            p2=v1[i][len(v1[i])-mp[i][0]-14:len(v1[i])]
            tkk=mp[len(v1)-1][1]+1
            for j in range(mp[len(v1)-1][1]+1,len(v1[i])-mp[i][0]-14):
                if(delta_G_Calculation1(v1[i][0:j])-delta_G_Calculation1(p2)>=0 and delta_G_Calculation1(v1[i][0:j+1])-delta_G_Calculation1(p2)<=0):
                    if(-delta_G_Calculation1(v1[i][0:j])+delta_G_Calculation1(p2)>delta_G_Calculation1(v1[i][0:j+1])-delta_G_Calculation1(p2)):
                        p1=v1[i][0:j]
                        tkk=j
                    else:
                        p1=v1[i][0:j+1]
                        tkk=j+1
            p3=v1[len(v1)-1][len(v1[len(v1)-1])-mp[len(v1)-1][0]:len(v1[len(v1)-1])]+v1[i][0:mp[len(v1)-1][1]]
            for kcm in range(num_cm):
                p3=p3+tstar
            p3=p3+v1[i][mp[len(v1)-1][1]:tkk]
            primer[i].append(p1)
            primer[i].append(p2)
            primer[i].append(p3)
            primer[i].append(reverse(p4))

        elif(i!=0 and i!=len(v1)-1):        #中间序列的引物设计
            tstar=['*']
            p4=v1[i][len(v1[i])-mp[i][0]-14:len(v1[i])-mp[i][0]]
            for kcm in range(num_cm):
                p4=p4+tstar
            p4=p4+v1[i][len(v1[i])-mp[i][0]:len(v1[i])]+v1[i+1][0:mp[i][1]]
            p2=v1[i][len(v1[i])-mp[i][0]-14:len(v1[i])]
            tkk=mp[i-1][1]+1
            for j in range(mp[i-1][1]+1,len(v1[i])-mp[i][0]-14):
                if(delta_G_Calculation1(v1[i][0:j])-delta_G_Calculation1(p2)>=0 and delta_G_Calculation1(v1[i][0:j+1])-delta_G_Calculation1(p2)<=0):
                    if(-delta_G_Calculation1(v1[i][0:j])+delta_G_Calculation1(p2)>delta_G_Calculation1(v1[i][0:j+1])-delta_G_Calculation1(p2)):
                        p1=v1[i][0:j]
                        tkk=j
                    else:
                        p1=v1[i][0:j+1]
                        tkk=j+1
            p3=v1[i-1][len(v1[i-1])-mp[i-1][0]:len(v1[i-1])]+v1[i][0:mp[i-1][1]]
            for kcm in range(num_cm):
                p3=p3+tstar
            p3=p3+v1[i][mp[i-1][1]:tkk]
            primer[i].append(p1)
            primer[i].append(p2)
            primer[i].append(p3)
            primer[i].append(reverse(p4))

        elif(i==len(v1)-1):         #最右端序列的引物设计
            tstar=['*']
            p4=v1[i][len(v1[i])-mp[i][0]-14:len(v1[i])-mp[i][0]]
            for kcm in range(num_cm):
                p4=p4+tstar
            p4=p4+v1[i][len(v1[i])-mp[i][0]:len(v1[i])]+v1[0][0:mp[i][1]]
            p2=v1[i][len(v1[i])-mp[i][0]-14:len(v1[i])]
            tkk=mp[i-1][1]+1
            for j in range(mp[i-1][1]+1,len(v1[i])-mp[i][0]-14):
                if(delta_G_Calculation1(v1[i][0:j])-delta_G_Calculation1(p2)>=0 and delta_G_Calculation1(v1[i][0:j+1])-delta_G_Calculation1(p2)<=0):
                    if(-delta_G_Calculation1(v1[i][0:j])+delta_G_Calculation1(p2)>delta_G_Calculation1(v1[i][0:j+1])-delta_G_Calculation1(p2)):
                        p1=v1[i][0:j]
                        tkk=j
                    else:
                        p1=v1[i][0:j+1]
                        tkk=j+1
            p3=v1[i-1][len(v1[i-1])-mp[i-1][0]:len(v1[i-1])]+v1[i][0:mp[i-1][1]]
            for kcm in range(num_cm):
                p3=p3+tstar
            p3=p3+v1[i][mp[i-1][1]:tkk]
            primer[i].append(p1)
            primer[i].append(p2)
            primer[i].append(p3)
            primer[i].append(reverse(p4))

    return primer



def control(n,v1,ol,num_cm):
    final_output=[]
    v2=[[] for i in range(n)] # v2用于依次储存互补的片段序列

    #ol=16
    t=15

    for i in range(n):          # 找到互补的片段序列
        for j in range (len(v1[i])):
            if(v1[i][j]=='A'):
                v2[i].append('T')
            if(v1[i][j]=='T'):
                v2[i].append('A')
            if(v1[i][j]=='C'):
                v2[i].append('G')
            if(v1[i][j]=='G'):
                v2[i].append('C')

    m1=[[] for i in range(n)] # m1用于储存重叠片段的位置
    for i in range(n):
        m1[i].append(int(ol/2))
        m1[i].append(int(ol/2))

    #print(v1[0][len(v1[0])-m1[0][0]:len(v1[0])]+v1[1][0:m1[0][1]])



    deep_search(m1, v1, ol, t, n)
    #print(re)

    Tm_min=1000
    Tm_min_index=0
    for i in range(len(re)):
        tm=[]
        for j in range(n-1):
            tem_seq=v1[j][len(v1[j])-re[i][j][0]-1:len(v1[j])]+v1[j+1][0:re[i][j][1]+1] # 得到重叠序列区域(两端各延伸一个碱基，方便计算delta_G)
            tem_Tm=delta_G_Calculation2(tem_seq) # 得到重叠区域对应的delta_G值
            tm.append(tem_Tm)
        tem_seq=v1[n-1][len(v1[n-1])-re[i][n-1][0]-1:len(v1[n-1])]+v1[0][0:re[i][n-1][1]+1]
        tem_Tm=delta_G_Calculation2(tem_seq)
        tm.append(tem_Tm)

        max=tm[0]
        min=tm[0]
        for j in range(n):
            if (tm[j]>max):
                max=tm[j]
            if (tm[j]<min):
                min=tm[j]
        if(max-min<Tm_min):
            Tm_min=max-min
            Tm_min_index=i

    print(re[Tm_min_index])
    final_output.append("".join(list(str(re[Tm_min_index]))))
    final_output.append("".join('\n'))
    final_output.append("".join("Overlapping Zone:"))
    final_output.append("".join('\n'))
    print("Overlapping Zone:")
    for j in range(n-1):
            tem_seq=v1[j][len(v1[j])-re[Tm_min_index][j][0]:len(v1[j])]+v1[j+1][0:re[Tm_min_index][j][1]]
            print("".join(tem_seq))
            print(delta_G_Calculation2(v1[j][len(v1[j])-re[Tm_min_index][j][0]-1:len(v1[j])]+v1[j+1][0:re[Tm_min_index][j][1]+1]))
            final_output.append("".join(tem_seq))
            final_output.append("".join('\n'))
            final_output.append("".join(list(str(delta_G_Calculation2(v1[j][len(v1[j])-re[Tm_min_index][j][0]-1:len(v1[j])]+v1[j+1][0:re[Tm_min_index][j][1]+1])))))
            final_output.append("".join('\n'))

    tem_seq=v1[n-1][len(v1[n-1])-re[Tm_min_index][n-1][0]:len(v1[n-1])]+v1[0][0:re[Tm_min_index][n-1][1]]
    print("".join(tem_seq))
    final_output.append("".join(tem_seq))
    final_output.append("".join('\n'))
    print(delta_G_Calculation2(v1[n-1][len(v1[n-1])-re[Tm_min_index][n-1][0]-1:len(v1[n-1])]+v1[0][0:re[Tm_min_index][n-1][1]+1]))
    final_output.append("".join(list(str(delta_G_Calculation2(v1[n-1][len(v1[n-1])-re[Tm_min_index][n-1][0]-1:len(v1[n-1])]+v1[0][0:re[Tm_min_index][n-1][1]+1])))))
    final_output.append("".join('\n'))

    print("\n")
    final_output.append("".join('\n'))
    primer=primer_design(v1,re[Tm_min_index],num_cm)

    for i in range(len(primer)):
        print("Fragment",i+1,":")
        final_output.append("".join("Fragment "))
        final_output.append("".join(list(str(i+1))))
        final_output.append("".join(":\n"))
        for j in range(3):
            print("".join(primer[i][j]))
            final_output.append("".join(primer[i][j]))
            if(j==2):
                csv_seq.append("".join(primer[i][j]))
            final_output.append("".join("\n"))
            print(Tm_Calculation_easy(primer[i][j]))
            final_output.append("".join(list(str(Tm_Calculation_easy(primer[i][j])))))
            final_output.append("".join("\n"))
            print(delta_G_Calculation1(primer[i][j]))
            final_output.append("".join(list(str(delta_G_Calculation1(primer[i][j])))))
            final_output.append("".join("\n"))
        print("".join(primer[i][3]))
        final_output.append("".join(primer[i][3]))
        csv_seq.append("".join(primer[i][3]))
        final_output.append("".join("\n"))
        print(Tm_Calculation_easy(primer[i][3]))
        final_output.append("".join(list(str(Tm_Calculation_easy(primer[i][3])))))
        final_output.append("".join("\n"))
        print(delta_G_Calculation1(reverse(primer[i][3])))
        final_output.append("".join(list(str(delta_G_Calculation1(reverse(primer[i][3]))))))
        final_output.append("".join("\n"))
        print("\n")
        final_output.append("".join("\n"))

    print("".join(final_output))
    return final_output






if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8100, debug=True)
        
