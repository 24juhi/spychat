import requests
from constant import BASE_URL , APP_ACCESS_TOKEN
from get_post_id import get_post_id
insta_username = raw_input('enter the user name:-')


def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    message = raw_input("Enter your Message:")
    paylod = {"access_token": APP_ACCESS_TOKEN, 'text': message}
    #print 'media_id'
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)

    print 'POST request url : %s' % (request_url)
    post_comment = requests.post(request_url,paylod).json()


    if post_comment['media'] ['code'] ==200:
        print  "Post comment Successfully"

    else:
        print "Sorry..! Unable to comment on post."

        exit()