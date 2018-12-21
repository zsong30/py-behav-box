from RESOURCES.GUI_elements_by_flav import convertString
import os
import threading
import subprocess

def load_expt_file(self):
    print("LOADING: ", self.expt_file_path_name)
    self.protocol = []
    self.conditions = []
    self.exptFileLines = []


    try:
        f = open(self.expt_file_path_name,'r')
        # Read Line by line

        for line in f:
            line = line.strip() # Remove leading and trailoing blanks and \n
            if not 'HAB_COND_EXT_AND_RECALL_VIs' in line:
                line = line.upper()
            print(line)
            self.exptFileLines.append(line)
            if line != "":
                condition={}

                if '[EXPERIMENT' in line:
                    EXPERIMENT = True
                    TONE1 = False
                    TONE2 = False
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = False
                elif '[TONE1' in line:
                    EXPERIMENT = False
                    TONE1 = True
                    TONE2 = False
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = False
                elif '[TONE2' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = True
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = False
                elif '[SHOCK]' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = False
                    SHOCK = True
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = False
                elif '[FREEZE]' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = False
                    SHOCK = False
                    FREEZE = True
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = False

                elif '[TOUCHSCREEN]' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = False
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = True
                    BAR_PRESS = False
                    SETUP = False

                elif '[BAR_PRESS]' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = False
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = True
                    SETUP = False

                elif '[PROTOCOL' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = False
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = True
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = False

                elif '[SETUP' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = False
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = True

                elif '[CONDITIONS' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = False
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = True
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = False

                elif '[END' in line:
                    EXPERIMENT = False
                    TONE1 = False
                    TONE2 = False
                    SHOCK = False
                    FREEZE = False
                    PROTOCOL = False
                    CONDITIONS = False
                    TOUCH = False
                    BAR_PRESS = False
                    SETUP = False


                if EXPERIMENT:
                    if 'EXPT_NAME' in line:
                        words = line.split('=')
                        self.Expt_Name = words[1].strip()
                        self.Expt_Name = self.Expt_Name.strip()
                        print(self.Expt_Name)

                    elif 'SUBJECT' in line:
                        words = line.split('=')
                        self.Subject = words[1].strip()
                        self.Subject = self.Subject.strip()
                        print(self.Subject)

                    elif 'EXPT_PATH' in line:
                        words = line.split('=')
                        self.datapath = words[1].strip()
                        self.datapath = self.datapath.strip()
                        print(self.datapath)
                    elif 'LOG_FILE_PATH' in line:
                        words = line.split('=')
                        log_file_path = words[1].strip()
                        log_file_path = log_file_path.strip()
                        print("LFP",log_file_path)
                    elif 'VIDEO_FILE_PATH' in line:
                        words = line.split('=')
                        video_file_path = words[1].strip()
                        video_file_path = video_file_path.strip()
                        print(video_file_path)
                    elif 'OPEN_EPHYS_PATH' in line:
                        if not self.open_ephys_started:
                            print('opening ephys')
                            self.open_ephys_started = True
                            words = line.split('=')
                            open_ephys_path = words[1].strip()
                            subprocess.Popen(open_ephys_path)
                    elif 'VI_TIMES_LIST_PATH' in line:
                        words = line.split('=')
                        self.VIs_file_path = words[1].strip()
                        print(self.VIs_file_path)

                elif TONE1:#TONE1
                    if 'DURATION' in line:
                        words = line.split('=')
                        self.Tone1_Duration = float(words[1].strip())
                        print("self.Tone1_Duration",self.Tone1_Duration)
                    if 'FREQ' in line:
                        words = line.split('=')
                        self.Tone1_Freq = float(words[1].strip())
                        print("self.Tone1_Freq: ",self.Tone1_Freq)
                    if 'VOL' in line:
                        words = line.split('=')
                        self.Tone1_Vol = float(words[1].strip())
                        print("self.Tone1_Vol: ",self.Tone1_Vol)

                elif TONE2:#TONE2
                    if 'DURATION' in line:
                        words = line.split('=')
                        self.Tone2_Duration = words[1].strip()
                        print("self.Tone2_Duration",self.Tone2_Duration)
                    if 'FREQ' in line:
                        words = line.split('=')
                        self.Tone2_Freq = float(words[1].strip())
                        print("self.Tone2_Freq: ",self.Tone2_Freq)
                    if 'VOL' in line:
                        words = line.split('=')
                        self.Tone2_Vol = float(words[1].strip())
                        print("self.Tone2_Vol: ",self.Tone2_Vol)

                elif TOUCH:
                    touch_image_dict={}
                    if 'IMAGES_PATH' in line:
                        words = line.split('=')
                        self.TOUCH_IMG_PATH = words[1].strip()
                        self.TOUCHSCREEN_USED = True
                    if 'COORDS' in line:
                        words = line.split('=')
                        imageCoords = words[1].split(':')
                        for i in range(len(imageCoords)):
                            for c in '()':
                                #Remove parenthesis from (x,y)
                                imageCoords[i] = imageCoords[i].replace(c, "")
                            imageCoordsStr = imageCoords[i].split(",")
                            self.touchImgCoords.append((int(imageCoordsStr[0]), int(imageCoordsStr[1])))
                    elif 'IMG' in line:
                        words = line.split('=')
                        imageInfo = words[1].split(":")
                        imageName = imageInfo[0].strip()
                        for c in '()':
                            #Remove parenthesis from rewards
                            imageInfo[1] = imageInfo[1].replace(c, "")
                        imgRewards = []
                        for probability in imageInfo[1].split(","):
                            imgRewards.append(int(probability))
                        self.touchImgs[imageName] = imgRewards

                elif BAR_PRESS:
                    self.BAR_PRESS_INDEPENDENT_PROTOCOL = True
                    if "VI" in line:
                        words = line.split('=')
                        VI = words[1].strip()
                        try:
                            self.var_interval_reward = int(VI)
                            print("var_interval_reward: ",self.var_interval_reward)
                        except:
                            print ("!!!!!!!!!!!VI must = a number in EXP file!!!!!!!!!!!!!!", )

                elif SHOCK:
                    if 'DURATION' in line:
                        words = line.split('=')
                        SDuration = words[1].strip()
                        self.Shock_Duration = float(SDuration.strip())
                        print(self.Shock_Duration)
                    if 'VOLTS' in line:
                        words = line.split('=')
                        V = words[1].strip()
                        self.Shock_V = float(V.strip())
                        print(self.Shock_V)
                    if 'AMPS' in line:
                        words = line.split('=')
                        amps = words[1].strip()
                        self.Shock_Amp = float(amps.strip())
                        print(self.Shock_Amp)

                elif FREEZE:
                    if 'DURATION' in line:
                        words = line.split('=')
                        Freeze_Duration = words[1].strip()
                        Freeze_Duration = Freeze_Duration.strip()
                        #print(Freeze_Duration)
                    if 'PIX' in line:
                        words = line.split('=')
                        Min_Pixels = words[1].strip()
                        Min_Pixels = Min_Pixels.strip()
                        #print(Min_Pixels)
                elif SETUP:
                    if "SETUP" not in line:
                        #print(line)
                        try:
                            words = line.split('=')
                            word1 = words[0].strip()
                            word1 = word1.upper()
                            word2 = words[1].strip() #Do NOT make this an upper() to retain True and False
                            word2 = word2.split("#") #IGNORES "#" FOLLOWED BY COMMENTS
                            word2 = word2[0].strip()
                            self.setup.append({word1:word2})
                        except:
                            self.setup.append({line:True}) # For lines without an '=' in them
                            #if line == 'END': PROTOCOL = False
                elif PROTOCOL:
                    if "PROTOCOL" not in line:
                        #print(line)
                        try:
                            words = line.split('=')
                            word1 = words[0].strip()
                            word1 = word1.upper()
                            word2 = words[1].strip() #Do NOT make this an upper() to retain True and False
                            word2 = word2.split("#") #IGNORES "#" FOLLOWED BY COMMENTS
                            word2 = word2[0].strip()
                            self.protocol.append({word1:word2})
                        except:
                            self.protocol.append({line:True}) # For lines without an '=' in them
                            #if line == 'END': self.protocol = False

                elif CONDITIONS:
                    print("self.conditions: ",line)
                    if "[CONDITIONS]" in line:
                        KEY_LINE = True

                    elif KEY_LINE: # CONDITION HEADING (i.e. all the KEYS)
                        keys = line.split(',') #list of condtions but need to be stripped of blanks and tabs
                        #print ("KEYS: ", keys)
                        KEY_LINE = False
                    else: # Not a CONDITION heading line, (i.e. all the VALUES)
                        values = line.split(',')
                        #print ("VALUES: ",values)

                        i=0
                        for val in values:
                            val = val.strip()
                            val = val.upper()
                            val = convertString(val)
                            condition[keys[i].strip()] = val #This strips keys, assigns a val to the key and creates condition dict

                            i+=1
                        self.conditions.append(condition)
                        #print (condition)
                else:
                    END_PROTOCOL = True
            else:# line == ""
                print("BLANK LINE")

        f.close()
        print(".......\n")
        print(self.touch_img_files)
    except OSError:
        print("NO SUCH FILE!!!!",self.expt_file_path_name)
        return False

    print("PROTOCOL LOADED]")
    print (self.protocol)
    for dct in self.protocol:
        for k,v in dct.items():
            print(str(k)+" = " + str(v))

    if self.VIs_file_path != "":
        try:
            #path,name = os.path.split(self.VIs_file_path)
            #VIs_file_path_COPY = name[:-4] + '_copy.txt'
            #VIs_file_path_COPY = os.path.join(self.newdatapath,VIs_file_path_COPY)
            f = open(self.VIs_file_path,'r')
            #fw = open(VIs_file_path_COPY,'w')
            # Read Line by line
            for line in f:
                #fw.write(line)
                self.VIFileLines.append(line)
                line = line.strip() # Remove leading and trailoing blanks and \n
                line = line.upper()
                print(line)
                if "HABITUATION" in line:
                    words = line.split(':')
                    words = words[1].strip()
                    words = words.split(',')
                    print("length of words: ",len(words))
                    for items in words:
                        num = items.strip()
                        print(num)
                        self.habituation_vi_times.append(int(num))
                if "CONDITIONING" in line:
                    words = line.split(':')
                    words = words[1].strip()
                    words = words.split(',')
                    print("length of words: ",len(words))
                    for items in words:
                        num = items.strip()
                        print(num)
                        self.conditioning_vi_times.append(int(num))
                if "EXTINCTION" in line:
                    words = line.split(':')
                    words = words[1].strip()
                    words = words.split(',')
                    print("length of words: ",len(words))
                    for items in words:
                        num = items.strip()
                        print(num)
                        self.extinction_vi_times.append(int(num))
                if "RECALL" in line:
                    words = line.split(':')
                    words = words[1].strip()
                    words = words.split(',')
                    print("length of words: ",len(words))
                    for items in words:
                        num = items.strip()
                        print(num)
                        self.recall_vi_times.append(int(num))
                print("VI FILE LOADED",self.VIs_file_path)
        except OSError:
            print("Could not open ",self.VIs_file_path)
            return False
    return True

def create_files(self):
    # DATA PATH + FILES

    #try:
    new_dir = os.path.join(self.datapath,self.Expt_Name)
    if not os.path.exists(new_dir ):  os.mkdir(new_dir)
    new_sub_dir = os.path.join(new_dir,self.date)
    if not os.path.exists(new_sub_dir ):os.mkdir(new_sub_dir)
    new_sub_dir = os.path.join(new_sub_dir,self.exptTime)
    if not os.path.exists(new_sub_dir ):os.mkdir(new_sub_dir)
    self.newdatapath = new_sub_dir
    expt_file_name_COPY = self.expt_file_name[:-4] + '_COPY.txt' # Removes the '.txt' from original name and adds 'COPY.txt'
    self.expt_file_path_name_COPY = os.path.join(self.newdatapath,expt_file_name_COPY)
    print(self.expt_file_path_name_COPY)

    log_file_name = self.Expt_Name + "-" + self.Subject + '-' +  self.dateTm + '-LOG_file'  + '.csv'
    self.log_file_path_name = os.path.join(self.newdatapath,log_file_name)
    print(self.log_file_path_name)

    video_file_name = self.Expt_Name + "-" + self.Subject + '-' +  self.dateTm + '-VIDEO_file' + '.avi'
    self.video_file_path_name = os.path.join(self.newdatapath,video_file_name)
    print(self.video_file_path_name)

    # COPY EXPT FILE TO EXPT FILE DATAPATH
    print("....................................\n")
    print("COPYING EXPT FILE", self.expt_file_path_name_COPY)
    try:
        exptfl = open(self.expt_file_path_name_COPY,'w')
    except:
        print("XXXXXX 1 could NOT copy of EXPT file",self.expt_file_path_name_COPY)
    try:
        for ln in self.exptFileLines:
            print (ln)
            if "EXPT_NAME" in ln:
                newln = "EXPT_NAME = " + self.Expt_Name

            if "SUBJECT" in ln:
                newln = "SUBJECT = " + self.Subject

            exptfl.write(newln+"\n")
        print("EXPT file copied",self.expt_file_path_name_COPY)
        exptfl.close()
    except:
        print("could NOT copy of EXPT file",self.expt_file_path_name_COPY)

    if self.VIs_file_path != "":
        try:
            path,name = os.path.split(self.VIs_file_path)
            VIs_file_path_COPY = name[:-4] + '_copy.txt'
            VIs_file_path_COPY = os.path.join(self.newdatapath,VIs_file_path_COPY)
            #f = open(self.VIs_file_path,'r')
            fw = open(VIs_file_path_COPY,'w')
            # w Line by line
            for ln in self.VIFileLines:
                fw.write(ln+"\n")
        except:
            print("COULD NOT WRITE VI FILE COPY", VIs_file_path_COPY)

def update_expt_file_copy(self):
    import fileinput
    print("....................................\n")
    print("UPDATING EXPT FILE", self.expt_file_path_name_COPY)
    try:
        exptfl = open(self.expt_file_path_name_COPY,'r+')

        for ln in exptfl:
            print (ln)
            if "EXPT_NAME" in ln:
                ln = "EXPT_NAME = " + self.Expt_Name + "\nSUBJECT = " + self.Subject
                prev_ln = ln
                exptfl.write(ln+"\n")
            if "SUBJECT" in ln:
                if ln == prev_ln: pass
                else:  ln = "SUBJECT = " + self.Subject
                break
            exptfl.write(ln+"\n")
        exptfl.close()
        return True
    except:
        print("COULD NOT UPDATE EXPT FILE", self.expt_file_path_name_COPY)
        return False