import os , re
try:
    import psutil
except:
    os.system('pip install psutil')
    import psutil
try:
    from sqlitedict import SqliteDict
except:
    os.system('pip install sqlitedict')
    from sqlitedict import SqliteDict
import datetime
import subprocess
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_bind_ips(except_ip_list=[] , except_ip_word_list=[] , except_keyword_list=[]):
    ips = psutil.net_if_addrs()
    result = []
    for name in ips:
        skip = False
        for blackkeyword in except_keyword_list:
            if blackkeyword in name:
                skip = True
                break
        if skip == True:continue

        for black_ip_keyword in except_ip_word_list:
            if black_ip_keyword in ips[name][1].address:
                skip = True
                break
        if skip == True:continue

        for black_ip in except_ip_list:
            if black_ip == ips[name][1].address:
                skip = True
                break
        if skip == True:continue

        result.append(ips[name][1].address)
    return result

def upload_file(src , remote, dst_folder , **kwargs): # rclone copy local:"F:\@ POOQ\[5GX] 월드베스트 그곳에 가면- 최고의 도시\E46.mp4" g01tv3:test.mp4
    ip = None
    mydict = SqliteDict('RcloneStorm.db', autocommit=True)
    for ip_candidate in kwargs['ips']:
        if ip_candidate not in mydict :
            mydict[ip_candidate] = {'lock' : False} # 없으면 초기생성
        if mydict[ip_candidate]['lock'] == False:
            mydict[ip_candidate] = {'lock': True}
            ip = ip_candidate
            break
    if ip == None:
        return 'ERROR'
    cmd = 'rclone %s local:"%s" %s:"%s" --bind %s' %(kwargs['mode'] , src , remote , dst_folder, ip)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               universal_newlines=True, encoding='utf-8')
    print("COMMAND\t",cmd)
    log = ""
    try:
        for line in process.stdout:
            log = log + line + "\n"
    except:
        pass
    mydict[ip] = {'lock': False}
    return log

def files_list(dir , skip_ext=[]):
    result = []
    for (path, dir, files) in os.walk(dir):
        for file in files:
            skip = False
            for ext in skip_ext:
                if ext == os.path.splitext(file)[1].lower() :
                    skip = True
                    break
            if skip == True:continue
            result.append(os.path.join(path, file))
    return result

def main(**kwargs):
    if len(kwargs['ips']) == 0 :
        print("ERROR\tThere is no internet you can use")
        return
    if len(kwargs['your_remote_list']) == 0 :
        print("ERROR\tThere is no Remote in your config (make rclone config)")
        return
    if len(kwargs['src_folder']) == 0 :
        print("ERROR\tThere is no folders you'd likely to upload.")
        return
    files = []
    for directory in kwargs['src_folder']:
        files += files_list(directory , skip_ext = kwargs['skip_ext'])


    ip_count = len(kwargs['ips'])
    kwargs['files'] = files
    mydict = SqliteDict('RcloneStorm.db', autocommit=True)
    temp_dict = {}
    for file in files:
        temp_dict[file] = {'lock' : False}
    mydict['file'] = temp_dict

    import multiprocessing
    def get_count(num , p=1):
        list = []
        allocate = int(num/p)
        for n in range(p):
            list.append(allocate)
        list[p-1] += num % p
        print("프로세스당 할당량",list)
        return list

    process = []
    start = time.time()
    count_list = get_count(len(files), ip_count)

    # ip별로 분배해준다
    index = 0
    split_list = []
    for c in count_list:
        split_list.append(files[index : index + c - 1])
        index += c

    # Process 생성
    for upload_files in split_list:
        p = multiprocessing.Process(target=up, args=(upload_files,) ,kwargs=kwargs, daemon=True)
        process.append(p)
        p.start()
    for p in process:
        p.join()
    print("TOTAL DURATION FOR UPLOADING\t" , time.time() - start , "SEC")
    return

def up(upload_files , **kwargs):
    for file in upload_files:
        mydict = SqliteDict('RcloneStorm.db', autocommit=True)
        if file in mydict['file'] and mydict['file'][file]['lock'] == False:
            mydict['file'][file]['lock'] = True
            base_remote_path = kwargs['remote_folder_path']
            folder_depth = kwargs['folder_depth']
            your_remote_list = kwargs['your_remote_list']
            if os.path.exists(file) == True:
                depth_list = []
                fullPath = file
                while True:
                    try:
                        a = os.path.split(fullPath)
                        path, filename = a[0], a[1]
                        depth_list.append(filename)
                        if filename == "":
                            raise ValueError
                        fullPath = path
                    except:
                        break
                base_remote_path_2 = ""
                depth = 0
                while folder_depth > depth:
                    base_remote_path_2 += "\\" + depth_list[folder_depth - depth]
                    depth += 1

                total_path = base_remote_path + base_remote_path_2
                # 경로를 잡아줬으니, ip랑 remote를 정해줘야.


            true_remote = False
            for remote in your_remote_list:
                today = datetime.datetime.now().day
                if remote not in mydict:
                    mydict[remote] = mydict[remote] = {'traffic': 0, 'lock': False, 'day': today}  # 초기 생성
                if mydict[remote]['day'] != today:  # 중간중간에 날짜가 달라지면 리셋해줘야지
                    mydict[remote] = {'traffic': 0, 'lock': False, 'day': today}  # 날짜가 다르면 traffic 을 리셋해준다
                if mydict[remote]['traffic'] / 1024 / 1024 / 1024 < kwargs['max_transfer']:  # OKAY
                    # print("UPLOAD\t",file, remote, total_path, ip)
                    true_remote = remote
                    break
            if true_remote == False:
                print("사용가능한 Remote 가 없습니다.")
                return
            print(bcolors.OKGREEN + 'UPLOAD START\t', true_remote, '\t', file, '\t\t',  bcolors.ENDC)
            mydict[true_remote]['traffic'] += os.path.getsize(file)
            log = upload_file(file, true_remote, total_path, **kwargs)
            if log == "ERROR":
                print(bcolors.WARNING + 'UPLOAD ERROR\t', true_remote, '\t', file, '\t\t', bcolors.ENDC)
                return
            print(bcolors.OKBLUE + 'UPLOAD DONE\t\t', true_remote, '\t', file, '\t\t',  bcolors.ENDC)



if __name__ == '__main__':
    if 'RcloneStorm.db' in os.listdir(os.getcwd()):
        os.remove('RcloneStorm.db')
    # Rclone Remote 네임 리스트, 사용할 Remote를 적는다
    your_remote_list = ['g01','g02','g03','g04','g05','g06','g07','g08','g09','g10','g11','g12','g13','g14','g15']

    # 해당 폴더 내에 있는 모든 파일을 올려버린다.
    src_folder = [r'F:\# TIER2\@ TVing', r'F:\# TIER2\@ POOQ']

    # 업로드 완료 후 지울 것이면 MOVE, 복사만 할것이면 COPY
    mode = 'move'

    # 구글 팀 드라이브 내의 어떤 폴더에 저장할 것인가
    remote_folder_path = "TV\\TEMP"

    # 소스 파일의 path에서 몇 단계의 폴더 깊이를 살릴 것인가
    # 0 이면 파일만
    # 1이면 폴더\파일
    # Example )
    # 값이 1이면, F:\@ POOQ\KBS 뉴스\KBS_NEWS_20190128-NEXT.mp4 에서 KBS 뉴스\KBS_NEWS_20190128-NEXT.mp4 를 말하는 것으로,
    # TV\TEMP\KBS 뉴스\KBS_NEWS_20190128-NEXT.mp4 이런 식으로 올라간다.
    # 값이 0이면 TV\TEMP\KBS_NEWS_20190128-NEXT.mp4 이런 식으로 올라간다.
    folder_depth = 1

    # except_ip_list 는 해당 아이피는 무시
    # except_ip_word_list 는 해당 키워드가 포함된 ip는 무시
    # except_keyword_list 는 해당 키워드의 NIC 네이밍을 무시 (이더넷 7 이런거)
    ips = get_bind_ips(except_ip_list=['192.168.130.1','192.168.164.1'] , except_ip_word_list=['169.254','127.0.0.1'] , except_keyword_list=['Loopback'])

    # 계정당 최대 전송용량 , 단위는 기가바이트
    max_transfer = 700

    # 특정 확장자 무시
    skip_ext = ['.txt' , '.db']

    main(src_folder = src_folder , your_remote_list = your_remote_list, ips = ips ,
         remote_folder_path=remote_folder_path , folder_depth=folder_depth , max_transfer=max_transfer,
         mode=mode , skip_ext = skip_ext)
