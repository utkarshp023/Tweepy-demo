import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime

consumer_key = "udJwhxC0JJMd2Agjghags9qBy"
consumer_secret = "UUEM0wIK1T39R871DuO2bE2bhZoBoe0cJ3hHlREQ8NqwsX1GW1"

access_token = "4844884717-71Kjg2PqxfDSHZ5da2UIDjwJ5QnUIixvByVax2U"
access_token_secret = "2vcJITSM0K8jlxqZhsI38yGoeLbt9Tqce1qbVcDsGsrLc"
count = 0
count_fin = 0
file_name=[]
st = ""

#This is a basic listener that just prints received tweets to stdout.
class Listener(StreamListener):                       
                            
        def on_data(self, data):
            global count
            global count_fin
            global file_name
            global st
            while (count < 10):
                with open(st,'a') as tf:
                    tf.write(data)
                    count = count + 1
                    if(count != 10):
                        return True
                print (data)

            count_fin = count_fin + 1
            tf.close()
            st = ""
            st = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            st+=str(count_fin)
            st+=".json" 
            if count_fin>9:
                self.part2()
                quit()
            file_name.append(st)
            count = 0
            return True


        def on_error(self, status):
            print (status)


        def part2(self):
            c = 1
            o_f = str(c)
            o_f+=".txt"
            for item in file_name:
                print(item,"\n")
                input_file=open(item, 'r')
                output_file=open(o_f, 'ab')
                dat = []
                lines = input_file.read().splitlines()
                for line in lines:
                        if len(line) == 0:
                                continue
                        dict = json.loads(line)
                        dat.append(dict)
                
                for element in dat:
                    output_str = ""
                    my_dict={}
                    my_dict['title']=element.get('created_at')
                    my_dict['description']=element.get('text')
                    my_dict['id']=element.get('user').get('name')
                    output_str = my_dict['title']
                    output_str+=" ---------- "
                    output_str+=my_dict['id']
                    output_str+=" ----------- "
                    output_str+=my_dict['description']
                    output_str+='\n'
                    output_file.write(output_str.encode("utf-8"))
                    
                output_file.close()
                input_file.close()
                c = c+1
                o_f = str(c)
                o_f+=".txt"
               

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = Listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    st = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    st+=".json"
    file_name.append(st)        
    stream = Stream(auth, l)
    stream.filter(track=['india', 'congress', 'bjp', 'aap', 'trs', 't20', 'cricket', 'football', 'politics'])    
       
