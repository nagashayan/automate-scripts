import os

start = 0
incr = 15
end = start + incr
for i in range(1,11):
    command = "ffmpeg -i class00-subclass04-trial07.avi -ss " + str(start) + " -t " + str(incr) + " -c copy -an class00-subclass04-trial07-sample-0"+str(i)+".mp4"
    #command = "ffmpeg -i videoplayback.3gp -ss " + str(start) + " -t " + str(incr) + " -c copy -an friends0"+str(i)+".mp4"
    print(command)
    os.system(command)
    start = start + incr
    end = end + incr
